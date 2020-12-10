#!/usr/bin/env python3

import sys

def find_chain(adapters_set, joltage=0, chain=[0]):
  if len(adapters_set) == 0:
    return True
  for j in range(joltage, joltage + 4):
    if j in adapters_set:
      adapters_set.remove(j)
      chain.append(j)
      if find_chain(adapters_set, j, chain):
        return chain
      chain.pop()
      adapters_set.add(j)
  return False


adapters = [int(joltage) for joltage in sys.stdin]
device = max(adapters) + 3
adapters.append(device)

chain = find_chain(set(adapters))

one_diff = 0
three_diff = 0
for i in range(len(chain) - 1):
  diff = chain[i + 1] - chain[i]
  if diff == 1:
    one_diff += 1
  elif diff == 3:
    three_diff += 1
print('part 1:', one_diff * three_diff)

s = set(adapters)
dp = [0 for _ in range(device + 1)]
dp[0] = 1
for j in range(1, device + 1):
  if j in s:
    dp[j] = sum(dp[max(0, j - 3):j])
print('part 2:', dp[-1])
