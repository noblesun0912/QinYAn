##  scripts learned form course,with  some modifiction
import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch HTML:", response.status_code)
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

def save_to_csv(data):
    with open('walmart_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

def main():
    url = 'https://www.walmart.com/'
    html = fetch_html(url)
    if html:
        data = parse_html(html)
        save_to_csv(data)

if __name__ == "__main__":
    main()
