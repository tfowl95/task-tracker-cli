import json
import sys
import time
from utils import add_task, update_task, delete_task, list_tasks, build_json


def main():
    file_path = "tasks.json"
    args = sys.argv[1:]
    test_json = build_json(args[0], args[1], args[2], time.time(), time.time())
    print(test_json)

if __name__ == "__main__":
    main()