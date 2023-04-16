# Route Documentation
#### `POST /login`

Endpoint used to authenticate users and generate a JWT access token.
Request

    HTTP Method: POST
    Endpoint: /login
    Headers:
        Content-Type: application/x-www-form-urlencoded
    Request Body:
```json
        username: "The user's username or email".
        password: "The user's password".
```
Response
    Status Codes:
        200 OK: Successful authentication.
        400 Bad Request: Invalid credentials.

    Response Body:
        access_token: The JWT access token.
        token_type: "Bearer".
example
```bash
$ curl -X POST https://example.com/login \
       -H "Content-Type: application/x-www-form-urlencoded" \
       -d "username=john_doe&password=secret"
```
sample response
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...<JWT Token>",
  "token_type": "Bearer"
}
```
<br/><br/>

#### `POST /user/new`

Endpoint used to create a new user.
Request

    HTTP Method: POST
    Endpoint: /user/new
    Headers:
        Content-Type: application/json
    Request Body:
        email: The user's email address. This should be a valid email address.
        password: The user's password. This should be a string.
        first_name: The user's first name. This should be a string.
        surname: The user's surname. This should be a string.
        username: The user's username. This should be a string.

Response

    Status Codes:
        201 Created: User created successfully.
        400 Bad Request: Invalid request body.
        403 Forbidden: User with the same email or username already exists.

    Response Body (if status code is 201 Created):
        user_id: The unique identifier of the created user.
        email: The email address of the created user.

    Response Body (if status code is 400 Bad Request):
        detail: The error message explaining the validation error(s).

    Response Body (if status code is 403 Forbidden):
        detail: The error message explaining that the email or username already exists.

Example
```curl
$ curl -X POST https://example.com/user/new \
       -H "Content-Type: application/json" \
       -d '{"email": "john.doe@example.com", "password": "password", "first_name": "John", "surname": "Doe", "username": "johndoe"}'
```
```json
{
  "user_id": "12345",
  "email": "john.doe@example.com"
}
```


<br/><br/>

#### `GET /quotes`
This endpoint returns a random motivational quote from the database. <br/>
`Request Parameters` <br/>
    limit (optional): The maximum number of quotes to return. Defaults to 1 if not set.

Headers

    X-API-Key: The API key used to authenticate the request.

Response

Returns a JSON object or an array of objects with the following fields:

    quote: The text of the motivational quote.
    author: The author of the quote.

Example response with limit set to 1:
```json 
{
    "quote": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs"
}
```
Example response with limit set to 3:
```json
[
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    },
    {
        "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "author": "Winston S. Churchill"
    },
    {
        "quote": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt"
    }
]
```
