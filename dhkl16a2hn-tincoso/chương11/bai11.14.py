dict1={'Minh':'0989741258',\
    'Hạnh':"0903852147",\
        'Bình':"0913753951",\
            'An':'0933753654'}
print('Vui lòng chọn chức năng:')
print('1:Tìm sdt')
print("2:Thêm sdt")
n=int(input('Nhập cú pháp:'))
def chon_chuc_nang(n):
     if n==1:
         name=input('Vui lòng nhập tên người muốn tìm:')
         print('SĐT của',name,'là',dict1[name])
     if n==2:
         print("NHẬP END ĐỂ KẾT THÚC!")  
         while True:
             a=input('Nhập tên:')
             b=input('Nhập sđt:')
             if a and b =='END':
                 break
             dict1.update({a:b})
     print('BẠN CÓ XÁC NHẬN BẢN CẬP NHẬT NÀY KHÔNG?')
     print('1:Có')
     print('2:Không')
     while True:
         c=int(input('Nhập cú pháp:'))
         if c==1:
             print(dict1)
         elif c==2:
            break
     return
chon_chuc_nang(n)
        
        