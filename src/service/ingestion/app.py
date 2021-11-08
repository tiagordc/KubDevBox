import logging
from fastapi import FastAPI

print('Starting ingestion API')

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
