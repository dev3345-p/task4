import os
import json

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("⚠ Error reading tasks file. Starting with empty list.")
        return []

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(tasks, f, indent=4)
    except OSError as e:
        print(f"⚠ Error saving tasks: {e}")

def show_menu():
    print("\n===== TO-DO LIST APP =====")
    print("1. View tasks")
    print("2. Add task(s)")
    print("3. Remove task")
    print("4. Mark task as done/undone")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["done"] else "❌ Pending"
            print(f"{i}. {task['title']} [{status}]")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("Please enter Y or N.")

def add_tasks(tasks):
    while True:
        task = input("Enter a task: ").strip()
        if not task:
            print("Task cannot be empty.")
            continue

        if any(t["title"].lower() == task.lower() for t in tasks):
            print(f"⚠ Task '{task}' already exists.")
        else:
            tasks.append({"title": task, "done": False})
            save_tasks(tasks)
            print(f"Task '{task}' added successfully!")

        if not get_yes_no("Do you want to add another task? (y/n): "):
            break

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' removed successfully!")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def mark_task(tasks):
    if not tasks:
        print("No tasks to update.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to toggle status: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = not tasks[task_num - 1]["done"]
            save_tasks(tasks)
            status = "Done" if tasks[task_num - 1]["done"] else "Pending"
            print(f"Task '{tasks[task_num - 1]['title']}' marked as {status}.")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_task(tasks)
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("⚠ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()