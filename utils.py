def add_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def list_tasks():
    pass

def build_json(id, description, status, createdAt, updatedAt):
    return {"id": id,
            "description": description,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": updatedAt
    }