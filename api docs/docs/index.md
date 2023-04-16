
# Quote Engine API Documentation
The Quote Engine API is a fast and reliable API that generates random motivational quotes. This API is built using FastAPI, a high-performance web framework for building APIs with Python.

With the Quote Engine API, you can easily integrate motivational quotes into your application or website, providing your users with daily inspiration and motivation. Whether you're building a personal development app, a fitness tracker, or a productivity tool, the Quote Engine API can help you enhance your user experience.

This documentation provides an overview of the Quote Engine API, including how to access the API, the available endpoints, and how to use the API in your application. Let's get started!


## Getting Started
To start using the Quote Engine API, follow these steps: <br/>
1. Clone the repository to your local machine using the following command:
```bash
    $ git clone https://github.com/njeru-codes/The-Quote-Engine
```
2.Create a .env file in the root directory of the project and add the following variables:
```json
    mongo_uri=""
    secret_key=""
```
The mongo_uri variable should be set to the URI of your MongoDB database. The secret_key variable is a random string used to create JWT tokens. You can generate a random string using the following command:
```bash 
    $ openssl rand -hex 32
```
3.Install the required dependencies using the following command:
```bash
    $ pip install -r requirements.txt
```
4.Start the server using the following command:
```bash
    $ uvicorn app.main:app
```
5.To view the API documentation, navigate to http://localhost:8000/docs in your web browser.
6.To view the documentation for the API built with OpenAPI, navigate to the api docs directory in the root of the project using the terminal, and run the following command:
```bash
    $ mkdocs serve
```
This will start a local development server for the API documentation. You can then view the documentation by navigating to http://localhost:8000 in your web browser.

## tech stack 
The Quote Engine API is built with the following technologies:
    ** <br/>   Python **: The core programming language used to build the API.
    ** <br/>   FastAPI **: A modern, fast (high-performance) web framework for building APIs with Python. *
    ** <br/>   MongoDB **: A NoSQL document-oriented database used to store the quotes data.
    ** <br/>   PyMongo **: A Python library for interacting with MongoDB databases.
    ** <br/>   PyJWT **: A Python library for encoding and decoding JSON Web Tokens (JWTs).
    ** <br/>   Bcrypt **: A password hashing library used to hash and verify user passwords.
    ** <br/>   Requests **: A Python library used to make HTTP requests to external APIs.
    ** <br/>   MkDocs **: A static site generator used to generate the API documentation.
    ** <br/>   Material for MkDocs **: A Material Design theme for MkDocs used to style the API  documentation.

The combination of these technologies provides a powerful and scalable platform for generating random motivational quotes, with a robust and user-friendly API and documentation.