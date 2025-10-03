# 📌 Redis CRUD Demo (FastAPI + Redis)

This project demonstrates a simple **CRUD (Create, Read, Update, Delete)** API using **FastAPI** and **Redis**.
It shows how to implement basic REST endpoints, handle JSON responses, and use Redis as a lightweight database.

---

## 🚀 Features

* FastAPI backend with auto-generated Swagger docs.
* Redis as the primary database (using hashes for user records).
* CRUD operations with structured JSON responses.
* Error handling with proper HTTP status codes (400, 404, 500).
* Easy to run locally with `uvicorn`.

---

## 📂 Project Structure

```
redis_crud_demo/
│── app.py          # FastAPI app with CRUD routes
│── crud.py         # CRUD logic (Redis operations)
│── db.py           # Redis connection helper
│── responses.py    # Response helper function
│── requirements.txt# Dependencies
│── README.md       # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/marora/redis_crud_demo.git
cd redis_crud_demo
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Redis server

If installed via Homebrew (macOS):

```bash
brew install redis
brew services start redis
```

Or using Docker:

```bash
docker run -d --name redis -p 6379:6379 redis:latest
```

### 5. Run FastAPI app

```bash
uvicorn app:app --reload
```

* First `app` = filename (`app.py`)
* Second `app` = FastAPI instance name inside the file

---

## 📖 API Documentation

Once running, visit:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔧 Example API Calls

### Create User

```bash
curl -X POST "http://127.0.0.1:8000/users/101" \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice", "email": "alice@example.com"}'
```

### Read User

```bash
curl http://127.0.0.1:8000/users/101
```

### Update User

```bash
curl -X PUT "http://127.0.0.1:8000/users/101" \
     -H "Content-Type: application/json" \
     -d '{"email": "alice@newmail.com"}'
```

### Delete User

```bash
curl -X DELETE http://127.0.0.1:8000/users/101
```

---

## ⚠️ Troubleshooting

* **`Error loading ASGI app. Could not import module "app"`**

  * Make sure you are in the project root (`redis_crud_demo/`).
  * Ensure your FastAPI instance is called `app = FastAPI()` in `app.py`.
  * If your file is named differently, adjust the run command:

    ```bash
    uvicorn main:app --reload      # if your file is main.py
    uvicorn redis_crud_demo.app:app --reload   # if running from parent dir
    ```

---

## 📌 Requirements

* Python 3.9+
* Redis (local or Docker)
* Packages listed in `requirements.txt`:

  ```
  fastapi
  uvicorn
  redis
  ```

---

## 📈 Next Steps

* Add authentication (JWT or OAuth2).
* Containerize with Docker.
* Use Redis JSON (`ReJSON`) for richer objects.
* Deploy with Nginx/Apache + Uvicorn/Gunicorn for production.