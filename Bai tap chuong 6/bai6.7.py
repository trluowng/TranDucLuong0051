import threading
import time

def worker(name, interval):
    print(f"Starting {name}")
    while True:
        print(f"{name}: Web {time.strftime('%b %d %H:%M:%S %Y', time.localtime())}")
        time.sleep(interval)
    print(f"Exiting {name}")

def main():
    print("Starting Main Thread")

    # Tạo và bắt đầu các luồng
    google_thread = threading.Thread(target=worker, args=("Google", 1))
    yahoo_thread = threading.Thread(target=worker, args=("Yahoo", 2))
    facebook_thread = threading.Thread(target=worker, args=("Facebook", 3))

    google_thread.start()
    yahoo_thread.start()
    facebook_thread.start()

    # Chờ một khoảng thời gian (ví dụ: 05 giây) 
    time.sleep(5)

    # Dừng các luồng
    google_thread.join()
    yahoo_thread.join()
    facebook_thread.join()

    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
