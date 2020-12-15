#!/usr/bin/env python3

import sys

def play(nums, last, start, end):
  for i in range(start, end + 1):
    if len(nums[last]) == 1:
      last = 0
    else:
      last = nums[last][1] - nums[last][0]
    if last not in nums:
      nums[last] = (i, )
    elif len(nums[last]) == 1:
      nums[last] = (nums[last][0], i)
    else:
      nums[last] = (nums[last][1], i)
  return last


input = [int(n) for n in sys.argv[1].split(',')]
nums = {n: (i + 1, ) for i, n in enumerate(input)}
x = play(nums, input[-1], len(input) + 1, 2020)
print('part 1:', x)
print('part 2:', play(nums, x, 2021, 30000000))
