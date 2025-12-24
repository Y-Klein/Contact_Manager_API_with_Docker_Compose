from fastapi import FastAPI
from app.data_interactor import *

app = FastAPI()


@app.get("/contacts")
def ger_all():
    return get_all_contacts()

@app.post("/contacts")
def create(contact:Contact):
    return create_contact(contact)

@app.put("/contacts/{id}")
def update(my_id,change_place,new_value):
    return update_contact(my_id,change_place,new_value)

@app.delete("/contacts/{id}")
def delete(my_id):
    return delete_contact(my_id)


