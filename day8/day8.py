import numpy as np

input = []
with open('day8/input.txt', 'r') as file:
    for line in file:
        input.append(list(line.rstrip()))
input = np.array(input)
antennas = np.delete(np.unique(input),np.where(np.unique(input) == "."))

map = input.copy()
track_count = 0

antinode_set = set()
for antenna in antennas:
    row_idxs,col_idxs = np.where(map == antenna)
    for i in range(0,len(row_idxs)):
        row_diff = np.delete(row_idxs,i) - row_idxs[i]

        col_diff = np.delete(col_idxs,i) - col_idxs[i]

        for j in range(0,len(row_diff)):
            new_row = row_idxs[i] - row_diff[j]
            new_col = col_idxs[i] - col_diff[j]
            if new_row >= 0 and new_row < len(map) and new_col >= 0 and new_col < len(map[0]):
                new_ant = (new_row,new_col)
                if new_ant not in antinode_set and map[new_ant] != antenna: 
                    antinode_set.add(new_ant)
                    track_count += 1
                if map[new_ant] == ".":
                    map[new_ant] = "#"
            new_row = row_idxs[i] + 2*row_diff[j]
            new_col = col_idxs[i] + 2*col_diff[j]
            if new_row > 0 and new_row < len(map) and new_col > 0 and new_col < len(map[0]):
                new_ant = (new_row,new_col)
                if new_ant not in antinode_set and map[new_ant] != antenna: 
                    antinode_set.add(new_ant)
                    track_count += 1
                if map[new_ant] == ".":
                    map[new_ant] = "#"
label,counts = np.unique(map,return_counts=True)

antinode_idxs = np.where(label == "#")

print(f'Day 8 Part 1 counting uniques: {counts[antinode_idxs][0]}')
print(f'Day 8 Part 1 counting as go: {track_count}')


map = input.copy()
track_count = 0

antinode_set = set()
for antenna in antennas:
    row_idxs,col_idxs = np.where(map == antenna)
    for i in range(0,len(row_idxs)):
        row_diff = np.delete(row_idxs,i) - row_idxs[i]

        col_diff = np.delete(col_idxs,i) - col_idxs[i]

        for j in range(0,len(row_diff)):
            for k in range(0,len(map)):
                new_row = row_idxs[i] - k*row_diff[j]
                new_col = col_idxs[i] - k*col_diff[j]
                if new_row >= 0 and new_row < len(map) and new_col >= 0 and new_col < len(map[0]):
                    new_ant = (new_row,new_col)
                    if new_ant not in antinode_set: 
                        antinode_set.add(new_ant)
                        track_count += 1
                    if map[new_ant] == ".":
                        map[new_ant] = "#"
                new_row = row_idxs[i] + (k)*row_diff[j]
                new_col = col_idxs[i] + (k)*col_diff[j]
                if new_row >= 0 and new_row < len(map) and new_col >= 0 and new_col < len(map[0]):
                    new_ant = (new_row,new_col)
                    if new_ant not in antinode_set: 
                        antinode_set.add(new_ant)
                        track_count += 1
                    if map[new_ant] == ".":
                        map[new_ant] = "#"
label,counts = np.unique(map,return_counts=True)

antinode_idxs = np.where(label == "#")

print(f'Day 8 Part 2 counting as go: {track_count}')
