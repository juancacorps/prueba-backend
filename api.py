import asyncio
import aiohttp

from fastapi import FastAPI
app = FastAPI()

async def get_list_ids():
    """
        Crea tareas asincronas con (N) cantidad. mandando a llamar la funcion:
        get_id_chucknorris. se crea la variable ids con tipo set para que no almancene
        ids repetidos.
    """
    range_ids = 25
    ids = set()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(range_ids):
            task = asyncio.ensure_future(get_id_chucknorris(session))
            tasks.append(task)
        completed_tasks, _ = await asyncio.wait(tasks)
        for task in completed_tasks:
            new_id = task.result()
            ids.add(new_id)    
    return ids

async def get_id_chucknorris(session):
    """
        Utilizando aiohttp se crea la petición para traer la informacion
        de manera asincrona.
    """
    async with session.get('https://api.chucknorris.io/jokes/random') as response:
        if response.status == 200:
            data = await response.json()
            return data["id"]
        else:
            return False

@app.get("/ids")
async def get_ids():
    ids = await get_list_ids()
    return {"ids": list(ids)}

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.main())
