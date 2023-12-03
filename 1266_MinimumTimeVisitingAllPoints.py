""" 
在一個2D平面上有n個點 points[i] = [xi, yi], x和y都是整數值
依著points的順序訪問這些點, 回傳最小時間
規則: 
    在一秒的時間你可以:
        1. 垂直移動1單位
        2. 水平移動1單位
        3. 斜向移動sqrt(2)單位 = 垂直1+水平1
    訪問的順序必須依照list
    可以經過別的點, 但是不被記錄成已訪問
"""
import time

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 0
        
        start_point = None
        time = 0
        for point in points:
            if start_point is None:
                start_point = point
                continue
            
            end_point = point
            x = abs(end_point[0]-start_point[0])
            y = abs(end_point[1]-start_point[1])
            slope = min(x, y)
            time += x + y - slope
            start_point = point
        return time

def test_case_run():
    points = [[1,1],[3,4],[-1,0]]
    result = Solution.minTimeToVisitAllPoints(Solution, points)
    print(result)
    points = [[3,2],[-2,2]]
    result = Solution.minTimeToVisitAllPoints(Solution, points)
    print(result)
    return

start = time.perf_counter()
test_case_run()
end = time.perf_counter()
print("執行時間：%f 豪秒" % ((end - start)*1000))

"""
Constraints:
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
"""

""" 
思路:
1. 拿下一個點跟這個點算出水平垂直的距離, 減去可以斜向行徑的次數, 得到訪問下一點的時間

"""