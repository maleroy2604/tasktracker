import unittest
from unittest import TestCase
from unittest.mock import patch
from tasktracker import TaskTracker
from datetime import datetime
import os


class MyTestCase(TestCase):
    def setUp(self):
        self.temp_file_name = f"tasks_test_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

    def tearDown(self):
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

    @patch('builtins.input', side_effect=["New task 1", "New task 2", "exit"])
    def test_start_daily_tasks_process(self, mock_input):
        task_tracker = TaskTracker([], self.temp_file_name)
        task_tracker.start_daily_tasks_process()
        self.assertEqual(task_tracker._tasks, ["New task 1", "New task 2"])

    def test_write_into_daily_file(self):
        task_tracker = TaskTracker(["Task1", "Task2"], self.temp_file_name)
        task_tracker.write_into_daily_file()
        with open(self.temp_file_name, 'r') as file:
            content = file.read()
        self.assertEqual(content, "Task1\nTask2\n")

    def test_read_from_daily_file(self):
        task_tracker = TaskTracker(["Task1", "Task2"], self.temp_file_name)
        task_tracker.write_into_daily_file()
        content = task_tracker.read_from_daily_file()
        self.assertEqual(content, "Task1\nTask2\n")



if __name__ == '__main__':
    unittest.main()
