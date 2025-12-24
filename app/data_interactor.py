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


    def get_dict(self):
        return {"id":self.id,"first name":self.first_name,"last name":self.last_name,"phone number":self.phone_number}

def create_contact(contact:Contact):
    contact = Contact.get_dict(contact)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s,%s,%s);",
                       [contact["first name"],contact["last name"],contact["phone number"]])
        cursor.execute("SELECT id FROM contacts WHERE phone_number = %s ",[contact["phone number"]])
        result =  cursor.fetchall()[0][0]
        connection.commit()
        return result


def get_all_contacts():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM contacts")
        all_contacts = cursor.fetchall()
        result = []
        for my_object in all_contacts:
            result.append(Contact.get_dict(Contact(id=my_object[0],first_name=my_object[1],last_name=my_object[2],phone_number=my_object[3])))
        return result

def update_contact(my_id,change_place,new_value):
    with connection.cursor() as cursor:
        cursor.execute(f"UPDATE contacts SET {change_place} = {new_value} WHERE id = {my_id}")
        connection.commit()
        return True

def delete_contact(my_id):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM contacts WHERE id = {my_id}")
        connection.commit()
        return True



# a = Contact(first_name="hhh",last_name="bbb",phone_number="6660")
# print(create_contact(a))
# print(get_all_contacts())
# print(update_contact(3,'phone_number' ,"6670" ))
# print(delete_contact(3))
# connection.close()