Chatbot v0.1

## A question based chatbot that tries to predict an answer based on candidate labels

How to set up the project:

1. If needed To Generate the requirements file `pip freeze > requirements.txt`
2. Install the requirements `pip install -r requirements.txt`
3. Generate an API key and update the `.env` file
4. Add the same API key to the client side request header as `x-api-key`


## Logging
Currently, the log output is a json file on the root of this project todo to make it modular and add logic to log in to a database to gather data.

## RateLimit
- added rate limiter to the endpoint