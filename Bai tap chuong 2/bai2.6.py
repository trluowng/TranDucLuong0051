import requests
import xml.etree.ElementTree as ET
import csv

def download_rss_feed(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    news_items = []
    for item in root.findall('.//item'):
        news_item = {}
        for child in item:
            news_item[child.tag] = child.text
        news_items.append(news_item)

    return news_items

def save_to_csv(news_items, csv_file):
    fieldnames = ['title', 'link', 'description', 'pubDate']
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(news_items)

# Thay đổi đường dẫn và tên tệp của bạn
rss_url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
xml_file = 'rss_feed.xml'
csv_file = 'news_items.csv'

# Tải nguồn cấp RSS từ URL và lưu thành tệp XML
download_rss_feed(rss_url, xml_file)

# Phân tích cú pháp tệp XML và lưu tin tức dưới dạng danh sách từ điển
news_items = parse_xml(xml_file)

# Lưu các mục tin tức vào tệp CSV
save_to_csv(news_items, csv_file)
