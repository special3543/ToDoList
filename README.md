# ToDoList

## Description

This is a simple To-Do List application developed using Python and PyQt5. The app allows users to keep track of tasks that they need to do and mark them as completed once they're done. Completed tasks can also be deleted from the list.

## Features

- Add tasks to the to-do list
- Mark tasks as completed
- Delete tasks from the to-do list
- Delete tasks from the completed list
- Dark theme for better visual experience
- Persistent storage: tasks are saved locally and loaded automatically when the app is started

## Setup & Installation

- Install Python 3 from the official Python website
- Install PyQt5 and appdirs by running the command: `pip install pyqt5 appdirs`
- Clone or download this repository
- Navigate to the repository's directory
- Run `main.py` to start the app

## How to Use

1. Enter a task in the text field and click on the "Add" button to add a task to the list.
2. Select a task and click on the "Delete" button to delete a task from the list.
3. Select a task and click on the "Complete" button to mark a task as completed. This will move the task from the to-do list to the completed list.
4. Click on the "Delete Completed" button to delete all completed tasks.

## Notes

- Tasks are saved in the local appdata directory, which is platform-specific. Tasks are saved automatically whenever they are added, deleted, or completed.
- When you complete a task, it is removed from the to-do list and added to the completed tasks list.
- When you delete a task from either list, it is permanently deleted and cannot be restored.
