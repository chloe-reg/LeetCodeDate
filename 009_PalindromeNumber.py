""" 
判斷一個整數x是否為palindrome數字
Follow up: 在不轉換成string的情況下解決此問題
"""
import time

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = x.__str__()
        
        left = 0
        right = len(str_x)-1
        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        
        num_array = []
        val = x
        while val != 0:
            num_array.append(val % 10)
            val = val // 10
        
        left = 0
        right = len(num_array)-1
        while left < right:
            if num_array[left] != num_array[right]:
                return False
            left += 1
            right -= 1
        
        return True

def test_case_run():
    x = 121
    print(Solution.isPalindrome2(Solution,x))
    
    x = -121
    print(Solution.isPalindrome2(Solution,x))
    
    x = 10
    print(Solution.isPalindrome2(Solution,x))
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. palindrome代表文字上由左往右讀或由右往左讀, 都一樣
2. 負數值皆被排除, 負號放在右邊沒有意義
3. 轉換成字串則取前後來倆倆比對

1. 用遞迴方式取得各進位數字, 存入陣列再一一比對
"""