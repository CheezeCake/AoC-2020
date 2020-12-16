#!/usr/bin/env python3

import sys
import re
from functools import reduce
import operator

def parse_rules(rules):
  res = {}
  r = re.compile('(.*): (\d+)-(\d+) or (\d+)-(\d+)')
  for rule in rules.split('\n'):
    m = r.match(rule)
    name, s1, e1, s2, e2 = m.groups()
    res[name] = [(int(s1), int(e1)), (int(s2), int(e2))]
  return res

def rules_not_matching(val, rules):
  return {name for name, rule  in rules.items() if (val < rule[0][0] or val > rule[0][1]) and (val < rule[1][0] or val > rule[1][1])}


rules, my_ticket, nearby_tickets = sys.stdin.read().split('\n\n')
rules = parse_rules(rules)
my_ticket = [int(value) for value in my_ticket.strip().split('\n')[1].split(',')]
nearby_tickets = [[int(value) for value in values.split(',')] for values in nearby_tickets.strip().split('\n')[1:]]

nt_rules_not_matching = [[rules_not_matching(value, rules) for value in ticket] for ticket in nearby_tickets]

invalid_tickets = set()
s = 0
for i in range(len(nearby_tickets)):
  for value, rules_not_matching in zip(nearby_tickets[i], nt_rules_not_matching[i]):
    if len(rules_not_matching) == len(rules):
      s += value
      invalid_tickets.add(i)
print('part 1:', s)


field_match = []
for j in range(len(rules)):
  not_matching = reduce(operator.or_, (nt_rules_not_matching[i][j] for i in range(len(nearby_tickets)) if i not in invalid_tickets))
  field_match.append(set(rules.keys()) - not_matching)

found = [field for field in field_match if len(field) == 1]
new_found = []
while len(found) > 0:
  for f in found:
    for j in range(len(field_match)):
      if len(field_match[j]) == 1:
        continue
      x = field_match[j] - f
      if len(x) == 1:
        new_found.append(x)
      field_match[j] = x
  found = new_found
  new_found = []

x = 1
for j in range(len(field_match)):
  match = list(field_match[j])[0]
  if match.startswith('departure'):
    x *= my_ticket[j]
print('part 2:', x)
