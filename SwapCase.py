def swap_case(s):
    ans = "" 
    for i in s:
        if ord(i) >= ord('a') <= ord('z'):
            ans += (chr(ord('A')+(ord(i)-ord('a'))))
        elif ord(i) >= ord('A') <= ord('Z'):
            ans += (chr(ord('a')+(ord(i)-ord('A'))))
        else:
            ans += i
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
