def solution(prices):
    answer = [0 for i in range(len(prices))]
    # 뒤 인덱스에서 자기보다 크거나 같은 수의 갯수(자신을 제외하고)
    for p1 in range(len(prices)): # 마지막 횟수 제외
        for p2 in range(p1+1, len(prices)): # 자기 자신 제외
            answer[p1] += 1 # 다음 횟수에 떨어지더라도 1초는 유지됨
            if prices[p1] > prices[p2]: # 반대
                break
    return answer
