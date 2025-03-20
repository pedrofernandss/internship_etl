import requests
from bs4 import BeautifulSoup

url = "https://api.remotar.com.br/jobs?search=&tagId=10,17&categoryId=4,7,15,13,14"
response = requests.get(url)
print(response.text)