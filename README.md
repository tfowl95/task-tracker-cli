# Task Tracker CLI

A lightweight command-line task tracker written in Python. Tasks are stored locally in a JSON file and can be managed entirely from your terminal.

---

## Concepts used

* CLI positional arguments via sys.argv
* JSON file i/o
* Creating executable script that runs in bash from any directory

---

## Features

* Add, update, and delete tasks
* Mark tasks as **in progress** or **done**
* List tasks by status (`all`, `done`, `todo`, `in-progress`)
* Automatic ID assignment
* Persistent storage using a local JSON file

---

## Project Structure

```
task-cli.py     # Main CLI entry point
utils.py        # Helper functions for task management
tasks.json      # Auto-created task storage file
```

---

## Requirements

* Python 3.7+
* Unix-like shell (macOS/Linux) or PowerShell/Command Prompt (Windows)

---

## Installation

1. Clone or download the project:

```
git clone https://github.com/tfowl95/task-tracker-cli.git
cd task-tracker-cli
```

2. Ensure the script is executable (macOS/Linux):

```
chmod +x task-cli.py
```

---

## Setup: Run as `task-cli` Command

### macOS / Linux

#### Add to PATH

1. Move the task-cli.py and utils.py to a directory in your PATH. Example:

```
mv task-cli.py /usr/local/bin/task-cli
mv utils.py /usr/local/bin/task-cli
```

1. Rename task-cli.py to task-cli and make sure it is executable:

```
chmod +x /full/path/to/task-cli
```

3. Verify:

```
task-cli add "test task"
task-cli list
task-cli delete 1
```

---

### Windows

#### Option 1: Add a Batch Wrapper

1. Create a file named `task-cli.bat` somewhere in your PATH (e.g., `C:\Windows` or a custom scripts folder):

```
@echo off
python "C:\full\path\to\task-cli.py" %*
```

2. Ensure Python is in your PATH.

3. Run:

```
task-cli add "test task"
task-cli list
task-cli delete 1
```

---

#### Option 2: Add Python Script Directory to PATH

1. Place the script in a folder (e.g., `C:\scripts`)
2. Add that folder to your system PATH
3. Run using:

```
python task-cli.py add "example task"
```

(Optional: rename to `task-cli.py` and associate `.py` with Python to run directly)

---

## Usage

### Add a Task

```
task-cli add "go grocery shopping"
```

---

### Update Task Description

```
task-cli update <id> "new description"
```

Example:

```
task-cli update 1 "buy groceries and cook dinner"
```

---

### Delete a Task

```
task-cli delete <id>
```

---

### Mark Task as In Progress

```
task-cli mark-in-progress <id>
```

---

### Mark Task as Done

```
task-cli mark-done <id>
```

---

### List Tasks

```
task-cli list
```

Filter options:

```
task-cli list done
task-cli list todo
task-cli list in-progress
```

---

## Data Storage

Tasks are stored in tasks.json in the same directory as your task-cli file:

* Automatically created if missing
* Stored as a JSON array
* Each task includes:

  * `id`
  * `description`
  * `status`
  * `createdAt`
  * `updatedAt`

---

## Example Task Output

```
ID:             1
Description:    go grocery shopping
Status:         Not started
Created At:     04/18/2026 02:15 PM
Updated At:     04/20/2026 09:46 PM
----------------------------------
```

---

## Error Handling

The CLI validates:

* Command existence
* Argument count
* ID format
* Task existence

Common errors include:

* Invalid command
* Missing arguments
* Non-numeric task IDs
* Task not found

---

## Notes

* Task IDs are unique and reused only if gaps exist
* Status values:

  * `Not started`
  * `In progress`
  * `Done`

---

## License

No license specified.
