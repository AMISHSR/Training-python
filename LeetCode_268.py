class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = math.factorial(len(nums))
        value = 1
        for num in nums:
            if num == 0:
                continue
            else:
                value = value * num    
        missing = result // value
        if missing in nums:
            missing = 0
        return missing

