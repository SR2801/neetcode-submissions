class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {n: 0 for n in nums}

        for n in nums:
            count[n] += 1
            if count[n] > len(nums)//2:
                return n
        return nums[0]

