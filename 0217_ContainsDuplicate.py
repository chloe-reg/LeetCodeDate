""" 
判斷陣列中是否有重複的項目
"""
import time

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

def test_case_run():
    nums = [1,2,3,1]
    result = Solution.containsDuplicate(Solution, nums)
    print(result)
    nums = [1,2,3,4]
    result = Solution.containsDuplicate(Solution, nums)
    print(result)
    nums = [1,1,1,3,3,4,3,2,4,2]
    result = Solution.containsDuplicate(Solution, nums)
    print(result)
    nums = [2,14,18,22,22]
    result = Solution.containsDuplicate(Solution, nums)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

""" 
思路:
1. 排序後判斷有沒有連續相同
"""