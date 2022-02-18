def solution(participant, completion):
    for i in completion :
        try :
            participant.remove(i)
        except :
            pass

    answer = participant[0]

    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])