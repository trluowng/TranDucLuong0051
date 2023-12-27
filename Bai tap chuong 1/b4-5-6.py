class Stack:
    def __init__(self,suc_chua):
        self.suc_chua = suc_chua # sức chứa tối đa
        self.data = []  #mảng float được cấp phát động
        self.top = -1 # vị trí đỉnh của ngăn xếp, ban đầu = -1
    def push(self,phantu):
        if not self.isFull():
            self.top += 1
            self.data.append(phantu)
            print(f'Đã đẩy phần tử {phantu} vào ngăn xếp.')
        else:
            print("Đã đầy phần tử. Không thể thêm.")
        
    def pop(self):
        if not self.isEmpty():
            popped_phantu = self.data.pop()
            self.top -= 1
            return popped_phantu
        else:
            print("Không có phần tử trong stack. Không thể lấy phần tử.")
            return None
            
    def isEmpty(self):
        return self.top == - 1
    
    def isFull(self):
        return self.top == self.suc_chua - 1
    
    def count(self):
        return self.top + 1
    
    def printStack(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp:")
            for phantu in self.data:
                print(phantu)


    def __del__(self):
        del self.data
suc_chua = int(input("Nhập sức chứa tối đa:"))
stack = Stack(suc_chua)
    
while True:
    print("Chọn thao tác:")
    print("1. Push (thêm phần tử vào ngăn xếp)")
    print("2. Pop (lấy phần tử ra khỏi ngăn xếp)")
    print("3. Kiểm tra ngăn xếp rỗng")
    print("4. Kiểm tra ngăn xếp đầy")
    print("5. Count (số phần tử trên ngăn xếp)")
    print("6. In ra nội dung ngăn xếp.")
    print("7. Thoát")

    choice = int(input("Nhập lựa chọn:"))
    
    if choice == 1:
        phantu = float(input("Nhập phần tử muốn đẩy vào ngăn xếp:"))
        stack.push(phantu)
        
    elif choice == 2:
        popped_phantu = stack.pop()
        if popped_phantu is not None:
            print(f'Phần tử lấy ra:{popped_phantu}')

    elif choice == 3:
        if stack.isEmpty():
            print("Ngăn xếp không rỗng.")
        else:
            print("Ngăn xếp không rỗng.")

    elif choice == 4: 
        if stack.isFull():
            print("Ngăn xếp đầy.")
        else:
            print("Ngăn xếp không đầy.")

    elif choice == 5:
        print(f'Số phần tử trên ngăn xếp {stack.count()}')

    elif choice == 6:
        stack.printStack()

    elif choice == 7:
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
del stack





