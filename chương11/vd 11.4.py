print("IF YOU WANNA STOP, PLEASE ENTER THE 'END'")
list=[]
while True:
    n=input('Nhập số:')
    if n=='END':
        break
    list.append(int(n))
print(list)
