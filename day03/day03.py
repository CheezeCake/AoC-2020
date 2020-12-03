#!/usr/bin/env python3

import sys

def trees_on_slope(grid, right, down):
  x, y = right, down
  trees = 0
  while y < len(grid):
    if grid[y][x % len(grid[0])] == '#':
      trees += 1
    x += right
    y += down
  return trees

grid = [list(line.strip()) for line in sys.stdin]
n = trees_on_slope(grid, 3, 1)

print('part 1:', n)
print('part 2:', trees_on_slope(grid, 1, 1) * n * trees_on_slope(grid, 5, 1) * trees_on_slope(grid, 7, 1) * trees_on_slope(grid, 1, 2))
