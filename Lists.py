if __name__ == '__main__':
    N = int(input())
    array = []
    for i in range(N):
        command = input().split(' ')
        if command[0] == 'append':
            array.append(int(command[1]))
        elif command[0] == 'print':
            print(array)
        elif command[0] == 'remove':
            array.remove(int(command[1]))
        elif command[0] == 'sort':
            array.sort()
        elif command[0] == 'pop':
            array.pop()
        elif command[0] == 'insert':
            array.insert(int(command[1]),int(command[2]))
        elif command[0] == 'reverse':
            array.reverse()
