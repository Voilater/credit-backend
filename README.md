# Credit Backend

A minimal Flask-based backend for handling credit applications.

## Features

- GET `/applications`: Returns all stored applications.
- POST `/applications`: Adds a new application to a local JSON file.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Sample POST Payload

```json
{
  "id": 1,
  "name": "John Doe",
  "amount": 50000,
  "status": "approved"
}
```
