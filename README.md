# Event Reminder API

This is a Django Rest Framework (DRF) based backend service that allows users to create and manage event reminders. It includes user registration and authentication using JWT (JSON Web Token). Below are the descriptions of the **login** and **register** endpoints.

## User Authentication Endpoints

### 1. User Registration (Register)

#### Endpoint
`POST /accounts/register/`

#### Description
This endpoint allows new users to register an account by providing a username, email, and password. The password will be securely hashed before being saved in the database.

#### Request Example
```bash
POST /accounts/register/
Content-Type: application/json

{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "strongpassword123"
}
```

#### Response Example
* Status Code: 201 Created
```json
{
  "message": "User created successfully"
}
```
* Status Code: 400 Bad Request
```json
{
  "error": "User creation failed"
}
```

### 2. User Login (Login)
#### Endpoint
`POST /accounts/login/`

#### Description
This endpoint allows registered users to login by providing their username and password. If the credentials are valid, the server will return a JWT access token and a refresh token.

#### Request Example
```bash
POST /accounts/login/
Content-Type: application/json

{
    "username": "newuser",
    "password": "strongpassword123"
}
```

#### Response Example
* Status Code: 200 OK
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```
* Status Code: 401 Unauthorized
```json
{
    "detail": "No active account found with the given credentials"
}
```

