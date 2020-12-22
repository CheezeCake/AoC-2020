#!/usr/bin/env python3

import sys

class Deck:
  def __init__(self, player, deck):
    self.player = player
    self.deck = deck.copy()
    self.top = 0

  def __len__(self):
    return len(self.deck[self.top:])

  def __getitem__(self, key):
    if type(key) is slice:
      return Deck(self.player, self.deck[self.top:][key])
    elif type(key) is int:
      return self.deck[key]
    else:
      raise TypeError('index must be int or slice, not {}'.format(type(key).__name__))

  def __repr__(self):
    return f'Player {self.player}\'s deck: {self.deck[self.top:]}'

  def __eq__(self, other):
    return self.player == other.player and self.deck[self.top:] == other.deck[other.top:]

  def __hash__(self):
    return hash((self.player, ','.join(str(card) for card in self.deck[self.top:])))

  def empty(self):
    return len(self) == 0

  def get_top(self):
    card = self.deck[self.top]
    self.top += 1
    return card

  def add(self, card):
    self.deck.append(card)

def play(player1_deck, player2_deck, recurse=False):
  seen = set()
  while not player1_deck.empty() and not player2_deck.empty():
    current_state = (player1_deck, player2_deck)
    if current_state in seen:
      return player1_deck
    seen.add(current_state)

    player1_card = player1_deck.get_top()
    player2_card = player2_deck.get_top()

    winner = 1 if player1_card > player2_card else 2

    if recurse and len(player1_deck) >= player1_card and len(player2_deck) >= player2_card:
      winner = play(player1_deck[:player1_card], player2_deck[:player2_card], True).player

    if winner == 1:
      player1_deck.add(player1_card)
      player1_deck.add(player2_card)
    else:
      player2_deck.add(player2_card)
      player2_deck.add(player1_card)

  return player1_deck if player2_deck.empty() else player2_deck

def score(deck):
  return sum(c * (i + 1) for i, c in enumerate(deck[::-1]))


player1_deck, player2_deck = [[int(card) for card in player_input.strip().split('\n')[1:]] for player_input in sys.stdin.read().split('\n\n')]

deck1 = Deck(1, player1_deck)
deck2 = Deck(2, player2_deck)
print('part 1:', score(play(deck1, deck2)))

deck1 = Deck(1, player1_deck)
deck2 = Deck(2, player2_deck)
print('part 2:', score(play(deck1, deck2, True)))
