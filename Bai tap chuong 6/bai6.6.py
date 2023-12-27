import threading
import random

# Ngưỡng nhất định cho các số chẵn và lẻ
threshold = random.randint(10, 30)

# Khóa để đồng bộ hóa in ra
print_lock = threading.Lock()

def print_even_numbers():
    with print_lock:
        for i in range(0, threshold+1, 2):
            print(f"Even Thread: {i}")

def print_odd_numbers():
    with print_lock:
        for i in range(1, threshold+1, 2):
            print(f"Odd Thread: {i}")

def main():
    # Tạo và bắt đầu luồng cho số chẵn
    even_thread = threading.Thread(target=print_even_numbers)
    even_thread.start()

    # Tạo và bắt đầu luồng cho số lẻ
    odd_thread = threading.Thread(target=print_odd_numbers)
    odd_thread.start()

    # Chờ cả hai luồng hoàn thành
    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()
