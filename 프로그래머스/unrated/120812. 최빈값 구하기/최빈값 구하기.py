def solution(array):
    answer = 0
    count=[]
    list1=[]
    for i in array : 
        count.append(array.count(i))

    for j in range(0,len(count)) :
        if max(count)==count[j] :
            list1.append(array[j])

    if len((set(list1)))>1:
        answer = -1
    elif len((set(list1)))==1 :
        answer = max((set(list1)))
    return answer