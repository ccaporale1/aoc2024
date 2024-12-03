import re
import pandas as pd 
import numpy as np

with open('day3/input.txt',"r") as file:
    content = file.read()

pattern = r'mul\(\d+,\d+\)'
sum = 0
matches = re.findall(pattern,content)
for match in matches:
    nums = np.array(re.findall(r'\d+',match)).astype(int)

    sum += np.prod(nums)
print(f'Day 3 Part 1: {sum}')

# Regex patterns for instructions
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

# Extract instructions in order of appearance
instructions = re.findall(pattern, content)

# Initial state: mul instructions are enabled
enabled = True
sum = 0

# Process each instruction
for instruction in instructions:
    if instruction == "don't()":  # Disable future mul instructions
        enabled = False
    elif instruction == "do()":  # Enable future mul instructions
        enabled = True
    elif instruction.startswith("mul(") and enabled:  # Process mul() if enabled
        # Extract numbers from the mul(a, b) instruction
        nums = np.array(re.findall(r"\d+", instruction)).astype(int)
        sum += np.prod(nums)
print(f'Day 3 Part 2: {sum}')