import random,math

a=int(input("a の値を入力: "))
b=int(input("b の値を入力: "))

def euclid(a,b):
  while a!=b:
    if a==0:
      return b
    elif b==0:
      return a
    else:
      a,b=b,a%b
  #if a==b:
  return a

def euclid2(a,b):
  return euclid(a,b)==1

print(euclid(a,b))
print(euclid2(a,b))

def extra(pairs,min,max):
  count=0
  for i in range(pairs):
    r1=random.randint(min,max)
    r2=random.randint(min,max)
    if euclid2(r1,r2)==True:
      count+=1
  return count/pairs

print(extra(100000,1,10000),6/(math.pi**2))
