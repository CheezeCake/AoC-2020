#!/usr/bin/env python3

import sys

def get_tile(steps):
  directions = {
    'e': (2, 0),
    'se': (1, 1),
    'sw': (-1, 1),
    'w': (-2, 0),
    'nw': (-1, -1),
    'ne': (1, -1),
  }
  x, y = 0, 0
  i = 0
  while i < len(steps):
    if steps[i] in ('s', 'n'):
      dx, dy = directions[steps[i:i + 2]]
      x += dx
      y += dy
      i += 2
    else:
      dx, dy = directions[steps[i]]
      x += dx
      y += dy
      i += 1
  return (x, y)

def flip_tiles(black_tiles):
  directions =  [(2,  0), (1, -1), (-1, -1), (-2,  0), (-1, 1), (1, 1)]
  new_black_tiles = set()
  white_tiles = set()
  for x, y in black_tiles:
    adj_tiles = {(x + dx, y + dy) for dx, dy in directions}
    adj_black_tiles = adj_tiles & black_tiles
    white_tiles |= adj_tiles - black_tiles
    if 0 < len(adj_black_tiles) < 3:
      new_black_tiles.add((x, y))
  for x, y in white_tiles:
    adj_black_tiles_cnt = sum((x + dx, y + dy) in black_tiles for dx, dy in directions)
    if adj_black_tiles_cnt == 2:
      new_black_tiles.add((x, y))
  return new_black_tiles


black_tiles = set()
for line in sys.stdin:
  p = get_tile(line.strip())
  if p in black_tiles:
    black_tiles.remove(p)
  else:
    black_tiles.add(p)
print('part 1:', len(black_tiles))

for _ in range(100):
  black_tiles = flip_tiles(black_tiles)
print('part 2:', len(black_tiles))
