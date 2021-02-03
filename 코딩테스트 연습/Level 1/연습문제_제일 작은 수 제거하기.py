def solution(arr):
    empty = [-1]
    arr.remove(min(arr))
    if len(arr)==0:
        return empty
    else:
        return arr
