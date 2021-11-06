import logging
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    logging.info('Get root')
    return {"Hello": "World"}
