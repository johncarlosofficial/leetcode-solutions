from typing import List


class Solution:

  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if (len(hand) % groupSize) != 0:
      return False

    hand.sort()

    card_freq = {}
    for card in hand:
      if card in card_freq:
        card_freq[card] += 1
      else:
        card_freq[card] = 1

    for card in card_freq:
      while card_freq[card] > 0:
        for i in range(groupSize):
          if card+i in card_freq and card_freq[card+i] > 0:
            card_freq[card+i] -= 1
          else:
            return False

    return True
            
  