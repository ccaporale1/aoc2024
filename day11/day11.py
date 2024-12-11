import numpy as n1p

input = []
with open('day11/input.txt', 'r') as file:
    for line in file:
        input=list(line.rstrip().split(" "))
p2=input.copy()
blinks = 25
for i in range(0,blinks):
    j = 0
    while j < len(input):
        if input[j] == "0":
            input[j] = "1"
        elif len(input[j]) % 2 == 0:
            midpoint = len(input[j]) // 2
            first_half = int(input[j][:midpoint])
            second_half = int(input[j][midpoint:])
            del input[j]
            input.insert(j,str(first_half))
            input.insert(j+1,str(second_half))
            j += 1
        else:
            input[j] = str(int(input[j]) * 2024)
        j += 1

print(f'Day 11 Part 1: {len(input)}')

from collections import Counter

def blinking(rock):
    if rock == "0":
        return ["1"]
    elif len(rock) % 2 == 0:
        midpoint = len(rock) // 2
        first_half = str(int(rock[:midpoint]))
        second_half = str(int(rock[midpoint:]))
        return [first_half, second_half]
    else:
        return [str(int(rock) * 2024)]

blinks = 75
counts = Counter(p2)
for _ in range(blinks):
    new_counts = Counter()

    for rock, count in counts.items():
        transformed = blinking(rock)
        for item in transformed:
            new_counts[item] += count  
 
    counts = new_counts

total_count = sum(counts.values())

print(f'Day 11 Part 2: {total_count}')