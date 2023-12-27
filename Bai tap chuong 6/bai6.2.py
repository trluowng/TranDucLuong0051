import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename} from {url}")
    else:
        print(f"Failed to download {filename} from {url}")

# Danh sách các URL cần tải xuống
urls = [
    "https://example.com/file1.txt",
    "https://example.com/file2.txt",
    "https://example.com/file3.txt"
]

# Tạo và bắt đầu một luồng cho mỗi URL
threads = []
for i, url in enumerate(urls):
    filename = f"file_{i+1}.txt"
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()
