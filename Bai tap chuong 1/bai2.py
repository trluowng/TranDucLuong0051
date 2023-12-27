#Tạo lớp thí sinh quản lí điểm thi
class thisinh:
    def __init__(self,ho_ten,diem_toan,diem_ly,diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    #Hàm tính tổng điểm
    def tinh_diem(self):
        return self.diem_toan + self.diem_hoa + self.diem_ly
    #Hàm in thông tin họ tên và điểm
    def in_thong_tin(self):
        print(f'Họ và tên {self.ho_ten}')
        print(f'Điểm toán: {self.diem_toan}')
        print(f'Điểm lý: {self.diem_ly}')
        print(f'Điểm hoá: {self.diem_hoa}')
        print(f'Tổng Điểm:{self.tinh_diem()}')

#Hàm nhập thông tin của thí sinh
def nhap_thong_tin_ts():
    ho_ten = input("Nhập họ tên: ")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))
    return thisinh(ho_ten, diem_toan, diem_ly, diem_hoa)

#Hàm liệt kê danh sách thí sinh
def ds_trung_tuyen(ds_thi_sinh):
    diemchuan = 20
    danhsach = [ts for ts in ds_thi_sinh if ts.tinh_diem() >=diemchuan]
    return sorted(danhsach, key=lambda a: a.tinh_diem(), reverse=True)

#Hàm in danh sách thí sinh trúng tuyển
def in_ds(danhsach):
    print("danh sách trúng tuyển:")
    for i, ts in enumerate(danhsach,1):
        print(f'thí sinh {i}:')
        ts.in_thong_tin()

#Chương trình chính
if __name__ == '__main__':
    so_thi_sinh = int(input("Nhập số lượng thí sinh:"))
    danh_sach_thi_sinh = []
    for i in range(so_thi_sinh):
        print(f'Nhập thông tin thí sinh{i+1}')
        ts = nhap_thong_tin_ts()
        danh_sach_thi_sinh.append(ts)
    
    danhsach = ds_trung_tuyen(danh_sach_thi_sinh)
    in_ds(danhsach)