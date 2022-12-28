i=2
n=int(input('nhập số:'))
while i<n:
    if n%i==0:
        a="là số nguyên tố!"
    else:
        a="ko là số nguyên tố!"
    break
print(n,a)
i+=1    

      