#!/usr/bin/env python3

import sys

def two_sum(nums, target):
  s = set()
  for n in nums:
    if n in s:
      return True
    s.add(target - n)
  return False

def find_invalid_number(nums):
  for i in range(25, len(nums)):
    if not two_sum(nums[i - 25:i], nums[i]):
      return nums[i]

def find_weakness(nums, invalid):
  start, end = 0, 1
  sum = nums[start]
  while sum != invalid and end < len(nums):
    if sum > invalid:
      sum -= nums[start]
      start += 1
    else:
      sum += nums[end]
      end += 1
  return min(nums[start:end]) + max(nums[start:end])


nums = [int(n) for n in sys.stdin]
invalid = find_invalid_number(nums)

print('part 1:', invalid)
print('part 2:', find_weakness(nums, invalid))
