# Print the Fibonacci series using the recursive method.
# Return the Nth value from the Fibonacci sequence.

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    # return n + fibonacci(n-1)
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-1] + i)
    return fib[-1]

def main():
    n: int = 5
    fib_value: int = fibonacci(n)
    print(f"Fibonacci value: {fib_value}")

if __name__ == "__main__":
    main()