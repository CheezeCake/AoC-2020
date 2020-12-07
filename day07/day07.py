#!/usr/bin/env python3

import re
import sys

def can_contain(bag, target, bags, mem={}):
  if bag in mem:
    return mem[bag]
  if target in bags[bag]:
    mem[bag] = True
    return True
  for contained in bags[bag].keys():
    if can_contain(contained, target, bags):
      mem[bag] = True
      return True
  mem[bag] = False
  return False

def count(bag, bags, mem={}):
  if bag in mem:
    return mem[bag]
  mem[bag] = sum(n + n * count(contained, bags) for contained, n in bags[bag].items())
  return mem[bag]

bags = {}
for line in sys.stdin:
  m = re.match('(.+) bags contain (.+)\.', line)
  bag_color = m.group(1)
  bag_content = {}
  for contained in m.group(2).split(', '):
    m = re.match('(\d) (.+) bags?', contained)
    if m:
      bag_content[m.group(2)] = int(m.group(1))
  bags[bag_color] = bag_content

print('part 1:', sum(can_contain(color, 'shiny gold', bags) for color in bags.keys()))
print('part 2:', count('shiny gold', bags))
