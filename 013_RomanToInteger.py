""" 
羅馬數字有七個不同的符號
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
根據輸入的羅馬符號, 回傳對應的數值
"""
import time

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        num_array = []
        for i in range(len(s)):
            if i == len(s)-1: # final number
                num_array.append(roman_to_int[s[i]])
                break
            
            if roman_to_int[s[i]] >= roman_to_int[s[i+1]]:
                num_array.append(roman_to_int[s[i]])
            else:
                num_array.append(-roman_to_int[s[i]])
        return sum(num_array)
    
    def romanToInt2(self, s: str) -> int:
        roman_to_int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        result = 0
        number = 0
        for i in range(len(s)):
            if i > 0:
                if number >= roman_to_int[s[i]]:
                    result+=number
                else:
                    result-=number
            number = roman_to_int[s[i]]
            
            if i == len(s)-1: # final number
                result+=number
                break
        return result

def test_case_run():
    s = "III"
    result = Solution.romanToInt2(Solution, s)
    print(result)
    
    s = "LVIII"
    result = Solution.romanToInt2(Solution, s)
    print(result)
    
    s = "MCMXCIV"
    result = Solution.romanToInt2(Solution, s)
    print(result)
    
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

""" 
思路:
1. 根據羅馬數字對應阿拉伯數字來建立一個字典
2. 從左到右, 由字典取得數值, 與下一位數值比較
3. 若該數值比下一位小則該數為負數填入表格 ex CM = -100 +1000
4. 若該數值比下一位大或相同則該數為正數填入表格 ex VI = +5 +1, II = +1 +1
5. 最後一位數必然是正數填入
6. 將表格數值加總可得最終結果

1. romanToInt1()去除表格機制, 直接進行數值計算, 並保存上一步驟, 不重複取值
"""