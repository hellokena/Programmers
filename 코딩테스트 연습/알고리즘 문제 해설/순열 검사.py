def solution(arr):
    arr.sort()
    for i in range(1, len(arr)+1):
        if arr[i-1] != i :
            return False
    return True
