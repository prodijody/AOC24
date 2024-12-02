from collections import Counter
from pathlib import Path


def process_file(filename: str) -> tuple[list[int], list[int]]:
    """Read and parse two columns of integers from a file."""
    numbers = []
    with Path(filename).open() as file:
        numbers = [tuple(map(int, line.split())) for line in file]
    return tuple(zip(*numbers))  # Unzip into two separate lists


def calculate_absolute_diff(list1: list[int], list2: list[int]) -> int:
    """Calculate sum of absolute differences between sorted lists."""
    return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))


def calculate_common_product(list1: list[int], list2: list[int]) -> int:
    """Calculate sum of products for common numbers."""
    counter2 = Counter(list2)
    return sum(num * counter2[num] for num in list1 if num in counter2)


def main():
    list1, list2 = process_file("1_input.txt")
    print(calculate_absolute_diff(list1, list2))
    print(calculate_common_product(list1, list2))


if __name__ == "__main__":
    main()
