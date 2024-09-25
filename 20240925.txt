print("程序员之禅的10条黄金法则")
print("1、专注；")
print("2、心无杂念；")
print("3、初学者心态（虚怀若谷）；")
print("4、无我；")
print("5、不要设置职业目标；")
print("6、敏事慎言；")
print("7、正念、观照、觉察；")
print("8、做自己的老板；")
print("9、玩物养志；")
print("10、淡泊宁静。")


print("昨天只是今日的回忆，\n而明日不过是今天的梦。\n——纪伯伦《先知》")



print(r"http:\\www.lixin.edu.cn")




print("小明的语文，数学，英语成绩是：88	99	98。")




def reverse_integer(n):
    s=str(n)
    reversed_s = s[::-1]
    reversed_n = int(reversed_s)
    return reversed_n
n = int(input())
print(reverse_integer(n))



print("Hello World！")




print ("""he's a pirate
She said, "Hurry up.\"
""")



print(r'Python中常用的转义字符有：换行符："\n"；制表符："\t"。')



with open('data.txt','w') as file:
    n=input()
    file.write (n)
with open('data.txt','r') as file:
    content = file.read()
    print (content)



w1 = input()
w2 = input()
w3 = input()
print(w1,w2,w3,sep="\t")



m=int(input())
x=2**m
n=2**x
n_str =str(n)
n_lenth=len(n_str)
print ("n=",n,"\n","n的长度为：",n_lenth)



n1 = input()
n2 = input()
n3 = input()
print (n1,n2,n3,sep=",")




print ("眼过千遍不如手过一遍！")
print("书看千行不如手敲一行！")




A = int(input())
B = int(input())
print (A, "+", B, "=", A+B)
print (A,"-",B,"=",A-B)
print (A,"*",B,"=",A*B)
print (A,"/",B,"=",A/B)




high =float (input())
weight =float (input())
BMI = weight / ( high + weight )
print('你的BMI指数是： %.2f' %BMI)



X = eval(input())
Y = eval(input())
print (X**Y)




lenth = eval(input())
width = eval(input())
print(lenth*width)