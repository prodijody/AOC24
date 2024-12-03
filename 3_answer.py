import re
from pathlib import Path


def read_input_file(filename: str) -> list[tuple[int, ...]]:
    """Read sequences of numbers from file, each line as a tuple."""
    with Path(filename).open() as file:
        return file.read().replace("\n", "")


def find_multiples(input_text: str) -> list:
    pattern = re.compile(
        r"mul\([0-9]+,[0-9]+\)",
        re.IGNORECASE,
    )
    return re.findall(pattern, input_text)


def process_multiples(multiples: list) -> int:
    return sum(
        int(num1) * int(num2)
        for num1, num2 in [multiple[4:-1].split(",") for multiple in multiples]
    )


def find_multiples_do_dont(input_text: str) -> list:
    pattern = re.compile(
        r"mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)",
        re.IGNORECASE,
    )
    return re.findall(pattern, input_text)


def process_multiples_do_dont(multiples: list) -> int:
    result = 0
    run = True
    for multiple in multiples:
        if "mul" in multiple and run:
            num1, num2 = multiple[4:-1].split(",")
            result += int(num1) * int(num2)
        elif "do()" in multiple:
            run = True
        elif "don't()" in multiple:
            run = False
    return result


if __name__ == "__main__":
    # part 1
    input_content = read_input_file("3_input.txt")
    multiples = find_multiples(input_content)
    result = process_multiples(multiples)
    print(result)
    # part 2
    multiples = find_multiples_do_dont(input_content)
    result = process_multiples_do_dont(multiples)
    print(result)
