Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... from bs4 import BeautifulSoup
... import csv
... 
... def fetch_html(url):
...     response = requests.get(url)
...     if response.status_code == 200:
...         return response.text
...     else:
...         print("Failed to fetch HTML:", response.status_code)
...         return None
... 
... def parse_html(html):
...     soup = BeautifulSoup(html, 'html.parser')
...     # Use BeautifulSoup to parse the HTML and extract the data you need
...     # Example:
...     # product_titles = soup.find_all('h3', class_='product-title')
...     # for title in product_titles:
...     #     print(title.text)
... 
... def save_to_csv(data):
...     # Example: Save data to a CSV file
...     with open('walmart_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
...         writer = csv.writer(csvfile)
...         # Write headers if needed
...         # writer.writerow(['Product Name', 'Price'])
...         # Write data
...         # for row in data:
...         #     writer.writerow(row)
... 
... def main():
...     url = 'https://www.walmart.com/'
...     html = fetch_html(url)
...     if html:
...         data = parse_html(html)
...         save_to_csv(data)
... 
if __name__ == "__main__":
    main()
