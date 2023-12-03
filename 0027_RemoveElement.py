""" 
給予一個整數陣列nums和一個整數val, 將nums中所有val移除, 使用in-place algorithm
回傳移除val後, nums的剩餘數量
"""
import time

class Solution:
    def removeElement(self, nums:list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

def test_case_run():
    nums = [3,2,2,3]
    val = 3
    result = Solution.removeElement(Solution, nums, val)
    print(result, nums)
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = Solution.removeElement(Solution, nums, val)
    print(result, nums)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. 和026題相似, 但改為和val值比較
2. 題目要求用原先的空間來存放資料
3. 因為不需要在意後面非獨特數字的空間, 不需要remove()耗費資源
"""