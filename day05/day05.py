#!/usr/bin/env python3

import sys

def decode(s, hi, lc):
  lo = 0
  for c in s:
    mid = (lo + hi) // 2
    if c == lc:
      hi = mid - 1
    else:
      lo = mid + 1
  return lo

def decode_row(bp):
  return decode(bp[:7], 127, 'F')

def decode_column(bp):
  return decode(bp[-3:], 7, 'L')


seat_ids = [decode_row(bp.strip()) * 8 + decode_column(bp.strip()) for bp in sys.stdin]

max_seat_id = max(seat_ids)
print('part 1:', max_seat_id)

for n in seat_ids:
  n = abs(n)
  if n < len(seat_ids) and seat_ids[n] >= 0:
    seat_ids[n] = -seat_ids[n]
for i in range(8, len(seat_ids)):
  if seat_ids[i] > 0:
    print('part 2:', i)
    sys.exit()
