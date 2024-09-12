n = input()

if n[::1] == n[::-1]:
    print(1)
else:
    print(0)

# [::1] 원래 문자열
# [::-1] 역순 or reversed