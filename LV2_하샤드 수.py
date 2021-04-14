def solution(x):
    list_x = list(map(int, str(x)))
    if x%sum(list_x) == 0: return True
    return False
