from math import sin,pi
a=0
b=pi / 2
N=100
h=(b-a) / N
S=0
for i in range(N):
    S+=sin(a+i*h)+sin(a+(i+1)*h)
S*=h/2
print(S)
