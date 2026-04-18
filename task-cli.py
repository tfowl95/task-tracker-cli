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
    add_task(args[1], tasks_content, file_path)
elif args[0] == "update":
    update_task(args[1], args[2], tasks_content, file_path)
elif args[0] == "delete":
    delete_task(args[1], tasks_content, file_path)
elif args[0] == "list":
    list_tasks()
else:
    print("Error: undefined command. Supported commands: add, update, delete, mark-in-progress, mark-done, list.")