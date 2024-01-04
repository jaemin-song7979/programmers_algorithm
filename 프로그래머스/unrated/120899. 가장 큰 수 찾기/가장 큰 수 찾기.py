def solution(array):
    answer = []
    for i in range(0,len(array)) :
        if max(array) == array[i] :
            answer.append(array[i])
            answer.append(i)
    return answer