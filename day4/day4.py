from word_search import WordSearch
import pandas as pd
import numpy as np

def part2(puzzle_input):
    rows = puzzle_input
    m = len(rows)
    n = len(rows[0])

    def check(r, c):
        if rows[r][c] != 'A':
            return False
        ul = rows[r-1][c-1]
        ur = rows[r-1][c+1]
        dl = rows[r+1][c-1]
        dr = rows[r+1][c+1]
        return sorted([ul, ur, dl, dr]) == ['M', 'M', 'S', 'S'] and ul != dr

    return sum(check(r, c) for r in range(1, m-1) for c in range(1, n-1))

def is_valid_intersection(line1, line2):
    # Extract endpoints
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2

    # Find the center points
    center1 = ((x1 + x2) // 2, (y1 + y2) // 2)
    center2 = ((x3 + x4) // 2, (y3 + y4) // 2)

    # Centers must match
    if center1 != center2:
        return False

    # Calculate direction vectors
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3

    # Normalize vectors
    norm1 = (dx1 // abs(dx1 or 1), dy1 // abs(dy1 or 1))
    norm2 = (dx2 // abs(dx2 or 1), dy2 // abs(dy2 or 1))

    # Check for perpendicular or diagonal intersection
    if norm1[0] * norm2[0] + norm1[1] * norm2[1] != 0:
        return False

    # Ensure no overlap or invalid redundancy
    if set(line1) & set(line2):
        return False

    return True


with open('day4/input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

board_df = pd.DataFrame(grid)
board = WordSearch(board_df,"XMAS")

print(f'Day 4 Part 1: {board.find_all("XMAS")}')

# check if perpendicular
board2 = WordSearch(board_df,"MAS")
board2.find_all("MAS")

count = 0
matches = board2.finds

valid_pairs = set()

for line1 in matches:
    for line2 in matches:
        if line1 == line2:
            continue
        if is_valid_intersection(line1, line2):
            valid_pairs.add(tuple(sorted([line1, line2])))

print(f'Day 4 Part 2: {len(valid_pairs)}')

print(f'Day 4 Part 2: {part2(grid)}')