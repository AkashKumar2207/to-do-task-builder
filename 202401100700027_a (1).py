def add_task(tasks):
  task = input("Enter the task: ")
  tasks.append({"task": task, "completed": False})
  print("Task added successfully!")

def view_tasks(tasks):
  if not tasks:
    print("No tasks in the list.")
    return

  print("Your tasks:")
  for index, task in enumerate(tasks):
    status = "[x]" if task["completed"] else "[ ]"
    print(f"{index + 1}. {status} {task['task']}")

def delete_task(tasks):
  view_tasks(tasks)
  if not tasks:
    return

  try:
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
      del tasks[task_index]
      print("Task deleted successfully!")
    else:
      print("Invalid task number.")
  except ValueError:
    print("Invalid input. Please enter a number.")

def mark_completed(tasks):
  view_tasks(tasks)
  if not tasks:
    return

  try:
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
      tasks[task_index]["completed"] = True
      print("Task marked as completed!")
    else:
      print("Invalid task number.")
  except ValueError:
    print("Invalid input. Please enter a number.")

def main():
  tasks = []
  while True:
    print("\nChoose an action:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      add_task(tasks)
    elif choice == "2":
      view_tasks(tasks)
    elif choice == "3":
      delete_task(tasks)
    elif choice == "4":
      mark_completed(tasks)
    elif choice == "5":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
