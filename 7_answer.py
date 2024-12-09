from pathlib import Path
import itertools

values = ["+", "*"]


def read_input_file(filename: str) -> list[tuple[int, list[int]]]:
    equations = []
    with Path(filename).open() as file:
        for line in file:
            test_value, nums = line.split(":")
            nums = [int(x) for x in nums.split()]
            equations.append((int(test_value), nums))
    return equations


if __name__ == "__main__":
    equations = read_input_file("7_input.txt")
    # print(equations)
    total_sum = 0
    for equation in equations:
        # print("----------------------------")
        # print(f"--------{equation[0]}-----------")
        nums = equation[1]
        operators = list(itertools.product(["+", "*", "||"], repeat=len(nums) - 1))
        for op_set in operators:
            # print(nums, op_set)
            num_sum = 0
            if op_set[0] == "+":
                num_sum += nums[0] + nums[1]
            if op_set[0] == "*":
                num_sum += nums[0] * nums[1]
            if op_set[0] == "||":
                num_sum += int(str(nums[0]) + str(nums[1]))
            # print(f"starting num_sum: {num_sum}")
            for i in range(1, len(op_set)):
                if op_set[i] == "+":
                    # print(f"adding {num_sum} + {nums[i + 1]}")
                    num_sum = num_sum + nums[i + 1]
                if op_set[i] == "*":
                    # print(f"multiplying {num_sum} * {nums[i + 1]}")
                    num_sum = num_sum * nums[i + 1]
                if op_set[i] == "||":
                    # print(f"adding  {int(str(num_sum) + str(nums[i+1]))}")
                    num_sum = int(str(num_sum) + str(nums[i + 1]))
            # print(f"{equation[0]} - {num_sum}")
            if num_sum == equation[0]:

                total_sum += num_sum
                break
    print(total_sum)
