#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

def mask_value(value, mask):
  masked = 0
  for i, b in enumerate(reversed(mask)):
    if b == '1':
      masked |= (1 << i)
    elif b == 'X':
      masked |= value & (1 << i)
  return masked

def mask_addr(addr, mask, i=0, final_addr=0):
  if i == len(mask):
    return [final_addr]
  if mask[-i - 1] == '0':
    return mask_addr(addr, mask, i + 1, final_addr | (addr & (1 << i)))
  elif mask[-i - 1] == '1':
    return mask_addr(addr, mask, i + 1, final_addr | (1 << i))
  else:
    return mask_addr(addr, mask, i + 1, final_addr & ~(1 << i)) + mask_addr(addr, mask, i + 1, final_addr | (1 << i))

def run(program, mem, mask_value, mask_addr):
  mask = ''
  for instr in program:
    if instr[0] == 'mask':
      mask = instr[1]
    else:
      addr, value = map(int, instr[1:])
      for masked_addr in mask_addr(addr, mask):
        mem[masked_addr] = mask_value(value, mask)

program = [line.strip().split(' = ') if line.startswith('mask') else re.match('(mem)\[(\d+)\] = (\d+)', line).groups() for line in sys.stdin]

mem = defaultdict(int)
run(program, mem, mask_value, lambda addr, _: [addr])
print('part 1:', sum(mem.values()))

mem = defaultdict(int)
run(program, mem, lambda value, _: value, mask_addr)
print('part 2:', sum(mem.values()))
