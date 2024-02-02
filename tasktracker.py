from datetime import datetime


class TaskTracker:

    def __init__(self):
        self.tasks = []

    def start_daily_tasks_process(self):
        while True:
            input_user = input("Enter your daily task (type exit to stop prompt): ")
            if input_user == "exit":
                break
            self.tasks.append(input_user)

        self.write_into_daily_file()

    def write_into_daily_file(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        file_name = f"tasks_{today_date}.txt"
        with open(file_name, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')
