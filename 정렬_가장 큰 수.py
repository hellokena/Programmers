def solution(numbers):
    # 1. 현재 int형 원소들로 이루어진 배열들을 str로 바꾼다
    numbers = list(map(str, numbers))
    
    #2. 1000 보다 작은 수들로 이루어지므로 3번 반복해서 3자리를 비교하도록 한다.
    # 문자열*n은 문자열을 n번 반복하도록 한다
    numbers.sort(reverse=True,key=lambda x:x*3)
    
    # 000의 경우 0으로 변환하기 위해 int로 치환해준 다음 str로 변경한다
    return str(int(''.join(numbers)))
    
