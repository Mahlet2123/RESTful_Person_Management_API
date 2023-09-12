# RESTful Person Management API

A RESTful API for managing person records, enabling you to create, read, update, and delete person information while providing dynamic parameter handling and secure database interactions. This project is done for HNGx internship  Stage-2 Task

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [Documentation](#documentation)

## Requirements

Before you begin, ensure you have all the requirements installed on your system:

Install the project dependencies:

    pip install -r requirements.txt

## Installation

1. Clone the repository to your local machine:

    git clone https://github.com/Mahlet2123/RESTful_Person_Management_API.git

2. Navigate to the project directory:

    cd RESTful_Person_Management_API

## Usage

To run the API, use the following command:

    python -m app

## API Endpoints

The API provides the following endpoints for CRUD operations on persons:

- Create a New Person

Endpoint: POST /api

Request Body: JSON object with "name" (string) and "age" (integer) fields.

Example:

    {
      "name": "John Doe",
      "age": 30
    }

- Get Person Details

Endpoint: GET /api/<int:user_id>
Example: GET /api/1

- Update Person Details

Endpoint: PUT /api/<int:user_id>

Request Body: JSON object with "name" (string) and "age" (integer) fields.

Example:

    {
      "name": "Updated Name",
      "age": 35
    }

- Delete a Person

Endpoint: DELETE /api/<int:user_id>

## Documentation

For detailed API documentation, including request/response formats and examples, please refer to the [API_Documentation]() file.
