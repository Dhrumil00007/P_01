# Patient CRUD API

A simple **Patient CRUD API** built with **Python and FastAPI**.
This project demonstrates how to create, read, update, and delete patient records through REST API endpoints.

## 🚀 Features

* Create a new patient
* Get all patients
* Get a patient by ID
* Update patient information
* Delete a patient
* FastAPI REST API
* Automatic API documentation with Swagger UI
* Python virtual environment support

## 🛠️ Technologies Used

* **Python 3**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* REST API
* Git & GitHub

## 📁 Project Structure

```text
patient_curd/
│
├── main.py
├── routes/
│   └── patient_routes.py
│
├── models/
│   └── patient.py
│
├── schemas/
│   └── patient_schema.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact folder structure may vary depending on the final version of the project.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Dhrumil00007/patient_curd.git
cd patient_curd
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not available, install FastAPI and Uvicorn manually:

```powershell
pip install fastapi uvicorn
```

## ▶️ Run the Project

Start the FastAPI server using:

```powershell
uvicorn main:app --reload
```

The API will normally run at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

After starting the server, open:

**Swagger UI**

```text
http://127.0.0.1:8000/docs
```

**ReDoc**

```text
http://127.0.0.1:8000/redoc
```

Swagger UI allows you to test the CRUD operations directly from your browser.

## 🔗 API Endpoints

| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| GET    | `/patients`      | Get all patients     |
| GET    | `/patients/{id}` | Get a patient by ID  |
| POST   | `/patients`      | Create a new patient |
| PUT    | `/patients/{id}` | Update a patient     |
| DELETE | `/patients/{id}` | Delete a patient     |

## 📝 Example Patient

Example request:

```json
{
  "name": "John",
  "email": "john@example.com",
  "age": 20
}
```

## 🧪 Testing

You can test the API using:

* FastAPI Swagger UI
* Browser for GET requests
* Postman
* Thunder Client
* curl

For example:

```text
GET http://127.0.0.1:8000/patients
```

## 📦 Requirements

Example `requirements.txt`:

```text
fastapi
uvicorn
```

Install them with:

```powershell
pip install -r requirements.txt
```

## 🔐 Environment

The project uses a Python virtual environment.

The `.venv` folder should **not** be uploaded to GitHub.

Make sure `.gitignore` contains:

```text
.venv/
__pycache__/
*.pyc
.env
```

## 📌 Project Purpose

This project was created as a **Patient CRUD assignment** to demonstrate:

1. FastAPI application setup
2. REST API development
3. CRUD operations
4. API routing
5. Request and response handling
6. Running an application with Uvicorn
7. Publishing a Python project to GitHub

## 👨‍💻 Author

**Dhrumil Patel**

---

⭐ If you find this project useful, feel free to star the repository.
