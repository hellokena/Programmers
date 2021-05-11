def solution(numbers, target):
    answer = [0]
    for i in numbers:
        temp = []
        for j in answer:
            temp.append(j+i)
            temp.append(j-i)
        answer = temp
    return answer.count(target)
