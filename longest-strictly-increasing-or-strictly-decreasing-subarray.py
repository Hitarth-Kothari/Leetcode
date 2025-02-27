class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        stored_inc = 1
        stored_dec = 1
        running_inc = 1
        running_dec = 1

        up_or_down = None

        if len(nums) <= 1:
            return 1
        
        curr = nums[0]

        for i in nums:
            if curr == i:
                up_or_down = None
                stored_inc = max(stored_inc, running_inc)
                stored_dec = max(stored_dec, running_dec)
                running_inc = 1
                running_dec = 1
            elif up_or_down == None:
                if i > curr:
                    up_or_down = True
                    running_inc += 1
                else:
                    up_or_down = False
                    running_dec += 1
            elif i > curr and up_or_down:
                running_inc += 1
            elif i < curr and not up_or_down:
                running_dec += 1
            else:
                up_or_down = not up_or_down
                stored_inc = max(stored_inc, running_inc)
                stored_dec = max(stored_dec, running_dec)
                running_inc = 2
                running_dec = 2
            curr = i

        return max(stored_inc, stored_dec, running_inc, running_dec)
