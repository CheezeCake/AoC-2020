#!/usr/bin/env python3

import sys

seat_ids = [int(bp.strip().translate(str.maketrans('FBLR', '0101')), 2) for bp in sys.stdin]

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
