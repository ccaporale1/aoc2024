import pandas as pd
import numpy as np

inputdata = pd.read_csv('day2/input.txt',delimiter=' ',header=None)
diff = np.diff(inputdata)
safe_p1 = 0
safe_p2 = 0
for row in inputdata.values:

    row_diff = np.diff(row)
    row_diff = row_diff[~np.isnan(row_diff)]
 
    row_check_pos = row_diff[~((row_diff>= 1.0) & (row_diff <= 3.0))]
    row_check_neg = row_diff[~((row_diff <= -1.0) & (row_diff >= -3.0))]
    if len(row_check_pos) == 0:
        safe_p1 += 1

    elif len(row_check_neg) == 0:
        safe_p1 += 1

    else: 
        for i in range(len(row)):
            row_test = np.delete(row,i)
            row_test = np.diff(row_test)
            row_test = row_test[~np.isnan(row_test)]
            row_check_pos = row_test[~((row_test >= 1.0) & (row_test <= 3.0))]
            row_check_neg = row_test[~((row_test <= -1.0) & (row_test >= -3.0))]
            if len(row_check_pos) == 0:
                safe_p2 += 1
                break
            elif len(row_check_neg) == 0:
                safe_p2 += 1
                break

print(f'Day 2 Part 1: {safe_p1}') 
print(f'Day 2 Part 2: {safe_p2+safe_p1}') 