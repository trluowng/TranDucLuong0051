import threading
import random

# Hàm tính tổng của một list con
def calculate_partial_sum(sublist, result_lock, result):
    partial_sum = sum(sublist)
    with result_lock:
        result[0] += partial_sum

# Người dùng nhập số lượng phần tử của list và số lượng thread
n = int(input("Nhập số lượng phần tử của list: "))
num_threads = int(input("Nhập số lượng thread: "))

# Tạo một list ngẫu nhiên với giá trị từ 0 đến 10
my_list = [random.randint(0, 10) for _ in range(n)]

# In list vừa tạo
print("List:", my_list)

# Tính số phần tử trong mỗi list con
elements_per_thread = len(my_list) // num_threads

# Khóa để đồng bộ hóa kết quả
result_lock = threading.Lock()

# Biến lưu kết quả
result = [0]

# Tạo và bắt đầu các luồng
threads = []
for i in range(num_threads):
    start_index = i * elements_per_thread
    end_index = start_index + elements_per_thread
    sublist = my_list[start_index:end_index]

    thread = threading.Thread(target=calculate_partial_sum, args=(sublist, result_lock, result))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

# In kết quả
print("Tổng các phần tử trong list:", result[0])
