def solution(a, b):
    #0 = FRI
    day = 0
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    
    for i in range(1, a): # 1월부터 그 전달까지의 값을 더해준다
        if i in thirty_one: day+=31
        elif i in thirty: day+=30
        else: day+=29
    day+=b-1 # 왜 -1을 빼는건지는 아무리 봐도 이해 안됨,,,
    date = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return date[day%7]
