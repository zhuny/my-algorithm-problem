def solution_test_set1(string: str):
    stack = []
    pair = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }
    stream = []
    prev_pop = False
    for char in string:
        if char in pair:
            stack.append(pair[char])
            stream.append(char)
            prev_pop = False
        elif len(stack) == 0 or stack[-1] != char:
            return ""
        else:
            if not prev_pop:
                stream.append(str(len(stack)))
            stream.append(stack.pop())
            prev_pop = True

    if len(stack) == 0:
        return "".join(stream)
    else:
        return ""


if __name__ == '__main__':
    print(solution_test_set1("({[]})()[[]]"))
    print(solution_test_set1("({[]})()[[]"))
    print(solution_test_set1("({[]})(]"))
