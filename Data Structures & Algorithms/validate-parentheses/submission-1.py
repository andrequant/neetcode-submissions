class Solution:
    def isValid(self, s: str) -> bool:
        sequence = []
        for element in s:
            if len(sequence) == 0 and not self.is_openning(element):
                return False
            if self.is_openning(element):
                sequence.append(element)
            else:
                if element == self.oposite(sequence[-1]):
                    sequence.pop()
                else:
                    return False
        
        if len(sequence) == 0:
            return True
        else:
            return False

    
    def is_openning(self, x):
        if x in ('(','[', '{'):
            return True
        else:
            return False
    
    def oposite(self,x):
        if x == '(':
            return ')'
        elif x == '[':
            return ']'
        elif x == '{':
            return '}'