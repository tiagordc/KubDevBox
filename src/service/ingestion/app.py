import logging
from fastapi import FastAPI

logging.info('Starting ingestion API')

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
