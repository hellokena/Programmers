def solution(answers):
    
    answer = [] 
    score1 = 0
    score2 = 0
    score3 = 0
    
    std1 = [1,2,3,4,5]
    std2 = [2,1,2,3,2,4,2,5]
    std3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if std1[i%len(std1)] == answers[i]:
            score1 += 1
        if std2[i%len(std2)] == answers[i]:
            score2 += 1
        if std3[i%len(std3)] == answers[i]:
            score3 += 1
            
    temp = [score1, score2, score3]
    
    for j,v in enumerate(temp):
        if v == max(temp):
            answer.append(j+1)
            
    return answer
