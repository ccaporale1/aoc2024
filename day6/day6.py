import numpy as np
map = []
with open('day6/input.txt', 'r') as file:
    for line in file:
        map.append(list(line.strip()))
map = np.array(map)
map_copy = map.copy()
guard_dirs = ["^","<",">","v"]
guard_pos = np.where(np.isin(map,guard_dirs))
orig_pos = (guard_pos[0],guard_pos[1])


while guard_pos[0] >= 0 and guard_pos[1] >= 0 and guard_pos[0] < len(map[0]) and guard_pos[1] < len(map):

    if map[guard_pos][0] == "^":
        forward = (int(guard_pos[0]-1),int(guard_pos[1]))
        if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
            if map[forward] == "#":
                map[guard_pos] = ">"
            else:
                map[forward] = "^"
                map[guard_pos] = "X"
                guard_pos = forward
        else:
            map[guard_pos] = "X"
            guard_pos = forward
    elif map[guard_pos][0] == ">":
        forward = (int(guard_pos[0]),int(guard_pos[1]+1))
        if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
            if map[forward] == "#":
                map[guard_pos] = "v"
            else:
                map[forward] = ">"
                map[guard_pos] = "X"
                guard_pos = forward
        else:
            map[guard_pos] = "X"
            guard_pos = forward
    elif map[guard_pos][0] == "<":
        forward = (int(guard_pos[0]),int(guard_pos[1]-1))
        if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
            if map[forward] == "#":
                map[guard_pos] = "^"
            else:
                map[forward] = "<"
                map[guard_pos] = "X"
                guard_pos = forward
        else:
            map[guard_pos] = "X"
            guard_pos = forward
    elif map[guard_pos][0] == "v":
        forward = (int(guard_pos[0]+1),int(guard_pos[1]))
        if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
            if map[forward] == "#":
                map[guard_pos] = "<"
            else:
                map[forward] = "v"
                map[guard_pos] = "X"
                guard_pos = forward
        else:
            map[guard_pos] = "X"
            guard_pos = forward
    else:
        print("something's wrong! exiting...")
        break
    

print(f'Day 6 Part 1: {np.count_nonzero(np.where(map == "X",1,0))}')

threshold = 10000
count = 0 
total = 0
for row in range(0,len(map)):
    for col in range(0,len(map[0])):
        map = map_copy.copy()
        count= 0
        if orig_pos != (row,col) and map[row,col] != "#":
            guard_pos = (orig_pos[0],orig_pos[1])
            map[row,col] = "#"
            while guard_pos[0] >= 0 and guard_pos[1] >= 0 and guard_pos[0] < len(map[0]) and guard_pos[1] < len(map):
      
                if map[guard_pos][0] == "^":
                    forward = (int(guard_pos[0]-1),int(guard_pos[1]))
                    if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
                        if map[forward] == "#":
                            map[guard_pos] = ">"
                        else:
                            map[forward] = "^"
                            map[guard_pos] = "X"
                            guard_pos = forward
                    else:
                        map[guard_pos] = "X"
                        guard_pos = forward
                elif map[guard_pos][0] == ">":
                    forward = (int(guard_pos[0]),int(guard_pos[1]+1))
                    if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
                        if map[forward] == "#":
                            map[guard_pos] = "v"
                        else:
                            map[forward] = ">"
                            map[guard_pos] = "X"
                            guard_pos = forward
                    else:
                        map[guard_pos] = "X"
                        guard_pos = forward
                elif map[guard_pos][0] == "<":
                    forward = (int(guard_pos[0]),int(guard_pos[1]-1))
                    if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
                        if map[forward] == "#":
                            map[guard_pos] = "^"
                        else:
                            map[forward] = "<"
                            map[guard_pos] = "X"
                            guard_pos = forward
                    else:
                        map[guard_pos] = "X"
                        guard_pos = forward
                elif map[guard_pos][0] == "v":
                    forward = (int(guard_pos[0]+1),int(guard_pos[1]))
                    if forward[0] >= 0 and forward[0] < len(map[0]) and forward[1] >= 0 and forward[1] < len(map):
                        if map[forward] == "#":
                            map[guard_pos] = "<"
                        else:
                            map[forward] = "v"
                            map[guard_pos] = "X"
                            guard_pos = forward
                    else:
                        map[guard_pos] = "X"
                        guard_pos = forward
                else:
                    print("something's wrong! exiting...")
                    break

                if count > threshold:
                    total +=1
                    break
                else:
                    count += 1


print(f'Day 6 Part 2: {total}')