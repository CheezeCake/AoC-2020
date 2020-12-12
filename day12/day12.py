#!/usr/bin/env python3

import sys
import math

instructions = [(line[0], int(line[1:])) for line in sys.stdin]

x, y = 0, 0
ang = 0

for action, value in instructions:
  if action == 'N':
    y += value
  elif action == 'S':
    y -= value
  elif action == 'E':
    x += value
  elif action == 'W':
    x -= value
  elif action == 'L':
    ang = (ang + value) % 360
  elif action == 'R':
    ang = (ang - value) % 360
  elif action == 'F':
    x += math.cos(ang * math.pi / 180) * value
    y += math.sin(ang * math.pi / 180) * value
  else:
    raise 'invalid action'
print('part 1:', round(abs(x) + abs(y)))

x, y = 0, 0
wx, wy = 10, 1

for action, value in instructions:
  if action == 'N':
    wy += value
  elif action == 'S':
    wy -= value
  elif action == 'E':
    wx += value
  elif action == 'W':
    wx -= value
  elif action == 'L':
    ang = value % 360
    c = math.cos(ang * math.pi / 180)
    s = math.sin(ang * math.pi / 180)
    nx = wx * c - wy * s
    ny = wx * s + wy * c
    wx = nx
    wy = ny
  elif action == 'R':
    ang = -value % 360
    c = math.cos(ang * math.pi / 180)
    s = math.sin(ang * math.pi / 180)
    nx = wx * c - wy * s
    ny = wx * s + wy * c
    wx = nx
    wy = ny
  elif action == 'F':
    x += wx * value
    y += wy * value
  else:
    raise 'invalid action'
print('part 2:', round(abs(x) + abs(y)))
