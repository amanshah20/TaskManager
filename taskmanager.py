tasks = []  # List to store tasks

while True:
    print("\n===== 🏆 Task Manager =====")
    print("1️⃣ View Tasks")
    print("2️⃣ Add Task")
    print("3️⃣ Mark Task as Completed")
    print("4️⃣ Delete Task")
    print("5️⃣ Exit")

    choice = input("Enter your choice: ")

    # View tasks
    if choice == "1":
        if len(tasks) == 0:
            print("\n📌 No tasks available!\n")
        else:
            print("\n===== 📝 Task List =====")
            for i in range(len(tasks)):
                status = "✔ Completed" if tasks[i][1] else "❌ Pending"
                print(f"{i+1}. {tasks[i][0]} [{status}]")

    # Add a new task
    elif choice == "2":
        title = input("Enter task title: ")
        tasks.append([title, False])  # False means the task is not completed
        print("✅ Task added successfully!\n")

    # Mark a task as completed
    elif choice == "3":
        if len(tasks) == 0:
            print("\n⚠ No tasks to complete!\n")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]} - {'✔ Completed' if tasks[i][1] else '❌ Pending'}")
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index][1] = True
                    print("✅ Task marked as completed!\n")
                else:
                    print("⚠ Invalid task number!\n")
            except ValueError:
                print("⚠ Please enter a valid number!\n")

    # Delete a task
    elif choice == "4":
        if len(tasks) == 0:
            print("\n⚠ No tasks to delete!\n")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]} - {'✔ Completed' if tasks[i][1] else '❌ Pending'}")
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    del tasks[index]
                    print("✅ Task deleted successfully!\n")
                else:
                    print("⚠ Invalid task number!\n")
            except ValueError:
                print("⚠ Please enter a valid number!\n")

    # Exit program
    elif choice == "5":
        print("🚀 Exiting Task Manager. Goodbye!")
        break

    # Invalid input
    else:
        print("⚠ Invalid choice! Please enter a valid option.\n")
