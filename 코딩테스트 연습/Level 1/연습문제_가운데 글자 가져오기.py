def solution(s):
    mid = len(s)//2
    if len(s)%2==0: #짝수
        return s[len(s)//2-1:len(s)//2+1]
    else: #홀수
        return s[len(s)//2]
    return answer
