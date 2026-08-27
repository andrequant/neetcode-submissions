class Solution:
    def countLetters(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            letter = s[i]
            c += 1
            for j in range(len(s)-i-1):
                nextl = s[i+j+1]
                if letter == nextl:
                    c += 1
                else:
                    break

        return c
