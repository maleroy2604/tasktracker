from tasktracker import TaskTracker
from datetime import datetime


class Main:
    TODAY_DATE = datetime.now().strftime("%Y-%m-%d")

    def call_task_tracker(self):
        file_name = f"tasks_{self.TODAY_DATE}.txt"
        tasks_tracker = TaskTracker([], file_name)
        tasks_tracker.start_daily_tasks_process()


if __name__ == '__main__':
    main = Main()
    main.call_task_tracker()

