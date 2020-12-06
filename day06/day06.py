#!/usr/bin/env python3

import sys
from collections import Counter

group_answers = [answers.strip().split("\n") for answers in sys.stdin.read().split("\n\n")]
print('part 1:', sum(len(set(''.join(answers))) for answers in group_answers))
print('part 2:', sum(n == len(answers) for answers in group_answers for n in Counter(''.join(answers)).values()))
