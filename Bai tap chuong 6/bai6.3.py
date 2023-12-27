import threading

# Khóa để khi in ra 2 luồng không bị lộn xộn
print_lock = threading.Lock()

def print_even_numbers():
    with print_lock:
        print("Các số chẵn:")
        for i in range(30, 51, 2):
            print(i)

def print_odd_numbers():
    with print_lock:
        print("Các số lẻ:")
        for i in range(31, 51, 2):
            print(i)

# Tạo và bắt đầu luồng cho số chẵn
even_thread = threading.Thread(target=print_even_numbers)
even_thread.start()

# Tạo và bắt đầu luồng cho số lẻ
odd_thread = threading.Thread(target=print_odd_numbers)
odd_thread.start()

# Chờ cả hai luồng hoàn thành
even_thread.join()
odd_thread.join()

print("Kết thúc chương trình.")
