from fastapi import FastAPI
from data_interactor import *

app = FastAPI()


@app.get("/contacts")
def ger_all():
    get_all_contacts()


