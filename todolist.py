def display_menu():
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nThe to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{i}. {task['task']} [{status}]")

def add_task(todo_list):
    task = input("\nEnter the task: ")
    todo_list.append({'task': task, 'completed': False})
    print("Task added.")

def remove_task(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def mark_task_completed(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                todo_list[task_number - 1]['completed'] = True
                print(f"Task '{todo_list[task_number - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            mark_task_completed(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the to-do list manager
main()
