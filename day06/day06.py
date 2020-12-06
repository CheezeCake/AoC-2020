#!/usr/bin/env python3

import sys
from functools import reduce
import operator

group_answers = [[set(answer) for answer in answers.strip().split("\n")] for answers in sys.stdin.read().split("\n\n")]
print('part 1:', sum(len(reduce(operator.or_, answers)) for answers in group_answers))
print('part 2:', sum(len(reduce(operator.and_, answers)) for answers in group_answers))
