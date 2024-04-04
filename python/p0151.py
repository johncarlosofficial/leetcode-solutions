class Solution:

  def reverseWords(self, s: str) -> str:
    words = []  # List to store individual words
    temp = []  # Temporary list to store characters of a word

    for i in range(len(s)):
      if s[i] != " ":
        temp.append(s[i])
      else:
        if temp:
          new_word = "".join(temp)
          words.append(new_word)
          temp = []  # Clear the temporary list for the next word

    if temp:
      new_word = "".join(temp)
      words.append(new_word)

    # Reverse the order
    left, right = 0, len(words) - 1
    while left < right:
      words[left], words[right] = words[right], words[left]
      right -= 1
      left += 1

    return " ".join(words)
