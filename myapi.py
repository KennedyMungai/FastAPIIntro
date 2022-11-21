from fastapi import FastAPI

app = FastAPI()

def index():
    return {"name":"First Data"}