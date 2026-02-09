# Address Book API

This is a FastAPI-based address book application.

## Features
- Create, delete addresses
- Store latitude and longitude
- SQLite database
- Retrieve addresses within a given distance
- Input validation using Pydantic

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy

## How to run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
