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
    output_value = 0
    explaination_list = []
    stack = []
    for current in input_string:
        if len(stack) > 0:
            top = stack[-1]
            current_value = VALUE_MAP[current]
            top_value = VALUE_MAP[top]
            if current_value <= top_value:
                stack.append(current)
            else:
                output_value += current_value - top_value
                explaination_list.append(f"{top}{current} = {current_value - top_value}")
                stack.pop()
        else:
            stack.append(current)
    if len(stack) > 0:
        count_map = {k: 0 for k in VALUE_MAP.keys()}
        for item in stack:
            count_map[item] += 1
        for key in count_map:
            if count_map[key] > 0:
                output_value += count_map[key] * VALUE_MAP[key]
                output_key = "".join([key for _ in range(count_map[key])])
                explaination_list.insert(0, f"{output_key} = {count_map[key] * VALUE_MAP[key]}")
    return output_value, explaination_list


def main():
    input_list = ["AAA", "LBAAA", "RCRZCAB"]
    for i, input_string in enumerate(input_list):
        output_value, explaination_list = solve(input_string)
        print(f"Example: {i + 1}")
        print(f"Input: s = \"{input_string}\"")
        print(f"Output: {output_value}")
        print(f"Explanation: {', '.join(explaination_list)}")


if __name__ == "__main__":
    main()
