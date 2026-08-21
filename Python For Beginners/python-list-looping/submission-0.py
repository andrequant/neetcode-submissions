from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    k = 0
    for i in nums:
        if i == x:
            k += 1
    return k



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
