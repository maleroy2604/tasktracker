import os.path
from datetime import datetime


class TaskTracker:

    def __init__(self, tasks, file_name):
        self._tasks = tasks
        self._file_name = file_name

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
            self.write_in_file_with_option('a')
        else:
            self.write_in_file_with_option('w')

    def read_from_daily_file(self):
        with open(self._file_name, 'r') as file:
            return file.read()

    def write_in_file_with_option(self, option):
        with open(self._file_name, option) as file:
            for task in self._tasks:
                file.write(task + '\n')

