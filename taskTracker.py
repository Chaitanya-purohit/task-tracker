import json
import os
import sys
from datetime import datetime

#Rename file
FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent = 2)

if len(sys.argv) < 2:
    print("Usage: python taskTracker.py <command> [args]")
    sys.exit(1)

command = sys.argv[1].lower()

if command == "add":
    description = sys.argv[2]
    tasks = load_tasks()
    now = datetime.now().isoformat()

    new_id = max((t["id"] for t in tasks), default = 0) + 1

    task = {
        "id" : new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt" : now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")
elif command == "list":
    tasks = load_tasks()
    l = []
    if (len(sys.argv) > 2):
        status = sys.argv[2]
        for t in tasks:
            if t["status"] == status:
                l.append(t)
    elif len(sys.argv) == 2:
        l = tasks
    if len(l) == 0:
        print("No tasks found")
    else: 
        for ta in l:
            print(f"[{ta['id']}] {ta['description']} - {ta['status']}")
elif command == "delete":
    tasks = load_tasks()
    if len(sys.argv) == 3:
          id = int(sys.argv[2])
          tasks = [t for t in tasks if t["id"] != id]
          save_tasks(tasks)
          print(f"Task {id} deleted successfully")
    else: 
        print("Incorrect use case")
elif command == "update":
    tasks = load_tasks()
    if len(sys.argv) >= 4:
        id = int(sys.argv[2])
        for t in tasks:
            if t["id"] == id:
                t["description"] = sys.argv[3]
                t["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print("Update successful")


