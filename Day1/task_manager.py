def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Task:
    def __init__(self, title, description, status=False):
        self.title = title
        self.description = description
        self.__status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = bool(value)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.__status
        }


class TaskManager:
    def __init__(self):
        self.tasks = []

    @logger
    def add_task(self, title, description, status):
        task = Task(title, description, status)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    @logger
    def change_status(self, index, new_status):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = new_status
            print("Status updated")
        else:
            print("Invalid index")

    @logger
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Deleted: {removed.title}")
        else:
            print("Invalid index")

    @logger
    def load_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task.title} - {task.description} - {task.status}")


def main():
    taskmanager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. Change Task Status")
        print("3. Delete Task")
        print("4. Load Tasks")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            status = input("Status (1/0): ") == "1"

            taskmanager.add_task(title, desc, status)

        elif choice == "2":
            idx = int(input("Index: ")) - 1
            status = input("Status (1/0): ") == "1"
            taskmanager.change_status(idx, status)

        elif choice == "3":
            idx = int(input("Index: ")) - 1
            taskmanager.delete_task(idx)

        elif choice == "4":
            taskmanager.load_tasks()

        elif choice == "5":
            break


if __name__ == "__main__":
    main()


