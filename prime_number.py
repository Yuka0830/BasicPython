a = int(input("aの値を入力: "))
<<<<<<< HEAD
=======
i=2
while i<a:
    if a%i==0:
        print("素数でない")
        break
    i+=1
if i>=a:
    print("素数である")

>>>>>>> parent of ce64cb7 (Python入門の解答)
b = int(input("bの値を入力: "))

def prime(n):
 if type(n)!=int or n<1:
   return "error"
 elif n==1:
   return "False"
 elif n<=3:
   return "True"
 elif n%2==0:
   return "False"
 else:
   for i in range(3, int(n**0.5)+1,2):
        if n%i==0:
          return "False"
 return "True"
        
print(prime(a))
print(prime(b))