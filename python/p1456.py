class Solution:

  def maxVowels(self, s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    left = 0
    right = k

    ans = 0

    for i in range(left, right):
      if s[i] in vowels:
        ans += 1

    temp = ans

    while right < len(s):
      if s[left] in vowels:
        temp -= 1
      left += 1

      if s[right] in vowels:
        temp += 1
      right += 1

      ans = max(ans, temp)

    return ans
