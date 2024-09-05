a=int(input("a の値を入力: "))
b=int(input("b の値を入力: "))
while a!=b:
    if a==0:
        print(b)
        break
    elif b==0:
        print(a)
        break
    elif a>b:
        a-=b
    else:
        b-=a
if a==b:
    print(a)
    

