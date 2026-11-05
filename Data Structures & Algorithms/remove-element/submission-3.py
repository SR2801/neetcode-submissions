class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        wall = n

        i = 0
        while i < wall:
            if nums[i] == val:
                wall -= 1
                nums[i], nums[wall] = nums[wall], nums[i]
            else:
                i += 1
        return wall

                