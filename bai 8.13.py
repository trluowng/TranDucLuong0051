import math
n= int(input('nhap so n: '))
i=1; a=0; b=0; c=1; d=0; e=0; f=0; u=1
while(i<=n):
    if(i%2==1): a= a +i
    if(i%2==0): b = b+ i
    c=c*i
    if(i%3==0): d=d*i
    while(u<i):
        u+=1
        if(i%u!=0): e=e+i
    f=f + 1/(math.pow(-1,i+1)*i)
    i+=1
print('A=',a,'; B=',b,'; C=',c,'; D=',d,'; E=',e,'; F=',f)