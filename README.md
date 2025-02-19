# FastAPI

## Setup Instructions

1. **Clone the repository:**  `git clone https://github.com/davidfl10/FastAPI`
2. **Create a virtual environment:** `python -m venv .venv`
3. **Activate the virtual environment:**
   * Windows: `.venv\Scripts\activate`
4. **Install dependencies:** `pip install -r requirements.txt`
5. **Run the application:** `fastapi dev main.py`
6. **OpenAPI documentation**: `http://localhost:8000/docs`   - on port /docs

## CRUD Operations Logic

This FastAPI application provides CRUD (Create, Read, Update, Delete) operations for managing property listings, storing data in a SQLite database.

* **Database:** SQLite is used for data storage. The database file (`FastAPI.db`) is created in the project directory. SQLAlchemy is used as the ORM to interact with the database. The database connection details are in `database.py`.
* **Models:** The `models.py` file defines the database schema using SQLAlchemy. The `Property` model represents the structure of the properties table.
* **Schemas:** The `schemas.py` file defines the data structures used for request and response bodies using Pydantic. This ensures data validation and serialization.
* **CRUD Functions:** The `crud.py` file contains functions for performing database operations:
  * `get_properties`: Retrieves a list of properties, with optional filtering by city.
  * `get_property`: Retrieves a specific property by ID.
  * `create_property`: Creates a new property in the database.
  * `update_property`: Updates an existing property.
  * `delete_property`: Deletes a property.

## JWT Authentication

The application uses JWT (JSON Web Token) for authentication:

* **Authentication:** User authentication is handled in `auth.py`. The `authenticate_user` function verifies user credentials against a hardcoded dictionary.
* **Token Generation:** Upon successful authentication, the `create_access_token` function generates a JWT. The token includes the username and an expiration time.
* **Token Endpoint:** The `/token` endpoint is used to obtain a JWT by providing a username and password.
* **Authorization:** Protected endpoints require a valid JWT, which is verified by the `get_current_user` function. This function extracts the username from the token and retrieves the user information.
