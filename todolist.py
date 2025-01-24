import os

TODO_FILE = "todo.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append(f"[ ] {task}")
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def view_tasks(tasks):
    """View all tasks in the list."""
    if not tasks:
        print("No tasks found.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def mark_completed(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            if "[x]" not in task:
                tasks[task_num - 1] = task.replace("[ ]", "[x]")
                save_tasks(tasks)
                print(f"Task {task_num} marked as completed!")
            else:
                print("Task is already completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
