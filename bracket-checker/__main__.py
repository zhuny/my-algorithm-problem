def solution(string: str):
    stack = []
    pair = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>',
        '"': '"',
        "'": "'"
    }
    stream = []
    prev_pop = False
    for char in string:
        if stack and stack[-1] == char:
            if not prev_pop:
                stream.append(str(len(stack)))
            stack.pop()
            stream.append(char)
            prev_pop = True
        elif char in pair:
            stream.append(char)
            stack.append(pair[char])
            prev_pop = False
        else:
            return ""

    if len(stack) == 0:
        return "".join(stream)
    else:
        return ""


if __name__ == '__main__':
    print(solution("({[]})()[[]]"))
    print(solution("({[]})()[[]"))
    print(solution("({[]})(]"))
    print(solution("'([]({{}})'')'"))
