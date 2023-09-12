# RESTful Person Management API Documentation

Welcome to the documentation for the RESTful Person Management API. This API allows you to manage "person" resources, performing CRUD (Create, Read, Update, Delete) operations on individual persons.

## API Base URL

The API is hosted at the following base URL:

http://localhost:5000


## API Endpoints

### 1. Create a New Person

- **Endpoint**: `POST /api`
- **Request Body**: JSON object with the following fields:
  - `name` (string): The name of the person (required).
  - `age` (integer): The age of the person (required).

**Example Request:**

```json
POST /api
Content-Type: application/json

{
  "name": "John Doe",
  "age": 30
}
```

Example Response

    {
      "message": "Person created successfully"
    }

Or

    {
        "message": "Person with this name already exists"
    }

if the name already exist in the database.

### 2. Get Person Details
Endpoint: GET /api/<int:user_id>

    {
      "name": "John Doe",
      "age": 30
    }

Example Response

    {
      "message": "Person not found"
    }

### Update Person Details
Endpoint: PUT /api/<int:user_id>

Path Parameter:

- user_id (integer): The ID of the person to update (required).

Request Body: JSON object with the following fields:

- name (string): The updated name of the person (required).
- age (integer): The updated age of the person (required).

**Example Request:**

    PUT /api/1
    Content-Type: application/json

    {
      "name": "Updated Name",
      "age": 35
    }

Example Response (Success - HTTP 200 OK):

    {
      "message": "Person updated successfully"
    }

Example Response (Person Not Found - HTTP 404 Not Found):

    {
      "message": "Person not found"
    }

### 4. Delete a Person

Endpoint: DELETE /api/<int:user_id>

Path Parameter:

- user_id (integer): The ID of the person to delete (required).

Example Request:

DELETE /api/1

Example Response (Success - HTTP 200 OK):

    {
      "message": "Person deleted successfully"
    }

Example Response (Person Not Found - HTTP 404 Not Found):

    {
      "message": "Person not found"
    }


