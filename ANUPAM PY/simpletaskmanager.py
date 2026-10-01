tasks = []

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Sort tasks")
    print("5. Exit")

    try:
        choice = int(input("\nChoose any option from the above: "))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == 2:
        if tasks:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
        else:
            print("No tasks to show.")

    elif choice == 3:
        task = input("Enter any task to remove: ")
        try:
            tasks.remove(task)
            print("Task removed.")
        except ValueError:
            print("Task not found.")

    elif choice == 4:
        tasks.sort()
        print("Tasks sorted:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid option! Please enter your choice again.")