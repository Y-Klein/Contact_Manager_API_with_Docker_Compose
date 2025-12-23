import mysql.connector
import os
from  dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional


load_dotenv()
connection =  mysql.connector.connect(
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME")
)


class Contact(BaseModel):
    id:Optional[int]= None
    first_name:str
    last_name:str
    phone_number:str


def get_dict(contact:Contact):
    return {"id":contact.id,"first name":contact.first_name,"last name":contact.last_name,"phone number":contact.phone_number}

def create_contact(contact:Contact):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s,%s,%s);",
                       [contact.first_name,contact.last_name,contact.phone_number])
        cursor.execute("SELECT id FROM contacts WHERE first_name = %s ",[contact.first_name])
        print(cursor.fetchall()[0][0])
        connection.commit()


def get_all_contacts():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM contacts")
        all_contacts = cursor.fetchall()
        for my_object in all_contacts:
            print(Contact(id=my_object[0],first_name=my_object[1],last_name=my_object[2],phone_number=my_object[3]))






a = Contact(first_name="hhh",last_name="bbb",phone_number="6660")
# create_contact(a)
get_all_contacts()
connection.close()