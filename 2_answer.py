from pathlib import Path
from typing import Sequence


def read_number_sequences(filename: str) -> list[tuple[int, ...]]:
    """Read sequences of numbers from file, each line as a tuple."""
    with Path(filename).open() as file:
        return [tuple(map(int, line.split())) for line in file]


def is_valid_sequence(sequence: Sequence[int]) -> bool:
    """
    Check if a sequence is valid based on rules:
    - Differences between adjacent numbers must be between 1 and 3
    - Direction of differences cannot change (must be monotonic)
    """
    if len(sequence) < 2:
        return True

    differences = [b - a for a, b in zip(sequence[:-1], sequence[1:])]

    # Check if all differences are between -3 and -1 OR 1 and 3
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    # Check if sequence is monotonic (all positive or all negative differences)
    return all(diff >= 0 for diff in differences) or all(
        diff <= 0 for diff in differences
    )


def count_valid_sequences(filename: str) -> int:
    """Count the number of valid sequences in the file."""
    sequences = read_number_sequences(filename)
    return sum(1 for seq in sequences if is_valid_sequence(seq))


def count_valid_sequences_with_error(filename: str) -> int:
    """Count the number of valid sequences in the file."""
    count = 0
    sequences = read_number_sequences(filename)
    for seq in sequences:
        if is_valid_sequence(seq):
            count += 1
            continue
        for x in range(0, len(seq)):
            temp = list(seq)
            del temp[x]
            if is_valid_sequence(temp):
                count += 1
                break
    return count


def main() -> None:
    result = count_valid_sequences("2_input.txt")
    print(f"Number of valid sequences: {result}")
    result = count_valid_sequences_with_error("2_input.txt")
    print(f"Number of valid sequences with error: {result}")


if __name__ == "__main__":
    main()
