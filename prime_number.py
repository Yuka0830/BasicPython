a = input("aの値を入力: ")
b = input("bの値を入力: ")

def prime(n):
 if not isinstance(n, int):
   raise TypeError("整数を入力してください")
 if n<1:
   raise ValueError("1より大きい整数を入力してください")
 elif n==1:
   return False
 elif n<=3:
   return True
 elif n%2==0:
   return False
 else:
   for i in range(3, int(n**0.5)+1,2):
        if n%i==0:
          return False
 return True
        
print(prime(a))
print(prime(b))