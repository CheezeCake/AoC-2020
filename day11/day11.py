#!/usr/bin/env python3

import sys
from copy import deepcopy

def round(layout, get_occupied, occupied_threshold):
  new_layout = deepcopy(layout)
  for i in range(len(layout)):
    for j in range(len(layout[i])):
      if layout[i][j] == '.':
        continue
      occupied = get_occupied(layout, i, j)
      if layout[i][j] == 'L' and occupied == 0:
        new_layout[i][j] = '#'
      elif layout[i][j] == '#' and occupied >= occupied_threshold:
        new_layout[i][j] = 'L'
  return new_layout

def within_bounds(layout, i, j):
  return i >= 0 and i < len(layout) and j >= 0 and j < len(layout[i])

DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

def get_occupied_part1(layout, i, j):
  return sum(layout[i + di][j + dj] == '#' for di, dj in DIRECTIONS if within_bounds(layout, i + di, j + dj))

def get_occupied_part2(layout, i, j):
  occupied = 0
  for di, dj in DIRECTIONS:
    ni = i + di
    nj = j + dj
    while within_bounds(layout, ni, nj) and layout[ni][nj] == '.':
      ni += di
      nj += dj
    if within_bounds(layout, ni, nj) and layout[ni][nj] == '#':
      occupied += 1
  return occupied

def round_part1(layout):
  return round(layout, get_occupied_part1, 4)

def round_part2(layout):
  return round(layout, get_occupied_part2, 5)

def serialize(layout):
  return ''.join([''.join(line) for line in layout])

def run(initial_layout, roundf):
  layout = initial_layout
  states = set()
  serialized = serialize(layout)
  while serialized not in states:
    states.add(serialized)
    layout = roundf(layout)
    serialized = serialize(layout)
  return sum(c == '#' for c in serialized)


initial_layout = [list(line.strip()) for line in sys.stdin]
print('part 1:', run(initial_layout, round_part1))
print('part 2:', run(initial_layout, round_part2))
