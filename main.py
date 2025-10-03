import json
from crud import create_user, read_user, update_user, delete_user

if __name__ == "__main__":
    print(json.dumps(create_user("101", {"name": "Alice", "email": "alice@example.com"}), indent=2))
    print(json.dumps(read_user("101"), indent=2))
    print(json.dumps(update_user("101", {"email": "alice@newmail.com"}), indent=2))
    print(json.dumps(read_user("101"), indent=2))
    print(json.dumps(delete_user("101"), indent=2))
    print(json.dumps(read_user("101"), indent=2))
