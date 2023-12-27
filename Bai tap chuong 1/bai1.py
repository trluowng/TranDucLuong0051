class hcn:
    def __init__(self,dai,rong):
        self.dai=dai
        self.rong=rong
    def chuvihcn(self):
        return 2*(self.dai +self.rong)
    def dientichhcn(self):
        return self.dai * self.rong
    def indulieu(self):
        print("do dai là:",self.dai)
        print (" chieu rong là:",self.rong)
        print("chu vi la:",self.chuvihcn())
        print("dien tich HCN la:",self.dientichhcn())
dai=float(input("nhập chiều dài của hình chữ nhật: "))
rong=float(input("nhập chiều rông của hình chủ nhật: "))
hcn=hcn(dai,rong)
hcn.indulieu()