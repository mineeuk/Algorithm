def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i] # 두 리스트를 정렬했기 때문에 동일 인덱스에 있는 값이 다르면 그 사람이 완주못한 선수.

    # 반복문이 끝나도 반환되지 않았다면, 이는 completion 리스트의 모든 요소가 participant와 일치한다는 뜻. 
    return participant[len(participant)-1] # 정렬된 participant의 마지막 요소(participant[len(participant) - 1])가 완주하지 못한 사람.