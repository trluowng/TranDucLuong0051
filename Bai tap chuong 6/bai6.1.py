import threading

def print_thread_name():
    # Hàm in tên của luồng
    thread_name = threading.current_thread().name
    print(f"Hello from thread {thread_name}")

# Tạo và bắt đầu 3 luồng
for i in range(3):
    thread = threading.Thread(target=print_thread_name)
    thread.start()

# Chờ tất cả các luồng hoàn thành
main_thread = threading.current_thread()
for thread in threading.enumerate():
    if thread is not main_thread:
        thread.join()
