#!/usr/bin/env python3

import sys

def move(next, current_cup, max_cup):
  cups_head = next[current_cup]
  cups_tail = next[next[cups_head]]
  cups_values = {cups_head, next[cups_head], cups_tail}
  next[current_cup] = next[cups_tail]
  destination_cup = current_cup - 1
  if destination_cup < 1:
    destination_cup = max_cup
  while destination_cup in cups_values:
    destination_cup -= 1
    if destination_cup < 1:
      destination_cup = max_cup
  next[cups_tail] = next[destination_cup]
  next[destination_cup] = cups_head
  return next[current_cup]


cups = [int(c) for c in sys.argv[1]]

next = {cups[i]: cups[i + 1] for i in range(len(cups) - 1)}
next[cups[-1]] = cups[0]
current_cup = cups[0]
for _ in range(100):
  current_cup = move(next, current_cup, max(cups))
cup = next[1]
s = ''
while cup != 1:
  s += str(cup)
  cup = next[cup]
print('part 1:', s)

next = {cups[i]: cups[i + 1] for i in range(len(cups) - 1)}
last = cups[-1]
for cup in range(max(cups) + 1, 1000000 + 1):
  next[last] = cup
  last = cup
next[1000000] = cups[0]
current_cup = cups[0]
for _ in range(10000000):
  current_cup = move(next, current_cup, 1000000)
print('part 2:', next[1] * next[next[1]])
