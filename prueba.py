import requests
import json
URL = 'https://api.chucknorris.io/jokes/random'
ids = []
run = True
limit_consult = 25
while run:
    re = requests.get(URL)
    if re.status_code == 200:
        data = re.json()
        if data["id"] not in ids:
            ids.append(data["id"])
    if len(ids) == limit_consult:
        run = False

values_originals = len(ids)
delete_duplicates = len(list(set(ids)))
print(f'no duplicate values {values_originals == delete_duplicates}')
print(f"array_ids: {ids}")


