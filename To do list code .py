def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx+1}. {task['task']} [{status}]")

def add_task(tasks):
    desc = input("Enter task description: ")
    tasks.append({"task": desc, "done": False})

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        print("\n==== To-Do List Menu ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()