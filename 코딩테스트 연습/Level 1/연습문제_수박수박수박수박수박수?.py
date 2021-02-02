def solution(n):
    answer = ''
    # 홀수 : 수, 짝수 : 박
    for i in range(1, n+1):
        if i%2 == 0:
            answer = answer + "박"
        else :
            answer = answer + "수"
    return answer
