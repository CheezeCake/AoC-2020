#!/usr/bin/env python3

import sys
import re

def parse_rule_match(match):
  m = re.match('"(.*)"', match)
  if m:
    return m.group(1)
  elif re.match('^(\d+ )*\d+$', match):
    return [[int(x) for x in match.split(' ')]]
  else:
    return [[int(x) for x in part.split(' ')] for part in match.split(' | ')]

def to_regex(rules, n, mem=None):
  if not mem:
    mem = {}
  if n in mem:
    return mem[n]
  if type(rules[n]) is str:
    mem[n] = rules[n]
    return mem[n]
  mem[n] = '(' + '|'.join('(' + (''.join(to_regex(rules, r, mem) for r in subrule) + ')') for subrule in rules[n]) + ')'
  return mem[n]


rules_input, messages = sys.stdin.read().split('\n\n')

rules = {}
for rule in rules_input.split('\n'):
  n, match = rule.strip().split(': ')
  n = int(n)
  rules[n] = parse_rule_match(match)

messages = [m.strip() for m in messages.strip().split('\n')]

r0_regex = re.compile('^' + to_regex(rules, 0) + '$')
print('part 1:', sum(1 if r0_regex.match(msg) else 0 for msg in messages))

rules[8] = parse_rule_match('42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42')
rules[11] = parse_rule_match('42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31')
r0_regex = re.compile('^' + to_regex(rules, 0) + '$')
print('part 2:', sum(1 if r0_regex.match(msg) else 0 for msg in messages))
