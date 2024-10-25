class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rep = {}
        for num in nums:
            if num in rep:
                rep[num] += 1
            else:
                rep[num] = 1
        
        sorted_nums = sorted(rep, key=rep.get, reverse=True)
        
        return sorted_nums[:k]
