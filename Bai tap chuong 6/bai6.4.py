import threading
import math
import random

def calculate_factorial(number):
    result = math.factorial(number)
    print(f"Giai thừa của {number} là {result}")

def main():
    # Chọn số ngẫu nhiên từ 1 đến 10
    number_to_calculate = random.randint(1, 10)

    # Tạo và bắt đầu một luồng để tính giai thừa
    factorial_thread = threading.Thread(target=calculate_factorial, args=(number_to_calculate,))
    factorial_thread.start()

    # Chờ luồng tính giai thừa hoàn thành
    factorial_thread.join()

if __name__ == "__main__":
    main()
