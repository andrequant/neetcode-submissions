import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            j = gifts.index(max(gifts))
            gifts[j] = math.floor(math.sqrt(gifts[j]))

        return sum(gifts)