import pandas as pd
import numpy as np

input_data = pd.read_csv("day1/input.txt",delimiter='   ').transform(np.sort)
print(f'Day 1 Part 1: {np.sum(abs(input_data.A - input_data.B))}')
sum = 0
for value in input_data.A: sum += (input_data.B == value).sum()*value
print(f'Day 1 Part 2: {sum}')