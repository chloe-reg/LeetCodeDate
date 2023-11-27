""" 
給予一個已排序的整數陣列 nums, 刪除其中重複的元素, 並返回新的陣列長度
要使用in-place algorithm原地演算法, 不要使用額外空間
"""
import time

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_count = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_count]:
                unique_count += 1
                nums[unique_count] = nums[i]
                
        return unique_count + 1
    
    def removeDuplicates2(self, nums: list[int]) -> int:
        index = 1
        prev_num = nums[0]
        
        while index < len(nums):
            if prev_num == nums[index]:
                nums.remove(prev_num)
            else:
                prev_num = nums[index]
                index += 1
                
        return len(nums)
        

def test_case_run():
    nums = [1,1,2]
    result = Solution.removeDuplicates(Solution, nums)
    print(result, nums)
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = Solution.removeDuplicates(Solution, nums)
    print(result, nums)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. 將後項跟前項比較
2. 題目要求用原先的空間來存放資料
3. 因為不需要在意後面非獨特數字的空間, 不需要remove()耗費資源
"""