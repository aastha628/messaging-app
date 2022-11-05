-- creating database for messaging app
CREATE DATABASE messaging_app;

-- connect to DATABASE - \c messaging_app

--creating user and giving it access to all the tables in the DATABASE 
CREATE USER mapp_user WITH ENCRYPTED PASSWORD 'some_secure_key';

GRANT ALL PRIVILEGES ON DATABASE messaging_app TO mapp_user;

ALTER DEFAULT PRIVILEGES
IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO mapp_user;
ALTER DEFAULT PRIVILEGES
IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO mapp_user;

--creating database tables 

CREATE TABLE queries(
    q_id SERIAL PRIMARY KEY ,
    user_id int NOT NULL,
    created_at TIMESTAMP NOT null,
    query TEXT not NULL
);

-- load all csv data into the queries TABLE 
-- \copy queries(user_id,created_at,query) from 'path/to/csvfile'  delimiter ',' csv header

CREATE TABLE agents(
    agent_id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    PASSWORD TEXT NOT NULL 
);

CREATE TABLE responses(
    r_id SERIAL PRIMARY KEY,
    agent_id INT REFERENCES agents(agent_id) ON DELETE SET NULL,
    query_id INT UNIQUE REFERENCES queries(q_id) ON DELETE CASCADE ,
    response TEXT NOT NULL 
);





