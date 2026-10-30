# Patient CRUD API

### 🌐 Live Application — Render

**[View ReDoc](https://YOUR-PATIENT-SERVICE.onrender.com/redoc)**

---

<div align="center">

## Patient Records. Clear Endpoints. Simple Operations.

A Python and FastAPI project for creating, viewing, updating, and deleting patient records through a documented REST API.

**Python · FastAPI · Pydantic · Uvicorn · Render**

[Source Code](https://github.com/Dhrumil00007/patient_curd) ·
[Local API Documentation](http://127.0.0.1:8000/docs)

</div>

---

## Overview

Patient CRUD API demonstrates the complete lifecycle of a patient record using REST endpoints. It includes request validation with Pydantic and interactive API documentation through FastAPI.

The project was developed for **Principles of DevOps and Web API Development**.

## Features

- **Create:** Add a patient record.
- **Read:** Retrieve all patients or find one by ID.
- **Update:** Modify an existing patient.
- **Delete:** Remove a patient record.
- **Validate:** Check request data against defined schemas.
- **Explore:** Test API operations directly through Swagger UI.

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Application programming language |
| FastAPI | API framework and routing |
| Pydantic | Data models and request validation |
| Uvicorn | ASGI application server |
| Swagger UI / ReDoc | API documentation |
| Git and GitHub | Version control and source hosting |
| Render | Application hosting |

## Project Layout

The following layout describes the structure used in this guide:

```text
patient_curd/
├── main.py
├── routes/
│   └── patient_routes.py
├── models/
│   └── patient.py
├── schemas/
│   └── patient_schema.py
├── requirements.txt
├── README.md
└── .gitignore
```

| Path | Responsibility |
| --- | --- |
| `main.py` | Creates the application and registers routes |
| `routes/patient_routes.py` | Defines patient API endpoints |
| `models/patient.py` | Contains the patient model |
| `schemas/patient_schema.py` | Defines request and response schemas |
| `requirements.txt` | Lists application dependencies |

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Dhrumil00007/patient_curd.git
cd patient_curd
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```bat
.venv\Scripts\activate.bat
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Start the application

```bash
python -m uvicorn main:app --reload
```

Open **http://127.0.0.1:8000/docs** to test the API.

## API Reference

Base URL for local development:

```text
http://127.0.0.1:8000
```

| Method | Endpoint | Operation |
| --- | --- | --- |
| `POST` | `/patients` | Create a patient |
| `GET` | `/patients` | Retrieve all patients |
| `GET` | `/patients/{id}` | Retrieve a patient by ID |
| `PUT` | `/patients/{id}` | Update a patient |
| `DELETE` | `/patients/{id}` | Delete a patient |

Replace `{id}` with an existing patient's ID. The running application's `/docs` page provides the authoritative endpoint paths and request schemas.

## Example Request

Example patient body for a schema containing `name`, `email`, and `age`:

```json
{
  "name": "John",
  "email": "john@example.com",
  "age": 20
}
```

Use the fields shown in Swagger UI if your patient schema differs.

## Test the API

1. Start the server.
2. Open `/docs`.
3. Expand the create-patient operation.
4. Select **Try it out**, enter the required fields, and select **Execute**.
5. Retrieve the created patient.
6. Update the record and retrieve it again.
7. Delete the record and check the response when retrieving it afterward.

You can also test requests using Postman, Thunder Client, or curl.

## Render Configuration

For an application whose entry point is `main.py` and FastAPI instance is `app`:

| Setting | Value |
| --- | --- |
| Build command | `pip install -r requirements.txt` |
| Start command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| Documentation path | `/docs` |

Configure any environment variables required by your application in the Render dashboard.

## Repository Hygiene

Recommended `.gitignore` entries:

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
.env
.env.*
!.env.example
.pytest_cache/
.vscode/
.idea/
```

Keep credentials and database connection secrets in environment variables.

## Learning Outcomes

This project demonstrates:

- FastAPI application setup and routing
- REST API design and CRUD operations
- Request validation with Pydantic
- Interactive API testing
- Python dependency management
- GitHub source hosting and Render deployment

## Author

**Dhrumil Patel**

[GitHub Profile](https://github.com/Dhrumil00007)
