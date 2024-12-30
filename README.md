# FastAPI Blog API

A simple RESTful API for a blog built with FastAPI and SQLAlchemy.

## Features

- Create blog posts
- Retrieve all blog posts
- Retrieve a specific blog post by ID
- Update existing blog posts
- Delete blog posts
- SQLite database integration

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the server with:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/blog` | Create a new blog post |
| GET | `/blog` | Retrieve all blog posts |
| GET | `/blog/{id}` | Retrieve a specific blog post |
| PUT | `/blog/{id}` | Update a specific blog post |
| DELETE | `/blog/{id}` | Delete a specific blog post |

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI) at `http://localhost:8000/docs`
- Alternative API documentation (ReDoc) at `http://localhost:8000/redoc`


## Database Schema

### Blog Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| title | String | Title of the blog post |
| body | String | Content of the blog post |
