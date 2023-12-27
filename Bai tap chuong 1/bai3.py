class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def kiem_tra_hop_le(self):
        if self.mau == 0:
            return False
        else:
            return True
    def nhap_phan_so(self):
        while not self.kiem_tra_hop_le():
            print("Mẫu số không thể bằng 0, hãy nhập lại mẫu số")
            self.mau = int(input("Nhap mau so: "))
    def in_phan_so(self):
        print("phấn số là: {}/{}".format(self.tu, self.mau))
tu = int(input("Nhap tu so: "))
mau = int(input("Nhap mau so: "))
PS=PS(tu,mau)
PS.in_phan_so()
