import requests
from datetime import datetime, timedelta

url = "https://api.remotar.com.br/jobs?search=&tagId=10&categoryId=4,7,15,13,14"
response = requests.get(url)

data = response.json()
jobs_list = data.get("data", [])

for job in jobs_list:
    creation_date = job.get("createdAt")
    current_date = datetime.now()

    time_difference = current_date - creation_date
        
    if time_difference < timedelta(days=10):
        title = job.get("title")
        description = job.get("descrption")
        link = job.get("externalLink")

    
