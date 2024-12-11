import numpy as np

input = []
with open('day10/input.txt', 'r') as file:
    for line in file:
        input.append(list(line.rstrip()))
map = np.array(input.copy())

def find_reachable_goals(map, start, goal_value):
    rows, cols = len(map), len(map[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [tuple(start)]
    visited = set()
    reachable_goals = set()

    while stack:
        current = stack.pop()
        visited.add(current)

        current_row, current_col = current

        for move in moves:
            next_row = current_row + move[0]
            next_col = current_col + move[1]

            # Check bounds
            if 0 <= next_row < rows and 0 <= next_col < cols:
                next_pos = (next_row, next_col)
                if next_pos not in visited:
                    value_diff = int(map[next_row][next_col]) - int(map[current_row][current_col])
                    if value_diff == 1:  # Valid move
                        if int(map[next_row][next_col]) == goal_value:
                            reachable_goals.add(next_pos)
                        else:
                            stack.append(next_pos)

    return reachable_goals


startx, starty = np.where(map == '0')
starts = np.array(list(zip(startx, starty)))
goal_value = 9
total_score = 0

for start in starts:
    reachable_goals = find_reachable_goals(map, start, goal_value)
    total_score += len(reachable_goals)

print(f'Day 10 Part 1: {total_score}')

# DFS
def count_paths(map, current, visited, path_count):
    rows, cols = len(map), len(map[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    current_row, current_col = current

    for move in moves:
        next_row = current_row + move[0]
        next_col = current_col + move[1]

        if 0 <= next_row < rows and 0 <= next_col < cols:
            next_pos = (next_row, next_col)
            current_height = int(map[current_row][current_col])
            next_height = int(map[next_row][next_col])
            if next_pos not in visited and next_height == current_height + 1:
                if next_height == 9:  
                    path_count[0] += 1
                else:
    
                    visited.add(next_pos)
                    count_paths(map, next_pos, visited, path_count)
                    visited.remove(next_pos) 
def trailhead_rating(map):
    startx, starty = np.where(map == '0')
    starts = list(zip(startx, starty))
    total_rating = 0

    for start in starts:
        visited = set()
        visited.add(start)
        path_count = [0]  
        count_paths(map, start, visited, path_count)
        total_rating += path_count[0]

    return total_rating

rating = trailhead_rating(map)

print(f'Day 10 Part2: {rating}')
