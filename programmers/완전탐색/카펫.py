def solution(brown, yellow):
    answer = []
    total = brown + yellow  # 전체 타일 개수
    
    for b in range(1, total + 1):
        if (total / b) % 1 == 0: #b가 정수인지
            a = total / b
            if a>=b :
                if 2 * a+2 * b == brown + 4 :
                    return [a,b]
                
    return answer
                
            
