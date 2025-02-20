class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        turns = 0
        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if min(x,y) >= k:
                return turns
            turns += 1
            heapq.heappush(nums, min(x,y)*2 + max(x,y))
        if nums[0] >= k:
            return turns        
