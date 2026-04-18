import sys
from pathlib import Path
import json
import datetime

def check_args(args):
    if len(args) == 0:
        print("Error: missing initial command. Supported commands: add, update, delete, list.")
        sys.exit()
    elif (len(args) == 1 or len(args) > 2) and args[0] == "add":
        print("Error: incorrect number of arguments. 'add' command accepts one argument: description (double quotes for strings)")
        sys.exit()
    elif (len(args) == 2 or len(args) == 1 or len(args) > 3) and args[0] == "update":
        print("Error: incorrect number of arguments. 'update' command accepts two arguments: id, description (double quotes for strings)")
        sys.exit()

def get_unique_id(tasks_content):
    existing_ids = []
    for task in tasks_content:
        existing_ids.append(int(task.get("id")))
    new_id = 1
    id_found = False
    while not id_found:
        if new_id in existing_ids:
            new_id += 1
        else:
            id_found = True
    return new_id

def add_task(description, tasks_content, file_path):
    new_id = get_unique_id(tasks_content)
    now = str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p"))
    new_task = build_json_obj(new_id, description, "Not started", now, now)
    tasks_content.append(new_task)
    with open(file_path, "w") as file:
        json.dump(tasks_content, file, indent = 4)
    print(f"Task added successfully (ID: {new_id})")

def update_task(id, description, tasks_content, file_path):
    match_found = False
    id = int(id)
    for task in tasks_content:
        if id == task.get("id"):
            match_found = True
            task["description"] = description
            with open(file_path, "w") as file:
                json.dump(tasks_content, file, indent = 4)
            print("Task description updated successfully")
            break
        else:
            continue
    if not match_found:
        print("Error: task id not found. Please run command 'list' for a list of tasks.")

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

def create_file_if_missing(file_path):
    if not Path(file_path).exists():
        with open(file_path, "w") as file:
            json.dump([], file)
