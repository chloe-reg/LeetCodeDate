'''
給定一個整數陣列 nums 和一個目標值 target，
請你在陣列中找出兩個數字的索引，使得它們的和等於目標值。
你可以假設每個輸入都只會有一個解，而你不可以使用相同的元素兩次。
'''
class Solution:
    # 暴力破解法
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [] # not found
    
    # 字典索引法 - 時間複雜度 O(n)
    def twoSumHashMap(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return [] # not found
        


nums = [2, 6, 4]
target = 6
result = Solution.twoSumHashMap(Solution, nums, target)

print(result)

'''
暴力法： 
    遍歷每一對數字，檢查它們的和是否等於目標值。
    這種方法的時間複雜度是 O(n^2)，其中 n 是數組的長度。
HashMap 方法： 
    使用 HashMap 來記錄每個數字及其索引，然後遍歷一次數組，
    查找目標值與當前數字的差值是否在 HashMap 中，時間複雜度是 O(n)。
雙指針方法： 
    對數組進行排序，然後使用兩個指針，一個指向開始，一個指向結尾，
    根據它們的和與目標值的大小調整指針的位置。這種方法的時間複雜度也是 O(n)。
集合（Set）方法： 
    將數組轉換為集合，然後遍歷數組，查找目標值減去當前數字的差值是否在集合中。
    這種方法的時間複雜度是 O(n)，但需要額外的空間來存儲集合。

HashMap 方法在效率和實現上都相對優越，因此在實際應用中經常被採用。
'''