import math
def solution(n):
    num = math.sqrt(n)
    if math.sqrt(n) == int(math.sqrt(n)): # 실수와 정수를 비교
        return pow(num+1, 2)
    return -1
