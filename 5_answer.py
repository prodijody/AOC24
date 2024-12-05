from pathlib import Path


def read_input_file(filename: str) -> tuple[list[str], list[str]]:
    with Path(filename).open() as file:
        lines = file.readlines()  # Read all lines into a list
    rules = [line.strip() for line in lines if "|" in line]
    manuals = [line.strip() for line in lines if "," in line]
    return rules, manuals


def process_rules(rules: list[str]) -> list[list[str, str]]:
    return [rule.split("|") for rule in rules]


def check_manual(manual: list[str], processed_rules: list[list[str, str]]) -> bool:
    for rule in processed_rules:
        if all(s in manual for s in rule):
            # print(f"Rule {rule} found in manual {manual}")
            index_1 = manual.index(rule[0])
            index_2 = manual.index(rule[1])
            # print(f"Indexes: {index_1}, {index_2}")
            if index_1 > index_2:
                return False
    return True


def get_middle_page(manual: list[str]) -> int:
    middle_page = len(manual) // 2
    return int(manual[middle_page])


def fix_manual(manual: list[str], processed_rules: list[list[str, str]]) -> list[str]:
    for rule in processed_rules:
        if all(s in manual for s in rule):
            index_1 = manual.index(rule[0])
            index_2 = manual.index(rule[1])
            if index_1 > index_2:
                print(f"Rule {rule} found in manual {manual}")
                print(f"Indexes: {index_1}, {index_2}")
                manual[index_1], manual[index_2] = manual[index_2], manual[index_1]
                print(f"Manual fixed: {manual}")
    return manual


if __name__ == "__main__":
    rules, manuals = read_input_file("5_test_input.txt")
    processed_rules = process_rules(rules)
    sum_correct = 0
    sum_incorrect = 0
    for manual in manuals:
        if check_manual(manual.split(","), processed_rules):
            sum_correct += get_middle_page(manual.split(","))
        else:
            print(f"Manual {manual} is not valid")
            fixed_manual = fix_manual(manual.split(","), processed_rules)
            sum_incorrect += get_middle_page(fixed_manual)
    print(sum_correct)
    print(sum_incorrect)
