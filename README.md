# Address Book API

FastAPI-based address book application with geolocation search.

## Features
- Create and delete addresses
- Store latitude and longitude
- SQLite database
- Find nearby addresses by distance
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
