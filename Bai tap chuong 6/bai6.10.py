import threading
import random

def max_value(list):
    max_value = max(list)
    print(f"GTLN in {list} là {max_value}")

def main():
    n = 9
    lst = [random.randint(0, 100) for i in range(n)]
    print(f"List ngẫu nhiên: {lst}")
    threads = []
    for i in range(3):
        start = i * n // 3
        end = (i + 1) * n // 3
        t = threading.Thread(target=max_value, args=(lst[start:end],))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
