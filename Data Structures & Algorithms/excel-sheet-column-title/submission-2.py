class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        current_number = columnNumber
        letters = []
        while current_number > 0:
            current_number -= 1
            l = current_number % 26
            letters.append(chr(l+65))
            current_number = current_number // 26 
            
        letters.reverse()
        return "".join(letters)