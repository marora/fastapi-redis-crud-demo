from fastapi import FastAPI, HTTPException
from crud import create_user, read_user, update_user, delete_user

app = FastAPI(title="Redis CRUD Demo", version="1.0")

@app.post("/users/{user_id}")
def create_user_api(user_id: str, user_data: dict):
    result = create_user(user_id, user_data)
    if result["error"]:
        raise HTTPException(status_code=result["status"], detail=result["error"])
    return result

@app.get("/users/{user_id}")
def read_user_api(user_id: str):
    result = read_user(user_id)
    if result["error"]:
        raise HTTPException(status_code=result["status"], detail=result["error"])
    return result

@app.put("/users/{user_id}")
def update_user_api(user_id: str, updates: dict):
    result = update_user(user_id, updates)
    if result["error"]:
        raise HTTPException(status_code=result["status"], detail=result["error"])
    return result

@app.delete("/users/{user_id}")
def delete_user_api(user_id: str):
    result = delete_user(user_id)
    if result["error"]:
        raise HTTPException(status_code=result["status"], detail=result["error"])
    return result
