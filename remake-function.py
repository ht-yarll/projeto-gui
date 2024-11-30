import time
import os
from datetime import datetime, timedelta


import requests
import pandas as pd

os.makedirs('dados/vagas', exist_ok = True) 

def request_data(labels):
        print(labels)
        responses = []

        with requests.Session() as session:
            for label in labels:
                print(f"Requesting for '{label}'...")
                url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

                try:
                    request = session.get(url)
                    response = request.json().get("data", [])
                    responses.append(response)
                    pd.DataFrame(request.json().get("data", [])).to_json( 
                        f"dados/vagas/{label}.json", index=False
                    )

                    print(f"Found {len(response)} results for '{label}'...")
                    time.sleep(0.5)

                except Exception as e:
                    print(e)

        return 

request_data(['dados'])