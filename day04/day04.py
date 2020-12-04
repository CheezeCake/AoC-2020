#!/usr/bin/env python3

import re
import sys

def valid_height(h):
  valid_range = {'cm': (150, 193), 'in': (59, 76)}
  m = re.match('^(\d+)(cm|in)$', h)
  return m and valid_range[m.group(2)][0] <= int(m.group(1)) <= valid_range[m.group(2)][1]

def valid_passport(p):
  valid = {
    'byr': lambda byr: 1920 <= int(byr) <= 2002,
    'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
    'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
    'hgt': valid_height,
    'hcl': lambda hcl: re.match('^#[0-9a-f]{6}$', hcl),
    'ecl': lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda pid: re.match('^\d{9}$', pid),
    'cid': lambda _: True,
  }
  return all(valid[k](v) for k, v in p.items())

passports = []
passport = {}
for line in sys.stdin:
  if len(line) <= 1:
    passports.append(passport)
    passport = {}
    continue
  for field in line.strip().split(' '):
    name, value = field.split(':')
    passport[name] = value
passports.append(passport)

have_all_fields = [p for p in passports if len(p) == 8 or (len(p) == 7 and 'cid' not in p)]
print('part 1:', len(have_all_fields))
print('part 2:', sum(valid_passport(p) for p in have_all_fields))
