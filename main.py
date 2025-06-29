def add_task(tasks):
    """
    Adds a new task to the task list.
    """
    new_task = input("Enter a new task: ").strip()
    if new_task:
        tasks.append(new_task)
        print("Task added successfully.")
    else:
        print("No task entered.")
    print(f"Updated Task List: {tasks}")


def delete_task(tasks):
    """
    Deletes a task from the task list using its 1-based index.
    """
    if not tasks:
        print("No tasks to delete.")
        return
    index = get_task_index(len(tasks), 'delete')
    if index is not None:
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' deleted successfully.")
    print(f"Updated Task List: {tasks}")


def update_task(tasks):
    """
    Updates a task in the task list using its 1-based index.
    """
    if not tasks:
        print("No tasks to update.")
        return
    index = get_task_index(len(tasks), 'update')
    if index is not None:
        current_task = tasks[index]
        new_description = input(f"Enter new task to replace '{current_task}': ").strip()
        if new_description:
            tasks[index] = new_description
            print("Task updated successfully.")
        else:
            print("Task not updated. No new description entered.")
    print(f"Updated Task List: {tasks}")


def get_task_index(task_count, action):
    """
    Prompts for a valid task index for the specified action.
    """
    try:
        index = int(input(f"Enter the task number to {action} (1 to {task_count}): ")) - 1
        if 0 <= index < task_count:
            return index
        else:
            print("Invalid number. Please enter a correct index.")
            return None
    except ValueError:
        print("Invalid input. Please enter a numerical index.")
        return None


def load_tasks_from_file(filename="tasks.txt"):
    """
    Loads tasks from a file. Returns a list of tasks or an empty list if the file is not found.
    """
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("File not found. Starting with an empty task list.")
        return []


def save_tasks_to_file(tasks, filename="tasks.txt"):
    """
    Saves the current task list to a file.
    """
    try:
        with open(filename, "w") as file:
            file.writelines(task + "\n" for task in tasks)
        print("Tasks saved to file successfully.")
    except IOError as e:
        print(f"Error saving tasks: {e}")


def main():
    tasks = load_tasks_from_file()
    print(f"Current tasks: {tasks}")

    actions = {
        1: add_task,
        2: delete_task,
        3: update_task
    }
    while True:
        try:
            action = int(input("1- Add Task\n2- Remove Task\n3- Update Task\n0- Exit\n>> "))
            if action == 0:
                print("Exiting Task Manager.")
                break
            elif action in actions:
                actions[action](tasks)
            else:
                print("Please enter a valid option.")
            save_tasks_to_file(tasks)
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
