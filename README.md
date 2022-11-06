# Messaging App

This is the basic feature of messaging app. App that allows agents to fetch the unanswered messages and submit their response. Few cases handled here -
* Only agents that are registered with us can answer.
* Each query can be answered only once

## Routes

1. Create a user 
```
POST - /register
{
    "email":{string},
    "password":{string}
}
```
2. Fetch message
```
GET - /message?agent_id={int}
```
3. Submit response
```
POST - /response
{
    "q_id":{int},
    "agent_id":{int},
    "response":{string}
}
```

## Steps to run the application

1. Clone the project
2. `cd` into the project directory
3. Create and run the python environment (on linux)
```
python -m venv env
source env/bin/activate
```
4. Install required libraries 
```
pip install -r requirements.txt
```
5. Setup your PostgreSQL database using all the commands given in [database.sql](/database.sql)
6. Run the server `uvicorn server:app --reload`