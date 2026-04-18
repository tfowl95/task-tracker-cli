import json
import sys
import datetime
from utils import *

args = sys.argv[1:]
check_args(args)

file_path = "tasks.json"
create_file_if_missing(file_path)

with open(file_path, "r") as file:
    tasks_content = json.load(file)

if args[0] == "add":
    new_id = find_new_id(tasks_content)
    add_task(new_id, args[1], tasks_content, file_path)
elif args[0] == "update":
    update_task()
elif args[0] == "delete":
    delete_task()
elif args[0] == "list":
    list_tasks()
else:
    print("Error: undefined argument. Supported arguments: add, update, delete, list.")