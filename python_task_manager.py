import json
import time

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


#Task Class

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.__done = done

    @property #for access and control so validation.....looks like an attribute but it is a method
    def done(self):
        return self.__done
    
    @done.setter
    def done(self, value):
        self.__done = bool(value)

    def to_dict(self):
        return {
            "title": self.title,
            "done": self.__done
        }
    

#Task Manager Class

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    #static utility method to read tasks from a file
    @staticmethod
    def show_line():
        print("-" * 40)
    @classmethod #accessible from class direct
    def app_name(cls):
        return "Task Manager Application"
    #file handling
    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)
    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Task(**item) for item in data]

        except:
            return []
    @logger
    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
    @logger
    def show_tasks(self):
        self.show_line()
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Done" if task.done == True else "Pending"
                print(f"{idx + 1}. {task.title} - {status}")
        self.show_line()
    @logger
    def mark_done(self, index):
        if 0<=index < len(self.tasks):
            self.tasks[index].done = True
            self.save_tasks()
    @logger
    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()



def main():
    taskmanager = TaskManager()

    while True:
        print("\n Add Task")
        print("\ Show Tasks")
        print("\ Mark Task as Done")
        print("\ Delete Task")
        print("\ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            taskmanager.add_task(title)
        elif choice == "2":
            taskmanager.show_tasks()
        elif choice == "3":
            taskmanager.show_tasks()
            index = int(input("Enter task number to mark as done: ")) - 1
            taskmanager.mark_done(index)
        elif choice == "4":
            taskmanager.show_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            taskmanager.delete_task(index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    
if __name__ == "__main__":
    main()