#!/usr/bin/env python3

import sys
from collections import defaultdict

def active_neighbors(grid, cube_coords, neighbor_coords=[]):
  dim = len(neighbor_coords)
  if dim == len(cube_coords):
    return 1 if cube_coords != neighbor_coords and grid[tuple(neighbor_coords)] else 0
  s = 0
  for dc in range(-1, 2):
    neighbor_coords.append(cube_coords[dim] + dc)
    s += active_neighbors(grid, cube_coords, neighbor_coords)
    neighbor_coords.pop()
  return s

def helper(grid, dim_limits, new_grid=defaultdict(bool), c=[]):
  dim = len(c)
  if dim == len(dim_limits):
    n = active_neighbors(grid, c)
    cube = grid[tuple(c)]
    if cube:
      if n != 2 and n != 3:
        cube = False
    else:
      if n == 3:
        cube = True
    if cube:
      new_grid[tuple(c)] = cube
    return
  for x in range(dim_limits[dim][0] - 1, dim_limits[dim][1] + 2):
    c.append(x)
    helper(grid, dim_limits, new_grid, c)
    c.pop()

def cycle(grid, dim):
  dim_limits = []
  for d in range(dim):
    dim_values = [c[d] for c in grid.keys()]
    min_c = min(dim_values, default=0)
    max_c = max(dim_values, default=0)
    dim_limits.append((min_c, max_c))
  new_grid = defaultdict(bool)
  helper(grid, dim_limits, new_grid)
  return new_grid

def run_cycles(grid, dim):
  for _ in range(6):
    grid = cycle(grid, dim)
  return sum(cube for cube in grid.values())


region = [line.strip() for line in sys.stdin]

grid_3d = defaultdict(bool)
grid_4d = defaultdict(bool)
for y in range(len(region)):
  for x in range(len(region[y])):
    if region[y][x] == '#':
      grid_3d[x, y, 0] = True
      grid_4d[x, y, 0, 0] = True

print('part 1:', run_cycles(grid_3d, 3))
print('part 2:', run_cycles(grid_4d, 4))
