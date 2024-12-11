import numpy as np

input = []
with open('day9/input.txt', 'r') as file:
    for line in file:
        input=list(line.rstrip())

memory = []
id_hold = 0

# make memory string
for bit in range(1,len(input)+1):
    if bit % 2 == 0: # even
        for i in range(0,int(input[bit-1])):
            memory.append(".")
    else: # odd
        for i in range(0,int(input[bit-1])):
            memory.append(str(id_hold))
        id_hold += 1
memory = np.array(memory)
p2_memory = memory.copy()
last_bit = -1
for i in range(0,len(memory)):
    if memory[last_bit] != ".":
        temp = memory[last_bit] 
        memory = np.delete(memory, last_bit)
        free_indxs = np.where(memory == ".")
        memory[free_indxs[0][0]] = temp
        memory = np.append(memory,".")
    else:
        last_bit -= 1

checksum = 0
for i in range(0,len(memory)):
    if memory[i] != ".":
        checksum += i * int(memory[i])

print(f'Day 9 Part 1: {checksum}')

def free_space(array):
    is_dot = array == '.'

    dot_changes = np.diff(is_dot.astype(int))

    starts = np.where(dot_changes == 1)[0] + 1  
    ends = np.where(dot_changes == -1)[0]       

    if is_dot[0]:  # Starts with a group
        starts = np.insert(starts, 0, 0)
    if is_dot[-1]:  # Ends with a group
        ends = np.append(ends, len(array) - 1)

    return list(zip(starts, ends))

last_bit = -1
files_checked = set()
for i in range(0,len(p2_memory)):
    if p2_memory[last_bit] != ".":
        
        temp = p2_memory[last_bit]
        if temp not in files_checked:
            files_checked.add(temp)
            #print(f'value: {temp}')
            idxs = np.where(p2_memory == temp)
            idxs = idxs[0]
            last_bit = idxs[0] 
            free_indxs = free_space(p2_memory)
            #print(f'file space: {idxs}')
            for free_slots in free_indxs:
                #print(f'free bits: {free_slots}')
                if (free_slots[1] - free_slots[0]+1) >= len(idxs) and free_slots[0] < idxs[0]:
                    #print(f'free bits size is {free_slots[1] - free_slots[0]+1} and size needed is {len(idxs)}')
                    for j in range(0,len(idxs)):
                        p2_memory[free_slots[0]+j] = temp
                    p2_memory[idxs] = "."
                    break
            #print(p2_memory)
    last_bit -= 1 

checksum = 0
for i in range(0,len(p2_memory)):
    if p2_memory[i] != ".":
        checksum += i * int(p2_memory[i])

print(f'Day 9 Part 2: {checksum}')