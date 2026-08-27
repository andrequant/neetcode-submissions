class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            j = gifts.index(max(gifts))
            gifts[j] = int(gifts[j]**0.5)

        return sum(gifts)