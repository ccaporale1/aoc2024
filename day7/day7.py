import numpy as np

def part1(expression,index=1,sum=0):
    if index > len(expression)-1:
        return sum
    
    mul_sum = sum * int(expression[index] )
    add_sum = sum + int(expression[index] )
    sum1 = part1(expression,index=index+1,sum=mul_sum)
    sum2 = part1(expression,index=index+1,sum=add_sum)

    if sum1 == int(expression[0]):
        sum = sum1
    elif sum2 == int(expression[0]):
        sum = sum2

    return sum

def part2(expression, index=1, sum=0):
    if index > len(expression) - 1:
        return sum

    current_value = int(expression[index])

    add_sum = sum + current_value
    mul_sum = sum * current_value
    concat_sum = int(str(sum) + str(current_value))  

    sum1 = part2(expression, index=index + 1, sum=add_sum)
    sum2 = part2(expression, index=index + 1, sum=mul_sum)
    sum3 = part2(expression, index=index + 1, sum=concat_sum)

    if sum1 == int(expression[0]):
        return sum1
    elif sum2 == int(expression[0]):
        return sum2
    elif sum3 == int(expression[0]):
        return sum3

    return 0


input = []
with open('day7/input.txt', 'r') as file:
    for line in file:
        input.append(list(line.rstrip().replace(":","").split(" ")))
total = 0
for equation in input:
    #equation = np.array(equation,dtype=float)
    total += part1(equation,index=1,sum=0)

print(f'Day 7 Part 1: {int(total)}')

total = 0
for equation in input:
    #equation = np.array(equation,dtype=float)
    total += part2(equation,index=1,sum=0)

print(f'Day 7 Part 2: {int(total)}')
