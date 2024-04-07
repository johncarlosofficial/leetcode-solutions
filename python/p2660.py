from typing import List


class Solution:

  def isWinner(self, player1: List[int], player2: List[int]) -> int:

    if len(player1) == 1:
      if player1[0] == player2[0]:
        return 0
      elif player1[0] > player2[0]:
        return 1
      else:
        return 2

    if len(player2) == 2:
      score1 = player1[0] + player1[1]
      score2 = player2[0] + player2[1]

      if score1 == score2:
        return 0
      elif score1 > score2:
        return 1
      else:
        return 2

    score1 = player1[0] + player1[1] if player1[0] != 10 else player1[0] + (
        2 * player1[1])
    score2 = player2[0] + player2[1] if player2[0] != 10 else player2[0] + (
        2 * player2[1])

    for i in range(2, len(player1)):
      if player1[i - 1] == 10 or player1[i - 2] == 10:
        score1 += 2 * player1[i]
      else:
        score1 += player1[i]

    for i in range(2, len(player2)):
      if player2[i - 1] == 10 or player2[i - 2] == 10:
        score2 += 2 * player2[i]
      else:
        score2 += player2[i]

    if score1 > score2:
      return 1
    elif score1 < score2:
      return 2
    else:
      return 0
