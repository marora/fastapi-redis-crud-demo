from db import get_redis_client
from responses import response

r = get_redis_client()

def create_user(user_id, user_data):
    try:
        if r.exists(f"user:{user_id}"):
            return response(error="User already exists", status=400)
        r.hset(f"user:{user_id}", mapping=user_data)
        return response(data={"user_id": user_id}, status=201)
    except Exception as e:
        return response(error=str(e), status=500)

def read_user(user_id):
    try:
        if not r.exists(f"user:{user_id}"):
            return response(error="User not found", status=404)
        return response(data=r.hgetall(f"user:{user_id}"), status=200)
    except Exception as e:
        return response(error=str(e), status=500)

def update_user(user_id, updates):
    try:
        if not r.exists(f"user:{user_id}"):
            return response(error="User not found", status=404)
        r.hset(f"user:{user_id}", mapping=updates)
        return response(data={"updated": True}, status=200)
    except Exception as e:
        return response(error=str(e), status=500)

def delete_user(user_id):
    try:
        if not r.exists(f"user:{user_id}"):
            return response(error="User not found", status=404)
        r.delete(f"user:{user_id}")
        return response(data={"deleted": True}, status=200)
    except Exception as e:
        return response(error=str(e), status=500)
