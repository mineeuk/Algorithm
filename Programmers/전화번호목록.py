def solution(phonebook):
    
    phonebook.sort()
    
    for i in range(len(phonebook)-1):
        if phonebook[i] == phonebook[i+1][:len(phonebook[i])]:  
            print(phonebook[i+1])
            print(len(phonebook[i]))
            # phone_book[i+1][:len(phone_book[i])]는 "1195524421"[:3]이 되어 "119"를 반환
            return False
    return True                                 
