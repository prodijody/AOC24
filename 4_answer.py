from pathlib import Path


def read_input_file(filename: str) -> list[tuple[int, ...]]:
    """Read sequences of numbers from file, each line as a tuple."""
    with Path(filename).open() as file:
        return [list(line.strip()) for line in file]


def search_word_horizontal(word: str, grid: list[list[str]]) -> int:
    """Search for a word in a grid horizontally."""
    count = 0
    for row in grid:
        if word in "".join(row):
            count += "".join(row).count(word)
    for row in grid:
        if word in "".join(reversed(row)):
            count += "".join(reversed(row)).count(word)
    return count


def search_word_vertical(word: str, grid: list[list[str]]) -> int:
    """Search for a word in a grid vertically."""
    count = 0
    for col in range(len(grid[0])):
        if word in "".join(row[col] for row in grid):
            count += "".join(row[col] for row in grid).count(word)
    for col in range(len(grid[0])):
        if word in "".join((row[col] for row in grid))[::-1]:
            count += "".join((row[col] for row in grid))[::-1].count(word)
    return count


def search_word_diagonal(word: str, grid: list[list[str]]) -> int:
    """Search for a word in a grid diagonally."""
    count = 0
    for row in range(len(grid[0])):
        for col in range(len(grid)):
            try:
                if word in "".join(grid[row + i][col + i] for i in range(len(word))):
                    count += 1
            except IndexError:
                pass
            try:
                if word in "".join(grid[row + i][col - i] for i in range(len(word))):
                    count += 1
            except IndexError:
                pass
    return count


def search_word_diagonally_up(word: str, grid: list[list[str]]) -> int:
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row - len(word) + 1 >= 0 and col + len(word) <= len(grid[0]):
                if word == "".join(grid[row - i][col + i] for i in range(len(word))):
                    count += 1
            if row - len(word) + 1 >= 0 and col - len(word) + 1 >= 0:
                if word == "".join(grid[row - i][col - i] for i in range(len(word))):
                    count += 1
    return count


if __name__ == "__main__":
    word_search = read_input_file("4_input.txt")
    word = "XMAS"

    count_1 = search_word_horizontal(word, word_search)
    print(count_1)
    count_2 = search_word_vertical(word, word_search)
    print(count_2)
    count_3 = search_word_diagonal(word, word_search)
    print(count_3)
    count_4 = search_word_diagonally_up(word, word_search)
    print(count_4)
    print(count_1 + count_2 + count_3 + count_4)
