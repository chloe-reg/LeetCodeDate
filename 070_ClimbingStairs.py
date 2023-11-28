""" 
距離n步抵達階梯頂端, 你可以一次爬1階層或兩階層, 有幾種不同的方法可以爬到頂端
"""
import time

class Solution:
    def climbStairs(self, n: int) -> int:
        one_step_count = n % 2
        two_step_count = n // 2
        result = 0
        
        while two_step_count >= 0:
            if one_step_count == 0 or two_step_count == 0:
                result += 1
            else: # C(m,k) = m!/(k!*(m-k)!)
                m = one_step_count + two_step_count
                k = two_step_count
                val = 1
                div = 1
                for i in range(m-k+1, m+1):
                    val *= i
                for i in range(2, k+1):
                    div *= i
                result += int(val / div)
            
            two_step_count -= 1
            one_step_count += 2
            
        return result
    
    def climbStairs2(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n):
            temp = b
            b = a + temp
            a = temp
        return a

def test_case_run():
    # n = 2
    # result = Solution.climbStairs(Solution, n)
    # print(result)
    # n = 3
    # result = Solution.climbStairs(Solution, n)
    # print(result)
    # n = 5
    # result = Solution.climbStairs(Solution, n)
    # print(result)
    n = 45
    result = Solution.climbStairs(Solution, n)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= n <= 45
"""

""" 
思路:
1. 用排列組合思維來解題 C(m,k) = m!/(k!*(m-k)!)
2. 花費最多步的情況一定是全部都走一個階層, 最少則為能兩階層就兩階層
    [1,1,...1,1]                       [2,2,...,2,2] or [2,2,...,2,1]
    min = n                            max = n/2 or (n/2)+1
3. [2,2,2,1,1] = C(5,3) = C(5,2)

1. 用費波那契數
"""

"""
遭遇問題:
在進行排列組合計算時, 明明是整數在做乘法和除法, 卻會算出0.9999xxxx的尾數
當使用int去強制轉態時被直接無條件捨去, 導致在n=45時計算結果與答案值僅差1
除法會產生浮點誤差, 可能會因為我這個連續除法的行為, 導致誤差值持續擴大

原先使用
    val = 1
    for i in range(m-k+1, m+1):
        val *= i
    for i in range(2, k+1):
        val /= i
    print(val) # 這時的結果會發現有誤差
    
後來改用
    val = 1
    div = 1
    for i in range(m-k+1, m+1):
        val *= i
    for i in range(2, k+1):
        div *= i
    val /= div 
    print(val) # 改完之後準確度高許多
"""