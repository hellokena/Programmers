def solution(n):
    answer= ''
    list = ['4','1','2']
    while n:
        mod = n%3 # 나머지를 먼저 몫보다 계산해주어야함
        n = n//3 # n을 계속해서 갱신해준다
        if mod==0: n -=1 
        answer = list[mod] + answer # 진수 계산할때 끝에서부터 계산하는 것 생각
    return answer
