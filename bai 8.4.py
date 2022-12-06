
#sử dụng công thức heron để tính diện tích tam giác 
import math
print("nhập số đo các cạnh tam giác")
a=int(input("nhập số:"))
b=int(input("nhập số:"))
c=int(input("nhập số:"))
p=(a+b+c)/2
print("nửa chu vi hình tam giác là",p)
S=math.sqrt ((p*(p-a)*(p-b)*(p-c)))
print("diện tích hình tam giác là",S)
