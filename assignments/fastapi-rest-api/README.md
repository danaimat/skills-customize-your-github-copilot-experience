# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a complete REST API using FastAPI to manage a collection of books. You'll learn how to create endpoints, handle HTTP methods, validate request data, and implement error handling—essential skills for modern web development.

## 📝 Tasks

### 🛠️ Task 1: Create Basic API Endpoints

#### Description
Set up a basic FastAPI application with GET endpoints to retrieve book data. Start by creating a simple in-memory data store and expose it through your API.

#### Requirements
Your API should:

- Have a GET `/books` endpoint that returns a list of all books in JSON format
- Have a GET `/books/{id}` endpoint that returns a single book by ID
- Return appropriate HTTP status codes (200 for success)
- Use proper JSON serialization for responses

**Example Response:**
```json
GET /books
[
  { "id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019 },
  { "id": 2, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008 }
]
```

### 🛠️ Task 2: Add Data Creation Endpoints

#### Description
Extend your API with POST endpoints to allow users to add new books to the collection. Implement proper request handling and data validation.

#### Requirements
Your API should:

- Have a POST `/books` endpoint that accepts JSON data (title, author, year) and adds a new book
- Generate unique IDs for new books automatically
- Return the created book with its assigned ID and a 201 status code
- Handle missing or invalid input by returning a 400 error
- Validate that required fields are present in the request body

**Example Request/Response:**
```json
POST /books
Request: { "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015 }
Response (201): { "id": 3, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015 }
```

### 🛠️ Task 3: Implement Update and Delete Operations

#### Description
Add PUT and DELETE endpoints to allow users to modify and remove books. This completes the full CRUD operations.

#### Requirements
Your API should:

- Have a PUT `/books/{id}` endpoint that updates an existing book's information
- Have a DELETE `/books/{id}` endpoint that removes a book from the collection
- Return the updated book data (200) when successful
- Return a 404 error if attempting to update or delete a non-existent book
- Prevent deletion of books that were not added by the user (optional challenge: track ownership)

**Example:**
```
PUT /books/1
Request: { "title": "Python Crash Course (2nd Edition)", "author": "Eric Matthes", "year": 2023 }
Response (200): { "id": 1, "title": "Python Crash Course (2nd Edition)", ... }

DELETE /books/3
Response (204): No Content
```

### 🛠️ Task 4: Add Advanced Features (Stretch Goal)

#### Description
Enhance your API with professional features like request validation using Pydantic models, filtering, and custom error handling.

#### Requirements
Your API should:

- Use Pydantic models to validate all request and response data
- Add a query parameter to `/books` for filtering by author: `GET /books?author=EricMatthes`
- Implement custom error responses with descriptive messages
- Add response documentation using FastAPI's built-in OpenAPI support (swagger UI at `/docs`)
- Handle edge cases like invalid query parameters gracefully

**Example:**
```
GET /books?author=EricMatthes
Response (200):
[
  { "id": 1, "title": "Python Crash Course (2nd Edition)", "author": "Eric Matthes", "year": 2023 }
]

GET /books/999
Response (404):
{ "detail": "Book with id 999 not found" }
```

## 📚 Tips

- Start by running the FastAPI server locally: `uvicorn main:app --reload`
- Test your endpoints using a tool like Postman, cURL, or use FastAPI's built-in `/docs` endpoint
- Remember that each endpoint should handle both success and error cases
- Use FastAPI's automatic documentation to verify your endpoints are properly configured
