from math import sin,pi,exp,sqrt
def integral(f,a=0,b=1,n=100):
  h=(b-a)/n
  S=0
  for i in range(n):
    S+=(f(a+i*h)+f(a+(i+1)*h))
  S*=(h/2)
  return S
print(integral(sin,0,pi/2,50))
def f1(x):
  return 4/(1+x**2)
print(integral(f1,0,1,100))
def f2(x):
  return sqrt(pi)*exp(-x**2)
print(integral(f2,-100,100,1000))