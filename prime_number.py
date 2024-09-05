a = int(input("aの値を入力: "))
i=2
while i<a:
    if a%i==0:
        print("素数でない")
        break
    i+=1
if i>=a:
    print("素数である")

b = int(input("bの値を入力: "))
i=2
while i<b:
    if b%i==0:
        print("素数でない")
        break
    i+=1
if i>=b:
    print("素数である")