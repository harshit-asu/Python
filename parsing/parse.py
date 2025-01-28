import time
import re
from multiprocessing import Pool
from collections import Counter
from typing import List
from memory_profiler import profile
import sys

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        retVal = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end-start} seconds.")
        return retVal
    return wrapper

def read_chunks(filename: str, chunk_size: int=10000):
    chunk = []
    with open(filename, 'r') as file:
        for line in file:
            chunk.append(line)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
    if chunk:
        yield chunk

def process_chunk(lines: List[str]) -> None:
    ipaddr = Counter()
    pattern = re.compile(r'(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    for line in lines:
        match = pattern.search(line)
        if match:
            ipaddr[match.groupdict()["ip"]] += 1
    return ipaddr

def aggregate_results(results: List[dict]) -> dict:
    total_ip_count = Counter()
    for ipaddr in results:
        total_ip_count.update(ipaddr)
    return total_ip_count

@timer
@profile
def parse(filename: str) -> dict:
    with Pool() as pool:
        chunk_generator = read_chunks(filename)
        results = pool.map(process_chunk, chunk_generator)
    return aggregate_results(results)

@timer
@profile
def parseTwo(filename: str) -> dict:
    pattern = re.compile(
        r'(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
    )
    results = Counter()
    with open(filename, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                results[match.groupdict()['ip']] += 1
    return results

def main():
    filename: str = sys.argv[1]
    parse(filename)
    parseTwo(filename)

if __name__ == "__main__":
    main()