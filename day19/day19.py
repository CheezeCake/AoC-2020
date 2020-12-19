#!/usr/bin/env python3

import sys
import re

def to_regex(rules, n, mem={}):
  if n in mem:
    return mem[n]
  if type(rules[n]) is str:
    mem[n] = rules[n]
    return mem[n]
  mem[n] = '(' + '|'.join('(' + (''.join(to_regex(rules, r, mem) for r in subrule) + ')') for subrule in rules[n]) + ')'
  return mem[n]


rules_input, messages = sys.stdin.read().split('\n\n')

rules = {}
for line in rules_input.split('\n'):
  n, match = line.strip().split(': ')
  n = int(n)
  m = re.match('"(.*)"', match)
  if m:
    rules[n] = m.group(1)
  elif re.match('^(\d+ )*\d+$', match):
    rules[n] = [[int(x) for x in match.split(' ')]]
  else:
    rules[n] = [[int(x) for x in part.split(' ')] for part in match.split(' | ')]

messages = [m.strip() for m in messages.strip().split('\n')]

r0_regex = re.compile('^' + to_regex(rules, 0) + '$')
print('part 1:', sum(1 if r0_regex.match(msg) else 0 for msg in messages))
