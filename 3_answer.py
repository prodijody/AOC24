import re


def use_regex(input_text):
    pattern = re.compile(
        r"mul\([0-9]+,[0-9]+\)",
        re.IGNORECASE,
    )
    return pattern.match(input_text)


print(
    use_regex("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
)
