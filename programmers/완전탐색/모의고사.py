def solution(answers):
    
    answer = []
    score = [0,0,0]
    
    s1 = [1,2,3,4,5] #5
    s2 = [2,1,2,3,2,4,2,5] #8
    s3 = [3,3,1,1,2,2,4,4,5,5] #10
    
    for i in range(len(answers)):
        if answers[i] == s1[i % 5]: #패턴 길이로 나누기
            score[0] += 1 #정답과 답안패턴 값이 같으면 맞은거로 cnt1 증가
        if answers[i] == s2[i % 8]:
            score[1] += 1
        if answers[i] == s3[i % 10]:
            score[2] += 1
    
        max_score = max(score)
    
    for i in range(3):
        if score[i] == max_score:
            #각 수포자의 점수가 최고 점수와 같으면 
            #해당 수포자 번호를 answer리스트에 추가
            answer.append(i+1)
            #수포자의 번호는 1번부터 시작해서 i+1을 리스트에 추가
    
    return answer
