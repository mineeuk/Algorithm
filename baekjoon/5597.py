"""
풀이법 #1
"""

# 입력 총 28 줄 1<=n<=30

student=[]
not_student=[]
for i in range(28):
    s=int(input())
    student.append(s)

for i in range(1,31):
    if i not in student:
        not_student.append(i) 

print(min(not_student))
print(max(not_student))

"""
풀이법 #2
"""
students = [i for i in range(1,31)] # 1~30 => 30명

for i in range(28): #  28명이 제출
  n = int(input())  # 출석번호
  students.remove(n) # 입력받은 출석번호를 students 배열에서 지워주면 출석번호가 안불린 번호만 남게됩니다.

students.sort() # 작은 값 부터 정렬

for i in range(len(students)):
  print(students[i])