"# Contact_Manager_API_with_Docker_Compose" 
In the data_interactor file:
The contact class inherits from a model base with the option to leave the ID only for the HashQ to complete it
Includes a function to convert the self to a dictionary

The create_contact function receives an instance of a contact, converts it to a dictionary, adds the contact to the database and returns the ID of the location with that phone number (which must be unique)

The get_all_contacts function retrieves the entire table from the database and for each row converts it to a dictionary and adds it to the list, finally returns the list

The update_contact function receives the IDs that want to change the location that I want to change and the new content that will be there, launches an appropriate command and returns TRUE

The delete_contact function receives an ID and launches a command that deletes the row at the location of the ID I received and returns TRUE

In the main file:

4 endpoints of the Paste API that use functions from the file data_interactor with error management As required

Docker File :
Builds an image that uses Python with the appropriate libraries and runs the software upon startup

Docker Compose :
Two services and a volume
1 :
Uses a SQL image with variables from the ENV Running on 3306:3306 Connected to a volume that contains the first run of the data and the data in the advice and also has a health check

2:
My application built from the Docker File
With environment variables adjusted to the runtime environment Running on port 8000:8000 and waiting for the health check of the Div

Run command from the main folder
docker compose up --buld -d

- Example curl commands to check each endpoint

