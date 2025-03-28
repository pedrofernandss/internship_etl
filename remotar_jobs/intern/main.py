from typing import List
import requests
from datetime import datetime, timedelta

from database.main import save_data

def request_jobs_list():
    url = "https://api.remotar.com.br/jobs?search=&tagId=10&categoryId=4,7,15,13,14"
    response = requests.get(url)

    return response

def is_recent_job(creation_date: str) -> bool:
    creation_date = datetime.fromisoformat(creation_date)
    current_date = datetime.now(creation_date.tzinfo)

    time_difference = current_date - creation_date
        
    if time_difference < timedelta(days=2):
        return True
    else: 
        return False
    
def clean_data():
    data = request_jobs_list().json()
    jobs_list = data.get("data", [])

    recent_jobs = []

    for job in jobs_list:
        creation_date = job.get("createdAt")
            
        if is_recent_job(creation_date):
            job_data = {
                "id": job.get(""),
                "title": job.get("title"),       
                "link": job.get("externalLink"),
                "company_name": job.get("company", {}).get("name"),
                "created_at": creation_date
            }

        save_data(job_data)
        recent_jobs.append(job_data)

    return recent_jobs