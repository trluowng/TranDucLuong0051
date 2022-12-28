#viết hàm giai thừa của thuật giải đệ quy
def giaithua(n):
    if n==1:
         return 1
    else:
          return n*giaithua(n-1)
print("giai thua cua",5,"la",giaithua(5),'\n')
    