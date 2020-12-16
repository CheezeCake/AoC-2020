#!/usr/bin/env python3

import sys
import re
from functools import reduce
import operator
from math import prod

rules, my_ticket, nearby_tickets = sys.stdin.read().split('\n\n')
rules = {field: [int(s1), int(e1), int(s2), int(e2)] for field, s1, e1, s2, e2 in (re.match('(.*): (\d+)-(\d+) or (\d+)-(\d+)', rule).groups() for rule in rules.split('\n'))}
my_ticket = [int(value) for value in my_ticket.strip().split('\n')[1].split(',')]
nearby_tickets = [[int(value) for value in values.split(',')] for values in nearby_tickets.strip().split('\n')[1:]]

rules_not_matching = [[{f for f, (s1, e1, s2, e2) in rules.items() if (val < s1 or val > e1) and (val < s2 or val > e2)} for val in ticket] for ticket in nearby_tickets]

invalid_tickets = set()
s = 0
for i in range(len(nearby_tickets)):
  for value, not_matching in zip(nearby_tickets[i], rules_not_matching[i]):
    if len(not_matching) == len(rules):
      s += value
      invalid_tickets.add(i)
print('part 1:', s)

rule_set = set(rules.keys())
field_match = [rule_set - reduce(operator.or_, (rules_not_matching[i][j] for i in range(len(nearby_tickets)) if i not in invalid_tickets)) for j in range(len(rules))]

found = [field for field in field_match if len(field) == 1]
while found:
  f = found.pop()
  for j in range(len(field_match)):
    if len(field_match[j]) == 1:
      continue
    x = field_match[j] - f
    if len(x) == 1:
      found.append(x)
    field_match[j] = x

print('part 2:', prod(my_ticket[j] for j in range(len(field_match)) if list(field_match[j])[0].startswith('departure')))
