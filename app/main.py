from fastapi import FastAPI
from data_interactor import *

app = FastAPI()


@app.get("/contacts")
def get_all():
    try:
        return get_all_contacts()
    except:
        raise TypeError("Something went wrong")

@app.post("/contacts")
def create(contact:Contact):
    try:
        return create_contact(contact)
    except:
        raise TypeError("Something went wrong")

@app.put("/contacts/{id}")
def update(my_id,change_place,new_value):
    try:
        return update_contact(my_id,change_place,new_value)
    except:
        raise TypeError("Something went wrong")

@app.delete("/contacts/{id}")
def delete(my_id):
    try:
        return delete_contact(my_id)
    except:
        raise TypeError("Something went wrong")


