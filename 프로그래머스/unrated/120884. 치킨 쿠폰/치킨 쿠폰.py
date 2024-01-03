def solution(chicken):
    answer=0
    sum_chicken_rest=0
    
    while chicken>=1:
        chicken_rest=chicken%10
        chicken=chicken//10
        sum_chicken_rest+=chicken_rest
        answer+=chicken

    if (sum_chicken_rest//10)+(sum_chicken_rest%10) >=10 :
        answer+=(((sum_chicken_rest//10)+(sum_chicken_rest%10))//10)

    if sum_chicken_rest>=10 :
        while sum_chicken_rest >=1 :
            sum_chicken_rest = sum_chicken_rest//10
            answer+=sum_chicken_rest
            
    return answer