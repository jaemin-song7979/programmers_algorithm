def solution(num, k):
    answer = 0
    answer = str(num).find(str(k))
    
    if answer > -1 :
        answer = answer+1
    else :
        answer = answer
    
    return answer