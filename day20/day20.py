#!/usr/bin/env python3

import sys
from copy import deepcopy
from collections import defaultdict
from math import sqrt

def rotate(tile):
  n = len(tile)
  for i in range(n // 2):
    for j in range(i, n - i - 1):
      tmp = tile[i][j]
      tile[i][j] = tile[n - j - 1][i]
      tile[n - j - 1][i] = tile[n - i - 1][n - j - 1]
      tile[n - i - 1][n - j - 1] = tile[j][n - i - 1]
      tile[j][n - i - 1] = tmp
  return tile

def flip_x(tile):
  return [row[::-1] for row in tile]

def flip_y(tile):
  return tile[::-1]

def column_matches(t1, col1, t2, col2):
  for i in range(len(t1)):
    if t1[i][col1] != t2[i][col2]:
      return False
  return True

def get_row(tile, row):
  return ''.join(tile[row])

def get_col(tile, col):
  return ''.join(tile[i][col] for i in range(len(tile)))

def get_first_row(tile):
  return get_row(tile, 0)

def get_last_row(tile):
  return get_row(tile, len(tile) - 1)

def get_first_col(tile):
  return get_col(tile, 0)

def get_last_col(tile):
  return get_col(tile, len(tile) - 1)

def arrange(tiles, ids, first_row, first_col, last_row, last_col, square, pos=0, used=set()):
  N = len(square)
  if pos == N * N:
    return True
  row = pos // N
  col = pos % N
  row_match = set(range(len(tiles))) if row == 0 else first_row[get_last_row(tiles[square[row - 1][col]])]
  col_match = set(range(len(tiles))) if col == 0 else first_col[get_last_col(tiles[square[row][col - 1]])]
  match = row_match & col_match
  for i in match:
    id = ids[i]
    if id in used:
      continue
    if row == 0 and any(ids[x] != id for x in last_row[get_first_row(tiles[i])]):
      continue
    if col == 0 and any(ids[x] != id for x in last_col[get_first_col(tiles[i])]):
      continue
    square[row][col] = i
    used.add(id)
    if arrange(tiles, ids, first_row, first_col, last_row, last_col, square, pos + 1, used):
      return True
    used.remove(id)
  return False

def build_image(square, tiles, tile_size):
  image = []
  tile_size -= 2
  for i in range(len(square) * tile_size):
    square_row = i // tile_size
    tile_row = i % tile_size
    image.append(list(''.join(get_row(tiles[t], tile_row + 1)[1:-1] for t in square[square_row])))
  return image

def find_monster_at(image, i, j, sea_monster_offsets):
  coords = {(j + dx, i + dy) for dx, dy in sea_monster_offsets}
  if all(x < len(image[j]) and y < len(image[i]) and image[y][x] == '#' for x, y in coords):
    return coords

def find_monsters(image, sea_monster_offsets):
  monsters = set()
  for i in range(len(image)):
    for j in range(len(image[i])):
      m = find_monster_at(img, i, j, sea_monster_offsets)
      if m:
        monsters |= m
  return monsters

def add_tile(tile, tiles, first_row, first_col, last_row, last_col, ids):
  tiles.append(deepcopy(tile))
  first_row[get_first_row(tiles[-1])].add(len(tiles) - 1)
  last_row[get_last_row(tiles[-1])].add(len(tiles) - 1)
  first_col[get_first_col(tiles[-1])].add(len(tiles) - 1)
  last_col[get_last_col(tiles[-1])].add(len(tiles) - 1)
  ids.append(id)


n = 0
tiles = []
ids = []
first_row = defaultdict(set)
last_row = defaultdict(set)
first_col = defaultdict(set)
last_col = defaultdict(set)
for tile_input in sys.stdin.read().strip().split('\n\n'):
  id = int(tile_input.split('\n')[0].split(' ')[1][:-1])
  tile = [list(row.strip()) for row in tile_input.strip().split('\n')[1:]]
  for _ in range(3):
    add_tile(tile, tiles, first_row, first_col, last_row, last_col, ids)
    add_tile(flip_x(deepcopy(tile)), tiles, first_row, first_col, last_row, last_col, ids)
    add_tile(flip_y(deepcopy(tile)), tiles, first_row, first_col, last_row, last_col, ids)
    tile = rotate(deepcopy(tile))
  n += 1

square_size = int(sqrt(n))
square = [[-1 for _ in range(square_size)] for _ in range(square_size)]
if not arrange(tiles, ids, first_row, first_col, last_row, last_col, square):
  raise 'could not find a working tile arrangement'
print('part 1:', ids[square[0][0]] * ids[square[0][-1]] * ids[square[-1][0]] * ids[square[-1][-1]])

image = build_image(square, tiles, len(tiles[0]))
hash_count = sum(sum(x == '#' for x in row) for row in image)
sea_monster = [
  '                  # ',
  '#    ##    ##    ###',
  ' #  #  #  #  #  #   ',
]
sea_monster_offsets = {(dx, dy) for dy in range(len(sea_monster)) for dx in range(len(sea_monster[dy])) if sea_monster[dy][dx] == '#'}

for _ in range(4):
  img = image
  monsters = find_monsters(image, sea_monster_offsets)
  if monsters:
    print('part 2:', hash_count - len(monsters))
    break
  img = flip_x(deepcopy(image))
  monsters = find_monsters(image, sea_monster_offsets)
  if monsters:
    print('part 2:', hash_count - len(monsters))
    break
  img = flip_y(deepcopy(image))
  monsters = find_monsters(image, sea_monster_offsets)
  if monsters:
    print('part 2:', hash_count - len(monsters))
    break
  image = rotate(deepcopy(image))
