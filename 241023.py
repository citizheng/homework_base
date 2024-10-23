b,c,a,c
d,c,c,b
b,d

r1=float(input())
r2=float(input())
n=int(input())
pi=3.14159
s1=pi*r1**2 - pi*r2**2
ss= n*s1
ss=round(ss,2)
print (ss)



init_amount = int(input())
year = int(input())
profit_rate = float(input())
profit= init_amount * pow((1+profit_rate), year)-init_amount
print(f"利息={profit:.2f}")



n1=int(input())
n2=int(input())
n3=int(input())
n=float((n1+n2+n3)/3)
print(f"{n:.2f}")



a=float(input())
b=float(input())
c=float(input())
def auf (a,b,c):
    lim = sorted([a,b,c])
    a,b,c = lim
    return (a**2) + (b**2) == c**2
result=auf(a,b,c)
if result==1:
    print ("YES")
else:
    print ("NO")



n=float(input())
if n>=60:
    print("pass")
else:
    print("fail")



user="whut001"
pwd="999999"
u=input()
p=input()
if u==user:
    if p==pwd:
        print("Success")
    else:
        print("Fail")
else:
    print("Fail")



use = input()
dill = (use[-1:])
num=int(use[0:-1])
if dill == 'c'or dill == 'C':
    re = num * 1.8 + 32
    print(f"转换后的温度为：{re:.2f}F")
elif dill=="f"or dill=="F":
    re = (num - 32) / 1.8
    print(f"转换后的温度为：{re:.2f}C")
else:
    print("输入有误!")



a= float(input())
b= float(input())
c= float(input())
if a==0:
    if b==0:
        print("Data error!")

    elif 0 != b:
        x=-c/b
        print(f"{x:.2f}")
elif a!=0:
    delta = b**2-4*a*c
    if delta<0:
        print("该方程无实数解")
    elif delta==0:
        x=(-b+delta**0.5)/(2*a)
        print(f"{x:.2f}")
    elif delta>0:
        x1= (-b+delta**0.5)/(2*a)
        x2= (-b-delta**0.5)/(2*a)
        print(f"{x1:.2f} {x2:.2f}")