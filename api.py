from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()
URL = 'https://api.chucknorris.io/jokes/random'

@app.get('/')
def read_ids():
    """API GET requests"""
    data = get_chucknorris_ids(URL, 25)
    return {"ids": data}

def get_chucknorris_ids(URL, limit_consult):
    """
    Función para obtener los ids de la URL donde devolvera los ids que no se repitan
    parms: URl = URL a consumir, limit_consult = limite de ids que traera el array
    return: array de ids distintos de la API
    """
    ids = []
    run = True
    limit_consult = limit_consult
    while run:
        re = requests.get(URL)
        if re.status_code == 200:
            data = re.json()
            if data["id"] not in ids:
                ids.append(data["id"])
        if len(ids) == limit_consult:
            run = False
    return ids

if __name__ == "__main__":
    uvicorn.run("api:app", port=5000)