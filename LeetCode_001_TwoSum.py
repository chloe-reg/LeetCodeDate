# 暴力破解法
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]


nums = [3, 3]
target = 6

print(Solution.twoSum(Solution, nums, target))
