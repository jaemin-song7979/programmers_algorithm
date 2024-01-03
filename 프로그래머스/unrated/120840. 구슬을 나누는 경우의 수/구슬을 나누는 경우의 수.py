def solution(balls, share):
    answer = 0
    share1=share
    share2=share
    list1 = []
    list2 = []
    num1 = 1
    num2 = 1
    
    while share1>0 :
        list2.append(balls)
        print(list2)
        balls-=1
        share1-=1
    

    for i in list2 :
        num2*=i
    up = num2

    while share2>0 :
        list1.append(share2)
        print(list1)
        share2-=1

    for j in list1 :
        num1*=j    
    down = num1

    answer = up//down
        
    return answer