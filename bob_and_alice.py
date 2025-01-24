pos = 1 #1 - leftmost, 2 - middle, 3 - rightmost

movement = input("")

for move in movement:
    if move == 'A': #for movement of leftmost to middle and vice versa
        if pos == 1:
            pos = 2
        elif pos == 2:
            pos =1
    elif move == 'B': #for movement of middle to rightmost and vice versa
        if pos == 2:
            pos = 3
        elif pos == 3:
            pos = 2
    elif move == 'C': #for movement of leftmost to rightmost and vice versa
        if pos == 1:
            pos = 3
        elif pos == 3:
            pos = 1
            

print(pos)
