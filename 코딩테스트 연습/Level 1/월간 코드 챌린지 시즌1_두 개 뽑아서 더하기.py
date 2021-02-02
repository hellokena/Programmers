def solution(numbers):
    answer = []
    for a,i in enumerate(numbers):
        for b,j in enumerate(numbers):
            if a == b:
                continue
            answer.append(i+j)
    answer = set(answer)
    answer = list(answer)
    answer = sorted(answer)
    return answer
