def solution(citations):
    answer = 0
  
    citations.sort(reverse=True)
    
    #i: 인용횟수, citation: h
    for i, citation in enumerate(citations):
        if i >= citation :
            return i
    
    return len(citations)    
    print(citations)
    # return answer
