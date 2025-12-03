import math

num = pow(150, 1/3)
select = 1
ans = 1

for i in range(2,16):
    temp = num*i
    print(temp)
    if temp % 1 < select:
        select = temp % 1
        ans = i

print(ans)
print(select)