#tính cước xe taxi
n1=eval(input("số km khi đi xe 4 chỗ:"))
n2=eval(input("số km khi đi xe 7 chỗ :"))
n3=eval(input("thời gian chờ(p):"))
if (n3<=5):
    print("tiền chờ miễn phí!")
else:
     n4=(n3-5)*800
     print("số tiền chờ bạn phải trả thêm là",n4)
if n1<=0.8:
     print("total money case 4:",(n1*11000)+n4)
elif n1<=20:
     print("total money case 4:",(n1*12100)+n4)
else:
     print("total money case 4:",(n1*10000)+n4)
if n2<=0.8:
    print("total money case 7:",(n2*13000)+n4)
elif n2<=30:
    print("total money case 7:",(n2*14100)+n4)
else:
    print("total money case 7:",(n2*12000)+n4)        