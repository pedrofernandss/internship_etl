import requests
from datetime import datetime, timedelta

url = "https://api.remotar.com.br/jobs?search=&tagId=10&categoryId=4,7,15,13,14"
response = requests.get(url)

data = response.json()
jobs_list = data.get("data", [])

for job in jobs_list:
    creation_date = job.get("createdAt")
    creation_date = datetime.fromisoformat(creation_date)
    current_date = datetime.now(creation_date.tzinfo)

    time_difference = current_date - creation_date
        
    if time_difference < timedelta(days=10):
        title = job.get("title")
        description = job.get("description")       
        link = job.get("externalLink")

        company = job.get("company")
        company_name = company.get("name")

        print(f"""
              A empresa {company_name} anunciou uma nova vaga para {title}! ✨✨

                    🧑‍🎓 Nível: Estágio
                    📍 Localidade: Remoto

                    Descrição da vaga:

                    {description}

                    
                    🌐 Link: {link}

                    Caso decida se inscrever, não esqueça de personalizar seu currículo! 😉

                    Que a sorte esteja sempre a seu favor! 🤗
              """)

    
