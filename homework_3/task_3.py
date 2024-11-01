import requests
from bs4 import BeautifulSoup

url = "https://www.interfax.ru/"

response = requests.get(url)
response.raise_for_status()
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.string)

paragraphs = soup.findAll('a', tabindex='4')
for p in paragraphs:
    print(p.text)
