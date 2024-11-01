class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = []

        for char in s:
            if len(answer) >= 2 and answer[-2] == answer[-1] == char:
                continue
            else:
                answer.append(char)

        return "".join(answer)
        