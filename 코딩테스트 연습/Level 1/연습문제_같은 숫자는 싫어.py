def solution(arr):
    answer = []
    answer.append(arr[0])
    temp = arr[0]
    for i in arr[1:]:
        if i != temp:
            answer.append(i)
        temp = i
    return answer
