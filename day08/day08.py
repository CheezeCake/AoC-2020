#!/usr/bin/env python3

import sys

def run_program(program):
  acc = 0
  pc = 0
  s = set()
  while pc not in s and pc < len(program):
    s.add(pc)
    instr, arg = program[pc]
    if instr == 'acc':
      acc += arg
      pc += 1
    elif instr == 'jmp':
      pc += arg
    else:
      pc += 1
  return (pc >= len(program), acc)


program = [(instr, int(arg)) for instr, arg in (line.strip().split(' ') for line in sys.stdin)]

print('part 1:', run_program(program)[1])

for i in range(len(program)):
  old = program[i]
  if old[0] == 'jmp':
    program[i] = ('nop', old[1])
  elif old[0] == 'nop':
    program[i] = ('jmp', old[1])
  ok, acc = run_program(program)
  if ok:
    print('part 2:', acc)
    break
  program[i] = old
