#!/usr/bin/env python3

import sys
from collections import defaultdict
from copy import copy
from functools import reduce
import operator

ingredients_count = defaultdict(int)
contains_allergen = {}

for line in sys.stdin:
  line = line.strip()
  ingredients_set = set()
  if line[-1] == ')':
    ingredients_list, allergens = line[:-1].split(' (contains ')
    ingredients_set = {ingredient for ingredient in ingredients_list.split(' ')}
    for allergen in allergens.split(', '):
      if allergen in contains_allergen:
        contains_allergen[allergen] &= ingredients_set
      else:
        contains_allergen[allergen] = copy(ingredients_set)
  else:
    ingredients_set = {ingredient for ingredient in line.split(' ')}
  for ingredient in ingredients_set:
    ingredients_count[ingredient] += 1

may_contain_allergen = reduce(operator.or_, (ingredients_set for ingredients_set in contains_allergen.values()))
inert_ingredients = ingredients_count.keys() - may_contain_allergen
print('part 1:', sum(ingredients_count[ingredient] for ingredient in inert_ingredients))

allergens_found = [allergen for allergen, ingredients in contains_allergen.items() if len(ingredients) == 1]
while allergens_found:
  allergen_found = allergens_found.pop()
  for allergen in contains_allergen.keys():
    if len(contains_allergen[allergen]) == 1:
      continue
    contains_allergen[allergen] -= contains_allergen[allergen_found]
    if len(contains_allergen[allergen]) == 1:
      allergens_found.append(allergen)
print('part 2:', ','.join(ingredient for _, ingredient in sorted((allergen, list(ingredients)[0]) for allergen, ingredients in contains_allergen.items())))
