# Find the average of numbers (with explanations).

def average(*numbers) -> float:
    count = total = 0
    for num in numbers:
        total += num
        count += 1
    return total/count if count != 0 else 0


def main():
    avg_value = average(1, 2, 4, 10)
    print(f"Average: {avg_value}")

if __name__ == "__main__":
    main()