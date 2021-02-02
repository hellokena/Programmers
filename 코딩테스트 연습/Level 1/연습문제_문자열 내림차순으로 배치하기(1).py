def solution(s):
    answer = ''
    s = sorted(s)
    for i in range(len(s)-1, -1, -1):
        answer += s[i]
    return answer
