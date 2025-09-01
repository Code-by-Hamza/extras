def menu():
    print("\n---Wellcome to the todo list---\n")
    print("1. View Tasks")
    print("2. Add tasks")
    print("3. Remove tasks")
    print("4. Save & Exit")

def load():
    try:
        with open("tasks.txt" , "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save(tasks):
    with open("tasks.txt" , "w") as f:
        for task in tasks:
            f.write (task + "\n")

def mainloop():
    tasks = load()
    
    while True:
        menu()
        choice = input("Enter a Number:").lstrip()
        
        if choice == "1":
            print("Your Tasks:")
            for i , task in enumerate(tasks,1):
                print(f"{i}. {task}")
        
        elif choice == "2":
            new_task = input("Add a new tasks:")
            tasks.append(new_task)
            print(f"Added:\n {new_task}")
        
        elif choice == "3":
            task_no = int(input("Enter task no. to remove:")) - 1
            
            if 0 <= task_no < len(tasks):
                removed = tasks.pop(task_no)
                print(f"Removed: {removed}")
        
        elif choice == "4":
            save(tasks)
            print("tasks saved! Good Bye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    mainloop()