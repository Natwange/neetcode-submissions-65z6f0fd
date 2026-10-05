class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                if value > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])

        return res