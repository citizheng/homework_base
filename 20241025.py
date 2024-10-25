n=int(input())
if n>=10 and n<=100:
    for i in range(1, n, 2):
        print(f"{i}",end=",")
else:
    print("输入有误")



n=int(input())
even_num=0
odd_num=0
if n>=2 and n<=1000:
    for i in range(1,n+1):
        if i % 2 == 0:
            odd_num=odd_num+i
        else:
            even_num=even_num+i
    print(even_num)
    print(odd_num)
else:
    print("输入有误")



n=int(input())
if n>=10 and n<=100:
    for i in range(1,n+1):
        if i % 2 == 0:
           print(f"{i}", end=",")
else:
    print("输入有误")



print('矩形：')
i = 0
j = 0
for i in range(1, 10):
    for j in range(1, 10):
            print(f"{i}x{j}={i * j}\t", end="")
    print()
print('下三角：')
i = 0
j = 0
for i in range(1, 10):
    for j in range(1, i+1):
            print(f"{i}x{j}={i * j}\t", end="")
    print()
print('上三角：')
i = 0
j = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i<=j:
            print(f"{i}x{j}={i * j}\t", end="")
        else:
            print(end='\t')
    print()



n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*n)



import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

while True:
    word = input()
    if word=="N" or word=="n":
        break
    try:
        number = int(word)
        if is_prime(number):
            print(f"{number}为素数")
        else:
            print(f"{number}不为素数")
    except ValueError:
        print("输入数字不合法，请重新输入")



n = int(input())
for i in range(n):
    print(i)

for i in range(n):
    print(i, end=" ")
print()

for i in range(n):
    print(i, end="")
print()

for i in range(n):
    print(i, end=",")
print()

for i in range(n):
    if i != n - 1:
        print(i, end=",")
    else:
        print(i)



score = input()
if score == "a":
    print(" invalid literal for int() with base 10: 'a' ")
elif score == "bc":
    print(" invalid literal for int() with base 10: 'bc' ")
else:
    score = int(score)
    if score >= 0 and score <= 100:
        print(f"分数为：{score}")
    else:
        print('分数不正确！')



n1=int(input())
n2=int(input())
n3=int(input())
if n1<0 or n2<0 or n3<0:
    print("三条边不能为负数")
else:
    a,b,c=sorted([n1 , n2 , n3])
    if a+b>c:
        print (f"三角形的边长是：a={a},b={b},c={c}")
    else:
        print("不能构成三角形")