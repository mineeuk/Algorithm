def solution(numbers):
    # numbers 원소로
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    return str(int(''.join(numbers)))
    # print(numbers)
            
