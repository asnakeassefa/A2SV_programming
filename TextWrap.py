import textwrap

def wrap(string, max_width):
    ans = ""
    count = 1
    for char in string:
        ans += char
        if count%max_width == 0:
            ans += "\n"
        count += 1
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
