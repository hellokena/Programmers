def solution(s):
    s = s.lower()
    array = s.split(" ")
    answer = ""
    for i in array:
        i = i.capitalize()
        answer += i + " "
    return answer[:-1]
