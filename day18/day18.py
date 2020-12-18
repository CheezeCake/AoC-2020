#!/usr/bin/env python3

import sys

class Expression:
  def evaluate(self):
    pass

  def __repr__(self):
    pass

class Constant(Expression):
  def __init__(self, value):
    self.value = value

  def evaluate(self):
    return self.value

  def __repr__(self):
    return str(self.value)

class Operation(Expression):
  def __init__(self, op, left, right):
    self.op = op
    self.left = left
    self.right = right

  def evaluate(self):
    a = self.left.evaluate()
    b = self.right.evaluate()
    if self.op == '+':
      return a + b
    elif self.op == '*':
      return a * b
    raise Exception(f'unknown operator: {self.op}')

  def __repr__(self):
    return f'({self.left} {self.op} {self.right})'

class Parser:
  def __init__(self, ops):
    self.__ops = ops

  def parse(self, tokens):
    self.tokens = tokens
    self.token_idx = 0
    self.next()
    return self.expr()

  def next(self):
    if self.token_idx < len(self.tokens):
      self.current = self.tokens[self.token_idx]
      self.token_idx += 1
    else:
      self.current = None

  def expr(self, prec_lvl=0):
    if prec_lvl >= len(self.__ops):
      return self.final()
    result = self.expr(prec_lvl + 1)
    while self.current in self.__ops[prec_lvl]:
      op = self.current
      left_operand = result
      self.next()
      right_operand = self.expr(prec_lvl + 1)
      result = Operation(op, left_operand, right_operand)
    return result

  def final(self):
    result = None
    if type(self.current) == int:
      result = Constant(self.current)
      self.next()
    elif self.current == '(':
      self.next()
      result = self.expr()
      if self.current != ')':
        raise Exception('expected )')
      self.next()
    else:
      raise Exception('expected number or (expr)')
    return result

def tokenize(s):
  tokens = []
  i = 0
  while i < len(s):
    c = s[i]
    if c in ['+', '*', '(', ')']:
      tokens.append(c)
    elif c.isdigit():
      n = int(c)
      while i + 1 < len(s) and s[i + 1].isdigit():
        n = n * 10 + int(s[i + 1])
        i += 1
      tokens.append(n)
    elif c != ' ':
      raise 'unknown symbol: ' + c
    i += 1
  return tokens

def eval_math_expr(s, ops):
  tokens = tokenize(s)
  tree = Parser(ops).parse(tokens)
  return tree.evaluate()


expressions = [line.strip() for line in sys.stdin]
print('part 1:', sum(eval_math_expr(expr, [['+', '*']]) for expr in expressions))
print('part 2:', sum(eval_math_expr(expr, [['*'], ['+']]) for expr in expressions))
