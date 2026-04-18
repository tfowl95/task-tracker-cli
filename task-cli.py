import json
import sys
import time
from utils import add_task, update_task, delete_task, list_tasks, build_json_obj


file_path = "tasks.json"
args = sys.argv[1:]

if args[0] == "add":
    add_task()
elif args[0] == "update":
    update_task()
elif args[0] == "delete":
    delete_task()
elif args[0] == "list":
    list_tasks()
else:
    print("Error, undefined command. Supported commands: add, update, delete, list.")