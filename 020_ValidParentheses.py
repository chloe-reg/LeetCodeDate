""" 
給予一個字串, 檢查括號是否匹配, 且要考慮閉合順序
'(', ')', '{', '}', '[' and ']'
"""
import time

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {'(':')','{':'}','[':']'}
        
        for char in s:
            if char not in parentheses_dict.keys():
                if len(stack) == 0:
                    return False
                if stack.pop() != char:
                    return False
            else:
                pair = parentheses_dict[char]
                stack.append(pair)
        
        return len(stack) == 0

def test_case_run():
    s = "()"
    result = Solution.isValid(Solution,s)
    print(result)
    
    s = "()[]{}"
    result = Solution.isValid(Solution,s)
    print(result)
    
    s = "(]"
    result = Solution.isValid(Solution,s)
    print(result)
    
    s = "([)]"
    result = Solution.isValid(Solution,s)
    print(result)
    
    s = "{[]}"
    result = Solution.isValid(Solution,s)
    print(result)
    
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. 用Stack來處理順序
2. 遇到左括號, 將右括號存進stack中...
3. 當遇到右括號, 將stack中的括號輸出檢查 O(n)
"""