class Date:
    def __init__(self, day=1, month=1, year=2022):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày: {self.day}, Tháng: {self.month}, Năm: {self.year}")

    def next(self):
        # Kiểm tra số ngày của từng tháng
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30 ,31 ,30 ,31]

        # Kiểm tra năm nhuận
        if (self.year % 4 ==0 and self.year %100 !=0) or (self.year %400 ==0):
            days_in_month[1] =29

        # Kiểm tra ngày cuối cùng của tháng hiện tại
        last_day_of_month = days_in_month[self.month -1]

         # Tăng giá trị ngày lên một đơn vị và kiểm tra xem có phải là ngày đầu tiên của tháng mới không
         # Nếu có thì tăng giá trị tháng lên một đơn vị và thiết lập lại giá trị ngày bằng một.
         # Nếu là cuối năm (tháng là 12), thiết lập lại giá trị tháng bằnig một và tăng giá trị năm lên một đơn vị.
        if self.day == last_day_of_month:
            if self.month == 12:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
            self.day = 1
        else:
            self.day += 1

# Sử dụng lớp Date để tạo một đối tượng và thực hiện các phương thức

# Tạo một đối tượng Date với giá trị mặc định (ngày: 1, tháng: 1, năm:2022)
date = Date()

# In thông tin về ngày ra màn hình
date.display() # Output: Ngày: 1, Tháng: 1, Năm:2022

# Tính ngày tiếp theo và in thông tin mới ra màn hình
date.next()
date.display() # Output: Ngày:2, Tháng:1, Năm:2022
