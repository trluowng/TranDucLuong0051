# kiẻm tra 1 số có p là số ngtố
n = int(input("Nhập số n = "))
flag = True 
if n < 2 :
  print(n, "không nguyên tố !!!")
else:
    for i in range(2,int(n/2)):
        if n%i == 0:
            flag = False
            break
    if flag :
         print(n,"là số nguyên tố ")
    else:
        print(n, "k phải là số nguyên tố !!!")
