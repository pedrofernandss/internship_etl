import requests
from bs4 import BeautifulSoup

url = "https://api.remotar.com.br/jobs?search=&tagId=10&categoryId=4,7,15,13,14"
response = requests.get(url)

data = response.json()
jobs_list = data.get("data", [])

for job in jobs_list:
    title = job.get("title")
    description = job.get("descrption")
    link = job.get("externalLink")

    print(title)
    print(link)
    print("###########")
