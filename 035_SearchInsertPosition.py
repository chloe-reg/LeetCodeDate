""" 
給予一個已排序的整數陣列和目標數字, 回傳這個目標會被放在這個陣列的位置
演算法必須是O(log(n))的時間複雜度
"""
import time

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)
    
    def searchInsert2(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return left

def test_case_run():
    nums = [1,3,5,6]
    target = 5
    result = Solution.searchInsert2(Solution, nums, target)
    print(result)
    
    nums = [1,3,5,6]
    target = 2
    result = Solution.searchInsert2(Solution, nums, target)
    print(result)
    
    nums = [1,3,5,6]
    target = 7
    result = Solution.searchInsert2(Solution, nums, target)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. 因為數列已排序, 可以單純比較數值大小
2. 若遍歷完數組, 代表target最大, 放在最後 O(n)

1. 題目要求O(lon(n)), 代表要使用二分搜索法
"""