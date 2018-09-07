# Microservice with Python Django

This is a simple example microservice written in Python Django, with a `GET /` which uses simple session authentication, and hits the Sinatra service to log a view event and then hits the Flask service to proxy the response back to the user. Also, it has a `POST/GET /login` endpoint for login purposes.
