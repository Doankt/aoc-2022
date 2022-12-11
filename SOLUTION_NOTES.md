# Solution Notes

## Day 1

Easy warmup problem just keeping a counter.

## Day 2

Makes use of % 3 for a rotating selection system.

## Day 3

Easy when I realized this problem is just set intersections.

Learned after that intersections between sets can be done with ```A & B```

## Day 4

Could also just check end numbers if they are contained in a set insted of actually creating the sets.

## Day 5

Parsing was a bit of a pain. Each char group is 4 char wide and I made use of that for parsing the stacks.

Could also have done move parsing without re. Though this solution does the same.

## Day 6

Much easier than the prevous day.
Make use of a sliding window.

## Day 7

My solution makes use of actually creating nested dicts. Though my first idea was how I actually wanted to implement this.

At first I wanted to have a dict where:

- Key: Dir name
- Value: Sum of files in dir

This should work, but instead what I missed was the dict should've been

- Key: **FULL** dir name
- Value: Sum of files in dir

I swapped to creating the actual dirs due to finding dirs in the input having the same name.

## Day 8

Checks all directions for all points starting from the point and moving outwards.

For visibility, I wanted to reduce the amount of checks by first starting with the direction where the tree was closest to the edge.

e.g. for the following forest

```text
000X0
00000
00000
00000
00000
```

X would check the directions in the following order and stop of any direction returns True: ```[UP, RIGHT, LEFT, DOWN]```

## Day 9

Finding the distance between a diagonal was very useful for today. Knowing when the distance between two points is above ```sqrt(2)``` is the easiest check for me to work with.

Today took a bit longer as I assumed some incorrect moves for when the tail has to follow. After re-reading the problem, I fixed the movement to the problem specification.

Also restructed the Solution class after to be generalized for any number of tail counts.

## Day 10

The worst thing I spent most time today was a silly mistake on my part.

It was a hard to spot issue, but for cycle checking for part 2 output I had ```(self.cycle-1 % 40)```. Due to python order of operations, the correct check should be ```((self.cycle-1) % 40)```

## Day 11

Today, I wondered if it was worth having a real Solver class implemented instead of making one for each day. The past few days have had Solver classes so a base one might be of use.

For parsing, I had initially thought about using regex, but remembered to day 5 where parsing could've been done faster if I had thought less. The method employed assumes that tests are always "divisible by x"

LCM would probably work better instead of multiplying all the mod values together, but it seemed it was small enough for 7 values.

## Day 12

## Day 13

## Day 14

## Day 15

## Day 16

## Day 17

## Day 18

## Day 19

## Day 20

## Day 21

## Day 22

## Day 23

## Day 24

## Day 25
