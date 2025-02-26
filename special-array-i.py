class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        even = (nums[0]%2==0)

        for i in range(1, len(nums)):
            if even == (nums[i]%2==0):
                return False
            else:
                even = not even
        
        return True
