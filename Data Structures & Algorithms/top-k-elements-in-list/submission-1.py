import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq.update({i: 1})
        
        heap = []

        for n in freq.keys():
            heapq.heappush_max(heap, (freq[n], n))
        
        maxes = []

        for i in range(k):
            maxes.append(heapq.heappop_max(heap)[1])

        return maxes

        