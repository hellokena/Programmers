  def solution(array, commands):
    answer = []
    for c in commands:
        new_array = []
        for i in range(c[0]-1, c[1]):
            new_array.append(array[i])
        new_array = sorted(new_array)
        temp = new_array[c[2]-1]
        answer.append(temp)
    return answer
