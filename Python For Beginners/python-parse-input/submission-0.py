from typing import List

def read_integers() -> List[int]:
    l = input().split(',')
    for i in range(len(l)):
        l[i] = int(l[i])
    
    return l

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
