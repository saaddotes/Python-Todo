def add_task(task_list):
    """
    Adds a new task to the task list.
    """
    task_description = input("Enter a new task: ").strip()
    if task_description:
        task_list.append(task_description)
        print("Task added successfully")
    else:
        print("No task entered.")
    print(f"Updated List: {task_list}")


def delete_task(task_list):
    """
    Deletes a task from the task list using its 1-based index.
    """
    if not task_list:
        print("No tasks to delete.")
        return
    try:
        index = int(input(f"Enter the task number to delete (1 to {len(task_list)}): ")) - 1
        if 0 <= index < len(task_list):
            task_list.pop(index)
            print("Task deleted successfully")
        else:
            print("Invalid number. Please enter a correct index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    print(f"Updated List: {task_list}")


def update_task(task_list):
    """
    Updates a task in the task list using its 1-based index.
    """
    if not task_list:
        print("No tasks to update.")
        return
    try:
        index = int(input(f"Enter the task number to update (1 to {len(task_list)}): ")) - 1
        if 0 <= index < len(task_list):
            new_description = input(f"Enter new task to replace '{task_list[index]}': ").strip()
            if new_description:
                task_list[index] = new_description
                print("Task updated successfully")
            else:
                print("No new task entered.")
        else:
            print("Invalid number. Please enter a correct index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    print(f"Updated List: {task_list}")


def load_tasks_from_file(filename="tasks.txt"):
    """
    Loads tasks from a file. Returns a list of tasks or an empty list if the file is not found.
    """
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_tasks_to_file(task_list, filename="tasks.txt"):
    """
    Saves the current task list to a file.
    """
    try:
        with open(filename, "w") as file:
            file.writelines(task + "\n" for task in task_list)
        print("Tasks saved to file successfully")
    except IOError as e:
        print(f"Error saving tasks: {e}")


def main():
    tasks = load_tasks_from_file()
    print(f"Current tasks: {tasks}")

    while True:
        try:
            action = int(input("1- Add Task\n2- Remove Task\n3- Update Task\n0- Exit\n>> "))
            if action == 0:
                print("Exiting Task Manager")
                break
            elif action == 1:
                add_task(tasks)
            elif action == 2:
                delete_task(tasks)
            elif action == 3:
                update_task(tasks)
            else:
                print("Please enter a valid option.")
            save_tasks_to_file(tasks)
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
