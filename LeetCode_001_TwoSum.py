# 給定一個整數陣列 nums 和一個目標值 target，
# 請你在陣列中找出兩個數字的索引，使得它們的和等於目標值。
# 你可以假設每個輸入都只會有一個解，而你不可以使用相同的元素兩次。
class Solution:
    # 暴力破解法
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]


nums = [2, 6, 4]
target = 6

print(Solution.twoSum(Solution, nums, target))