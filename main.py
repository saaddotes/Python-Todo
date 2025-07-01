def add_task(task_list):
    """
    Adds a new task to the task list.
    """
    new_task = get_task_input("Enter a new task:")
    if new_task:
        task_list.append(new_task)
        print("Task added successfully.")
    else:
        print("No task entered.")
    print_tasks(task_list)


def delete_task(task_list):
    """
    Deletes a task from the task list using its 1-based index.
    """
    modify_task_list(task_list, action_type='delete')


def update_task(task_list):
    """
    Updates a task in the task list using its 1-based index.
    """
    modify_task_list(task_list, action_type='update')


def modify_task_list(task_list, action_type):
    """
    Modifies the task list based on action type ('delete' or 'update').
    """
    if not task_list:
        print(f"No tasks to {action_type}.")
        return
    index = get_task_index(task_list, action_type)
    if index is not None:
        if action_type == 'delete':
            removed_task = task_list.pop(index)
            print(f"Task '{removed_task}' deleted successfully.")
        elif action_type == 'update':
            current_task = task_list[index]
            new_description = get_task_input(f"Enter new task description to replace '{current_task}':")
            if new_description:
                task_list[index] = new_description
                print("Task updated successfully.")
            else:
                print("Task not updated. No new description entered.")
    print_tasks(task_list)


def get_task_input(prompt):
    """
    Utility function to get input from the user with stripping the whitespace.
    """
    return input(prompt).strip()


def get_task_index(task_list, action_type):
    """
    Prompts for a valid task index for the specified action.
    """
    task_count = len(task_list)
    try:
        index = int(input(f"Enter the task number to {action_type} (1 to {task_count}): ")) - 1
        if 0 <= index < task_count:
            return index
        else:
            print("Invalid number. Please enter a valid index.")
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
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("File not found. Starting with an empty task list.")
        return []


def save_tasks_to_file(task_list, filename="tasks.txt"):
    """
    Saves the current task list to a file.
    """
    try:
        with open(filename, "w") as file:
            file.writelines(task + "\n" for task in task_list)
        print("Tasks saved to file successfully.")
    except IOError as e:
        print(f"Error saving tasks: {e}")


def print_tasks(task_list):
    """
    Prints the current list of tasks.
    """
    if task_list:
        print("Updated Task List:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")


def main():
    task_list = load_tasks_from_file()
    print("Current tasks:")
    print_tasks(task_list)

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
                actions[action](task_list)
            else:
                print("Please enter a valid option.")
            save_tasks_to_file(task_list)
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()