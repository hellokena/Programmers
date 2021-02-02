def solution(s):
    p_ = 0
    y_ = 0
    for i in s:
        if i in ['p', 'P']:
            p_ += 1
        if i in ['y', 'Y']:
            y_ += 1
    if p_ == y_: return True
    else: return False
