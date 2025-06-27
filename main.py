```python
def add_todo():
    """
    Adds a new task to the task list.
    """
    task_input = input("Enter a new task: ")
    tasks.append(task_input)
    print("Task added successfully")
    print(f"Updated List: {tasks}")


def delete_task():
    """
    Deletes a task from the task list using its 1-based index.
    """
    try:
        index_input = int(input(f"Enter the task number to delete (1 to {len(tasks)}): ")) - 1
        if 0 <= index_input < len(tasks):
            tasks.pop(index_input)
            print("Task deleted successfully")
        else:
            print("Invalid number. Please enter a correct index.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def update_task():
    """
    Updates a task in the task list using its 1-based index.
    """
    try:
        index_input = int(input(f"Enter the task number to update (1 to {len(tasks)}): ")) - 1
        if 0 <= index_input < len(tasks):
            updated_task = input(f"Enter new task to replace '{tasks[index_input]}': ")
            tasks[index_input] = updated_task
            print("Task updated successfully")
        else:
            print("Invalid number. Please enter a correct index.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def load_tasks_from_file():
    """
    Loads tasks from a file 'tasks.txt'. Returns a list of tasks or an empty list if the file is not found.
    """
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks_to_file():
    """
    Saves the current task list to 'tasks.txt'.
    """
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved to file successfully")
    except Exception as e:
        print(f"Error saving tasks: {e}")


tasks = load_tasks_from_file()
print(f"Current tasks: {tasks}")

actions = {
    1: add_todo,
    2: delete_task,
    3: update_task,
    0: exit
}

while True:
    try:
        action = int(input("1- Add Task\n2- Remove Task\n3- Update Task\n0- Exit\n>> "))
        if action in actions:
            if action == 0:
                print("Exiting Task Manager")
                break
            actions[action]()
            save_tasks_to_file()
        else:
            print("Please enter a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")
```