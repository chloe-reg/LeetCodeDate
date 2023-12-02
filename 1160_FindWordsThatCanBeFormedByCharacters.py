""" 
給你一個字符串数组 words 和一個字符串 chars
如果 words[i] 可以用 chars 中的字母組成, 那麼返回所有這些單詞的長度之和
"""
import time

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_count = [0]*26
        for char in chars:
            char_count[ord(char)-ord('a')] += 1
        
        result = 0
        for word in words:
            word_count = [0]*26
            val = 0
            for char in word:
                index = ord(char)-ord('a')
                word_count[index] += 1
                if word_count[index] > char_count[index]:
                    val = 0
                    break
                else:
                    val += 1
            result += val
        return result

def test_case_run():
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    result = Solution.countCharacters(Solution, words, chars)
    print(result)
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    result = Solution.countCharacters(Solution, words, chars)
    print(result)
    words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin","ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb","ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl","boygirdlggnh","xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx","nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop","hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx","juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr","lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo","oxgaskztzroxuntiwlfyufddl","tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp","qnagrpfzlyrouolqquytwnwnsqnmuzphne","eeilfdaookieawrrbvtnqfzcricvhpiv","sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz","yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue","hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv","cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob","qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs","qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
    chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
    result = Solution.countCharacters(Solution, words, chars)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""

""" 
思路:
1. 先統計chars中包含的字母總數
2. 如果word需要的字母數大於chars總數代表無法組成字母, val值設成零, 否則val加總長度
3. 加總所有輸出的val值可以得到結果
"""