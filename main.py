VALUE_MAP = {
    'A': 1,
    'B': 5,
    'Z': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'R': 1000,
}


def solve(input_string: str) -> tuple[int, list[str]]:
    stack = [(input_string[0], VALUE_MAP[input_string[0]], input_string[0])]
    for current in input_string[1:]:
        current_value = VALUE_MAP[current]
        top, top_value, top_root = stack[-1]
        if current == top_root:
            stack.pop()
            stack.append((f"{top}{current}", top_value + current_value, top_root))
        elif current_value < top_value:
            stack.append((current, current_value, current))
        else:
            stack.pop()
            stack.append((f"{top}{current}", current_value - top_value, top_root))
    output_value = sum(value for _, value, _ in stack)
    explaination_list = [f"{item} = {value}" for item, value, _ in stack]
    return output_value, explaination_list


def main():
    input_list = ["AAA", "LBAAA", "RCRZCAB"]
    for i, input_string in enumerate(input_list):
        output_value, explaination_list = solve(input_string)
        print(f"Example {i + 1}:")
        print(f"Input: s = \"{input_string}\"")
        print(f"Output: {output_value}")
        print(f"Explanation: {', '.join(explaination_list)}")


if __name__ == "__main__":
    main()
