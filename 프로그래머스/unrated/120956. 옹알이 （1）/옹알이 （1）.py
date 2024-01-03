def solution(babbling):
    answer = 0
    sound =["aya", "ye", "woo", "ma"]
    make_sound = ''

    for i in range(1,5) :
        if i == 1 :
            for j in range (0,4) :
                make_sound = sound[j]
                for x in range(0,len(babbling)) : 
                    if make_sound == babbling[x] :
                        answer += 1

        if i == 2 :
            for j in range (0,4) :
                for k in range (0,4) :
                    if sound[j]!=sound[k] :
                        make_sound=sound[j]+sound[k]
                        for x in range(0,len(babbling)) : 
                            if make_sound == babbling[x] :
                                answer += 1

        if i == 3 :
             for j in range (0,4) :
                for k in range (0,4) :
                    for q in range (0,4) :
                        if sound[j]!=sound[k] and sound[k]!=sound[q] and sound[j]!=sound[q] :
                            make_sound=sound[j]+sound[k]+sound[q]
                            for x in range(0,len(babbling)) : 
                                if make_sound == babbling[x] :
                                    answer += 1
        if i == 4 :
             for j in range (0,4) :
                for k in range (0,4) :
                    for q in range (0,4) :
                        for s in range (0,4) :
                            if sound[j]!=sound[k] and sound[j]!=sound[q] and sound[j]!=sound[s] and sound[k]!=sound[q] and sound[k]!=sound[s] and sound[q]!=sound[s] :
                                make_sound=sound[j]+sound[k]+sound[q]+sound[s]
                                for x in range(0,len(babbling)) : 
                                    if make_sound == babbling[x] :
                                        answer += 1

    return answer