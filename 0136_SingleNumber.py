""" 
給予一個非空的整數陣列nums, 且每個元素都會重複兩次, 除了只出現一次的, 回傳只出一次的
使用線性時間複雜度的解決方案, 並僅使用恆定的額外空間
"""
import time

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

def test_case_run():
    nums = [2,2,1]
    result = Solution.singleNumber(Solution, nums)
    print(result)
    nums = [4,1,2,1,2]
    result = Solution.singleNumber(Solution, nums)
    print(result)
    nums = [1]
    result = Solution.singleNumber(Solution, nums)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice 
    except for one element which appears only once.
"""

""" 
思路:
1. 題目要求時間複雜度O(n), 就不能用雙層迴圈暴力破解(O(n^2)), 要利用XOR的特點來解這題
2. XOR兩個相同的數字則輸出為0
3. 初始結果值設定為0, 如果數列中出現兩個相同的數字, 則前後對結果做XOR相當於不變
4. 於是結果值最後剩下的數值, 即為數列中唯一只出現一次的值
"""