def solution(s):
    array = list(map(int, s.split()))
    return str(min(array))+ ' ' + str(max(array))
  
def solution(s):
    array = list(map(int, s.split()))
    a  = []
    a.append(str(min(array)))
    a.append(str(max(array)))
    return ' '.join(a)
    
