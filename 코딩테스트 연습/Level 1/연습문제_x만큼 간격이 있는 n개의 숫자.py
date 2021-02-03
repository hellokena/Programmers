def solution(x, n):
    answer = []
    new_x=abs(x)
    for i in range(new_x, new_x*n+1, new_x):
        if x>=0:
            answer.append(i)
        else:
            answer.append(-i)
    return answer
