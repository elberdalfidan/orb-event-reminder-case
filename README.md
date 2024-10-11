# Event Reminder API

This is a Django Rest Framework (DRF) based backend service that allows users to create and manage event reminders. It includes user registration and authentication using JWT (JSON Web Token). The API provides various endpoints for users to register, log in, create, update, delete, and retrieve event reminders and categories. 

## Features
- **User Registration**: Allows new users to create an account.
- **User Authentication**: Secure login for existing users, returning JWT for session management.
- **Category Management**: Users can create, list, update, and delete categories for their event reminders.
- **Event Reminders**: Users can create, list, update, delete, and filter event reminders based on categories.

Below are the descriptions of the **endpoints**.

## Installation via Virtual Environment
1. Clone the repository 
2. Create a virtual environment
```bash
python -m venv venv
```
3. Activate the virtual environment
* Windows
```bash
source venv/bin/activate
```
* MacOS/Linux
```bash
. ./venv/bin/activate
```
4. Install the required packages
```bash
pip install -r requirements.txt
```
5. Run the migrations
```bash
python manage.py migrate
```
6. Run the server
```bash
python manage.py runserver
```

## Installation via Docker
1. Clone the repository
2. Build the Docker image
```bash
docker-compose up --build
```

# Postman API Documentation

To help you get started with the API, you can import the Postman collection from the repository. The collection includes all the available endpoints, along with request examples and responses.

### How to Import Postman Collection
1. Open Postman.
2. Click on the "Import" button in the top left corner.
3. Choose the exported JSON file from your project directory.
4. Once imported, you can explore the API endpoints and make requests directly from Postman.

The Postman collection file can be found in the `docs/` directory of the project.

# API Documentation

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

## Event Reminder Endpoints

### 1. Create Event Reminder

#### Endpoint
`POST /events/`

#### Description
This endpoint allows users to create a new event reminder.

#### Request Example
```bash
POST /events/
Content-Type: application/json
Authorization
Bearer eyJ..
        
    {
        "title": "Test Event",
        "description": "This is a test event",
        "category": 1,
        "event_date": "2022-12-31T23:59:59Z"
    }
```

#### Response Example
* Status Code: 201 Created
```json
{
    "id": 1,
    "user": 1,
    "title": "Test Event",
    "description": "This is a test event",
    "category": 1,
    "event_date": "2022-12-31T23:59:59Z"
}
```
* Status Code: 400 Bad Request
```json
{
    "error": "Event creation failed"
}
```

### 2. List Event Reminders

#### Endpoint
`GET /events/`

#### Description
This endpoint allows users to view all the event reminders they have created.

#### Request Example
```bash
GET /events/
Content-Type: application/json
Authorization
Bearer eyJ
```

#### Response Example
* Status Code: 200 OK
```json
[
    {
        "id": 1,
        "user": 1,
        "title": "Test Event",
        "description": "This is a test event",
        "category": 1,
        "event_date": "2022-12-31T23:59:59Z"
    }
]
```
* Status Code: 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 3. Update Event Reminder

#### Endpoint
`PUT /events/<event_id>/`

#### Description
This endpoint allows users to update the details of a specific event reminder.

#### Request Example
```bash
PUT /events/1/
Content-Type: application/json
Authorization
Bearer eyJ
    {
        "title": "Updated Event",
        "description": "This is an updated event",
        "category": 1,
        "event_date": "2022-12-31T23:59:59Z"
    }
```

#### Response Example

* Status Code: 200 OK
```json
{
    "id": 1,
    "user": 1,
    "title": "Updated Event",
    "description": "This is an updated event",
    "category": 1,
    "event_date": "2022-12-31T23:59:59Z"
}
```
* Status Code: 400 Bad Request
```json
{
    "error": "Event update failed"
}
```

### 4. Delete Event Reminder

#### Endpoint
`DELETE /events/<event_id>/`

#### Description
This endpoint allows users to delete a specific event reminder.

#### Request Example
```bash
DELETE /events/1/
Content-Type: application/json
Authorization
Bearer eyJ
```

#### Response Example
* Status Code: 204 No Content
```json
{}
```
* Status Code: 400 Bad Request
```json
{
    "error": "Event deletion failed"
}
```

### 5. Get Upcoming Event Reminders

#### Endpoint
`GET /events/upcoming/`

#### Description
This endpoint allows users to view all the upcoming event reminders they have created.

#### Request Example
```bash
GET /events/upcoming/
Content-Type: application/json
Authorization
Bearer eyJ
```

#### Response Example
* Status Code: 200 OK
```json
[
    {
        "id": 1,
        "user": 1,
        "title": "Test Event",
        "description": "This is a test event",
        "category": 1,
        "event_date": "2022-12-31T23:59:59Z"
    }
]
```
* Status Code: 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 6. Get Events By Category Name

#### Endpoint
`GET /events/category/<category_name>/`

#### Description
This endpoint allows users to view all the event reminders they have created under a specific category.

#### Request Example
```bash
GET /events/category/TEST%20CATEGORY/
Content-Type: application/json
Authorization
Bearer eyJ
```

#### Response Example

* Status Code: 200 OK
```json
[
    {
        "id": 1,
        "user": 1,
        "title": "Test Event",
        "description": "This is a test event",
        "category": 1,
        "event_date": "2022-12-31T23:59:59Z"
    }
]
```
* Status Code: 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```


