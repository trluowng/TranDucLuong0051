import threading
import requests

def make_http_request(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

def main():
    # Danh sách các URL cần thực hiện yêu cầu
    urls = [
        "https://www.example.com",
        "https://www.example.org",
        "https://www.example.net"
    ]

    # Tạo và bắt đầu một luồng cho mỗi URL
    threads = []
    for url in urls:
        thread = threading.Thread(target=make_http_request, args=(url,))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
