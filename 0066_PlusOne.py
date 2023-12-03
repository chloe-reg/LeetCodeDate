""" 
有一個large integer被放在一個digits的陣列中, 最高位放在最左邊, 且沒有前導數字 0
將這個數字+1, 並回傳結果陣列
"""
import time

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        val = digits[-1] + 1
        result = [val % 10]
        carry = val // 10
        
        for i in reversed(range(len(digits)-1)):
            val = digits[i] + carry
            result.insert(0, val % 10)
            carry = val // 10
        
        if carry != 0:
            result.insert(0, carry)
        return result
    
    def plusOne2(self, digits: list[int]) -> list[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            val = digits[i] + carry
            digits[i] = val % 10
            carry = val // 10
            if carry == 0:
                return digits
        
        if carry != 0:
            digits.insert(0, carry)
        return digits
    
    def plusOne3(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits
            
        
def test_case_run():
    digits = [1,2,3]
    result = Solution.plusOne3(Solution, digits)
    print(result)
    digits = [4,3,2,1]
    result = Solution.plusOne3(Solution, digits)
    print(result)
    digits = [9]
    result = Solution.plusOne3(Solution, digits)
    print(result)
    digits = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    result = Solution.plusOne3(Solution, digits)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. large integer, 代表這個數字可能超過標準整數型態 ex int, long 的範圍
    如題目所表示他的位數範圍是1~100位數, long的範圍才到19位數
2. 沒有前導數字, 若第一位是0, 代表數字本身就是0
3. 題目沒提到要用原地演算, 建立一個新的回傳陣列
4. 或是藉由本身的digits來儲存, 有需要的話新增一項在0的位置(進位)

5.          reversed(range(len(digits))) vs range(len(digits)-1, -1, -1)
    Runetime               win           |
    Memory                               |               win
"""