import math
def solution(progresses, speeds):
    remainList = []
    for i in range(len(progresses)):
        remainList.append(math.ceil((100 - progresses[i]) / speeds[i]))
    result = []
    temp = 0
    front_maximum = remainList[0]
    for i in range(1, len(remainList)):
        # 앞 스텝이 더 크거나 같을 경우
        if remainList[i]<=front_maximum: 
            temp += 1
        # 뒷 스텝이 더 클경우
        else:
            result.append(temp+1)
            temp = 0 # reset
            front_maximum = remainList[i]
    result.append(temp+1) # 마지막 step을 자기자신을 더해준 후 append              
    return result



