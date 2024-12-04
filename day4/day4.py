from word_search import WordSearch
import pandas as pd

with open('day4/input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

# Convert the list of lists into a pandas DataFrame
board_df = pd.DataFrame(grid)
board = WordSearch(board_df,"XMAS")

print(f'Day 4 Part 1: {board.find_all("XMAS")}')

