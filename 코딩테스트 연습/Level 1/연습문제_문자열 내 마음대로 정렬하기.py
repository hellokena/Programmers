def solution(strings, n):
    
    strings.sort() #먼저 순서대로 sort시킨다(제한조건 5)
    key = []
    answer=[]
    for i in strings:
        key.append(i[n])
        
    key.sort() # 각 문자를 정렬
    
    for a in key:
        for b in strings:
            if a==b[n]:
                answer.append(b)
                strings.remove(b)
                break
    return answer
