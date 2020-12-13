#!/usr/bin/env python3

import sys

min_ts = int(sys.stdin.readline())
buses = [(i, int(id)) for i, id in enumerate(sys.stdin.readline().strip().split(',')) if id != 'x']

ts = min_ts
done = False
while not done:
  for _, id in buses:
    if id != 'x' and ts % int(id) == 0:
      print('part 1:', (ts - min_ts) * int(id))
      done = True
  ts += 1

min_ts = 1
step = 1
for i, id in buses:
  while (min_ts + i) % id != 0:
    min_ts += step
  step *= id
print('part 2:', min_ts)
