def add_task():
    print("In add_task")

def update_task():
    print("In update_task")

def delete_task():
    print("In delete_task")

def list_tasks():
    print("In list_tasks")

def build_json_obj(id, description, status, createdAt, updatedAt):
    return {"id": id,
            "description": description,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": updatedAt
    }