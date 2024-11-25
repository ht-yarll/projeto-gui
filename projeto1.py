import time
import os
from datetime import datetime, timedelta


import requests
import pandas as pd

os.makedirs('dados/vagas', exist_ok = True)

class GupyScraper:
    def __init__(self, search_labels):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)"
        }
        self.search_labels = search_labels

        self.ids = set()

    def request_data(self, labels):
        print(labels)
        responses = []

        with requests.Session() as session:
            for label in labels:
                print(f"Requesting for '{label}'...")
                url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

                try:
                    request = session.get(url, headers=self.headers)
                    response = request.json().get("data", [])
                    responses.append(response)
                    #nesta parte creio que possa haver melhora
                    #já que estou passando json para .json, não sei se precisa do "to_json"
                    pd.DataFrame(request.json().get("data", [])).to_json( 
                        f"dados/vagas/{label}.json", index=False
                    )

                    print(f"Found {len(response)} results for '{label}'...")
                    time.sleep(0.5)

                except Exception as e:
                    print(e)

        return 
    
scraper = GupyScraper(["developer", 'designer'])   #vou tentar passar um modo para fazer meio que um "programa"
scraper.request_data(scraper.search_labels)        # onde pode-se inserir o nome da vaga. Tentar fazeer até o fds.