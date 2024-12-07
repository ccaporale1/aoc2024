# Day 6

**Problem:**
There is a guard patrolling and the goal is to predict the movement of the guard based on a set of rules:

- [ ] If there is something directly in front of you, turn right 90 degrees.

- [ ] Otherwise, take a step forward.

Give a n x m map where "." is traversible spot, "#" is an obstacle, and "X" is a spot already visited.

The direction the guard is facing is determined by "^" (up), ">" (right), "<" (left), and "v" (down).

## Part 1

**Goal:** Determine the number of distinct traversible spots the guard will use before leaving the n x m mapped area.

Using a brute force method, iterate through this process:

- [ ] Check base case of if guard position is not in n x m map, exit and count the number of "X" elements in the n x m array.
- [ ] Check the direction the guard is facing and get the value of the spot "in front" of the guard
  - [ ] If the spot is not "#", move "forward"
  - [ ] If the spot is "#" rotate the guard 90deg to the right:
    - [ ] "^" -> ">"
    - [ ] ">" -> "v"
    - [ ] "v" -> "<"
    - [ ] "<" -> "^"

## Part 2

**Goal:** Determine the number of distinct spots a single new obstacle can be placed that sends the guard into an infinite loop.

Using a brute force method, iterate this process:

- [ ] For each row & column, if that location is not the guard's starting position or an existing obstacle, place an obstacle "#"
  - [ ] run the movement steps used in part 1
  - [ ] track the number of steps being taken, if the number of steps reach a high threshold, assume that the guard is in an infinite loop, +1 to the count, and restart the process 