# 핵심은 한 구명보트에 최대한 많은 사람들 태우는 것
# -> 문제 조건에서 최대 2명 태울 수 있다고 적혀있음
def solution(people, limit):
    answer = len(people)
    people.sort(reverse=True)
    start = 0
    end = answer-1
    while start<end:
        if people[start]+people[end]<=limit:
            answer -=1
            end-=1 # limit안에 들어야함 end를 없앰
            # 가장 무거운 사람을 태우고
            # 남은 1자리를 가벼운 사람부터 차례로 고려함
        start+=1
    return answer
