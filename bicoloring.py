
while True:
    vertices = int(input())
    if vertices == 0:
        break
    edges = int(input())
    color = [0] * (vertices+1)
    ans = True 
    for _ in range(edges):
        e1,e2 = map(int,input().split())
        if color[e1] and color[e2] and color[e1] == color[e2]:
            ans = False
        elif not color[e1] and not color[e2]:
            color[e1] = 1
            color[e2] = 2
        else:
            if color[e1] and color[e2]:
                continue
            else:
                if color[e1]:
                    if color[e1] == 1:
                        color[e2] = 2
                    elif color[e1] == 2:
                        color[e2] = 1
                if color[e2]:
                    if color[e2] == 1:
                        color[e1] = 2
                    elif color[e2] == 2:
                        color[e1] = 1

    if ans:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")