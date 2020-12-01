#!/usr/bin/env python3

import sys

def three_sum(entries):
  entries.sort()
  for i in range(len(entries) - 2):
    a = entries[i]
    start = i + 1
    end = len(entries) - 1
    while start < end:
      s = a + entries[start] + entries[end]
      if s == 2020:
        return a * entries[start] * entries[end]
      elif s > 2020:
        end -= 1
      else:
        start += 1

def two_sum(entries):
  s = set()
  for e in entries:
    if e in s:
      return e * (2020 - e)
    s.add(2020 - e)

entries = [int(x) for x in sys.stdin]
print('part 1:', two_sum(entries))
print('part 2:', three_sum(entries))
