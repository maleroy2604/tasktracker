from tasktracker import TaskTracker


class Main:
    @staticmethod
    def calltasktracker():
        tasks_tracker = TaskTracker()
        tasks_tracker.start_daily_tasks_process()


if __name__ == '__main__':
    Main.calltasktracker()

