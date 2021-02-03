def solution(n):
    answer = []
    n = list(str(n))
    while len(n) > 0:
        answer.append(max(n))
        n.remove(max(n))
    return int(''.join(answer))
