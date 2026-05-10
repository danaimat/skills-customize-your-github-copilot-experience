"""
Building REST APIs with FastAPI - Starter Code

This is a template for building a REST API to manage a book collection.
Complete the tasks by implementing the required endpoints.

Start the server with: uvicorn main:app --reload
Test your API at: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(
    title="Book Management API",
    description="A REST API for managing a collection of books",
    version="1.0.0"
)

# ============================================================================
# Data Models (using Pydantic for validation)
# ============================================================================

class Book(BaseModel):
    """Model representing a book in the collection"""
    id: int
    title: str
    author: str
    year: int

class BookCreate(BaseModel):
    """Model for creating a new book (without ID)"""
    title: str
    author: str
    year: int

# ============================================================================
# In-Memory Database
# ============================================================================

# Sample book data to get you started
books_db = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
]

next_id = 3  # Track the next ID to assign to new books

# ============================================================================
# Task 1: Get Endpoints
# ============================================================================

@app.get("/books", response_model=List[Book])
def get_books(author: Optional[str] = Query(None)):
    """
    TODO: Task 1 & 4
    Get all books, optionally filtered by author.
    
    - Return all books if no author filter is provided
    - If author filter is provided, return only books by that author (Task 4)
    - For Task 1, focus on returning all books
    """
    # TODO: Implement this endpoint
    pass

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """
    TODO: Task 1
    Get a single book by ID.
    
    - Return the book if found
    - Return 404 error if not found
    """
    # TODO: Implement this endpoint
    pass

# ============================================================================
# Task 2: Post Endpoint
# ============================================================================

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    """
    TODO: Task 2
    Create a new book and add it to the collection.
    
    - Assign a unique ID automatically
    - Return the created book with status 201
    - Validate that all required fields are provided
    """
    # TODO: Implement this endpoint
    pass

# ============================================================================
# Task 3: Put and Delete Endpoints
# ============================================================================

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookCreate):
    """
    TODO: Task 3
    Update an existing book.
    
    - Update the book with the given ID
    - Return the updated book with status 200
    - Return 404 if book not found
    """
    # TODO: Implement this endpoint
    pass

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """
    TODO: Task 3
    Delete a book from the collection.
    
    - Remove the book with the given ID
    - Return status 204 (No Content) on success
    - Return 404 if book not found
    """
    # TODO: Implement this endpoint
    pass

# ============================================================================
# Task 4: Error Handling (Stretch Goal)
# ============================================================================

@app.get("/")
def root():
    """Welcome endpoint with API information"""
    return {
        "message": "Welcome to the Book Management API",
        "docs_url": "/docs",
        "tasks_completed": "Add your task completion status here"
    }

# TODO: Add custom error handling as needed in Task 4

if __name__ == "__main__":
    # Run the server with: python main.py
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
