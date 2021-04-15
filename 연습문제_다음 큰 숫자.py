def solution(n):
    next_n = n
    while True:
        next_n += 1 # 조건1
        n_2 = bin(n)
        next_n_2 = bin(next_n)
        print(n_2, next_n_2)
        if str(n_2).count('1') == str(next_n_2).count('1'): # 조건2
            print(next_n)
            return next_n
