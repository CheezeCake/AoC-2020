#!/usr/bin/env python3

import sys

lines = [line for line in sys.stdin]
valid1 = 0
valid2 = 0
for line in lines:
  parts = line.split(' ')
  assert len(parts) == 3
  x, y = map(int, parts[0].split('-'))
  letter = parts[1][0]
  password = parts[2]
  cnt = password.count(letter)
  if cnt >= x and cnt <= y:
    valid1 += 1
  if (password[x - 1] == letter and password[y - 1] != letter) or (password[x - 1] != letter and password[y - 1] == letter):
    valid2 += 1

print('part 1:', valid1)
print('part 2:', valid2)
