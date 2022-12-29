if __name__ == '__main__':
# Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    numbers = input().split(' ')
    numbers = [int(x) for x in numbers]

    t = tuple(numbers)

    print(hash(t))
