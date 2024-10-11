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

## Category Endpoints

### 1. Create Category

#### Endpoint
`POST /categories/`

#### Description
This endpoint allows users to create a new category for their event reminders.

#### Request Example
```bash
POST /categories/
Content-Type: application/json
Authorization
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
    
    {
        "name": "TEST CATEGORY",
        "description": "This is a test category"
    }
```

#### Response Example
* Status Code: 201 Created
```json
{
    "id": 1,
    "user": 1,
    "name": "TEST CATEGORY",
    "description": "This is a test category"
}
```
* Status Code: 400 Bad Request
```json
{
    "error": "Category creation failed"
}
```

### 2. List Categories

#### Endpoint
`GET /categories/`

#### Description
This endpoint allows users to view all the categories they have created.

#### Request Example
```bash
GET /categories/
Content-Type: application/json
Authorization 
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

#### Response Example
* Status Code: 200 OK
```json
[
    {
        "id": 1,
        "user": 1,
        "name": "TEST CATEGORY",
        "description": "This is a test category"
    }
]
```
* Status Code: 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 3. Update Category

#### Endpoint
`PUT /categories/<category_id>/`

#### Description
This endpoint allows users to update the details of a specific category.

#### Request Example
```bash
PUT /categories/1/
Content-Type: application/json
Authorization
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9... 
    {
        "name": "UPDATED CATEGORY",
        "description": "This is an updated category"
    }   
```

#### Response Example
* Status Code: 200 OK
```json
{
    "id": 1,
    "user": 1,
    "name": "UPDATED CATEGORY",
    "description": "This is an updated category"
}
```
* Status Code: 400 Bad Request
```json
{
    "error": "Category update failed"
}
```

### 4. Delete Category

#### Endpoint
`DELETE /categories/<category_id>/`

#### Description
This endpoint allows users to delete a specific category.

#### Request Example
```bash
DELETE /categories/1/
Content-Type: application/json
Authorization
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

#### Response Example
* Status Code: 204 No Content
```json
{}
```
* Status Code: 400 Bad Request
```json
{
    "error": "Category deletion failed"
}
```



