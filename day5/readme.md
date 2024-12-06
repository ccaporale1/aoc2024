# Day 5


## Part 1

First, read in the input and sorting it into rule sets and update lists of page numbers.

Then, iterate through the update lists and check if any rules are violated.

This can be done by checking if the two numbers in the rule set both exist in the update lists.

If both exist, check that the index of the first rule # is less than the index of the second rule number. 

If it is less, then add the value of the middle index to the sum value.

## Part 2

The same prep as Part 1, but instead of checking lists already in the correct order, only use the list in incorrect order after sorting them.

Iterate through each update lists and check if any rules are violated.

If none are, do not use that list.

If a rule is violated, correct that rule. Repeat this until no rules are violated.

Then add the value of the middle index to the sum value.