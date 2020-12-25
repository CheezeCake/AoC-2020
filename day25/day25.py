#!/usr/bin/env python3

import sys

def transform(subject, value):
  return (value * subject) % 20201227

def find_loop_size(pubkey):
  loop_size = 0
  value = 1
  while value != pubkey:
    value = transform(7, value)
    loop_size += 1
  return loop_size

card_pubkey, door_pubkey = (int(pubkey) for pubkey in sys.stdin)

card_loop_size = find_loop_size(card_pubkey)
door_loop_size = find_loop_size(door_pubkey)

x = 1
for _ in range(card_loop_size):
  x = transform(door_pubkey, x)
y = 1
for _ in range(door_loop_size):
  y = transform(card_pubkey, y)
assert x == y
print('part 1:', x)
