import os.path
from datetime import datetime


class TaskTracker:

    TODAY_DATE = datetime.now().strftime("%Y-%m-%d")

    def __init__(self):
        self._tasks = []
        self._file_name = f"tasks_{self.TODAY_DATE}.txt"

    def start_daily_tasks_process(self):
        if os.path.exists(self._file_name):
            content = self.read_from_daily_file()
            print(f"Current tasks: \n {content}")
        while True:
            input_user = input("Enter your daily task (type exit to stop prompt): ")
            if input_user == "exit":
                break
            self._tasks.append(input_user)

        self.write_into_daily_file()

    def write_into_daily_file(self):
        if os.path.exists(self._file_name):
            with open(self._file_name, 'a') as file:
                for task in self._tasks:
                    file.write(task + '\n')
        else:
            with open(self._file_name, 'w') as file:
                for task in self._tasks:
                    file.write(task + '\n')

    def read_from_daily_file(self):
        with open(self._file_name, 'r') as file:
            return file.read()
