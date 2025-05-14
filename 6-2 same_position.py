def same_position():
    n = int(input())
    s = list(input())
    position = [0, 0]
    temp_position = []
    for i in s:
        temp_position.append([position[0],position[1]])
        if i == 'R':
            position[0] += 1
        elif i == 'L':
            position[0] -= 1
        elif i == 'U':
            position[1] += 1
        else:
            position[1] -= 1
        if position in temp_position:
            return print('Yes')
    return print('No')

same_position()