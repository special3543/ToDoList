import sys
import pickle
import os
import appdirs
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QHBoxLayout, QSizePolicy

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.app_name = "TodoApp"
        self.app_author = "OpenAI"
        self.app_dir = appdirs.user_data_dir(self.app_name, self.app_author)
        self.todo_file = os.path.join(self.app_dir, 'todo.dat')
        self.completed_file = os.path.join(self.app_dir, 'completed.dat')

        self.resize(1000, 800)
        self.setWindowTitle('To-Do List')

        self.layout = QHBoxLayout()

        self.todo_list = QListWidget()
        self.completed_list = QListWidget()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("What to do ?")

        self.add_btn = QPushButton('Add')
        self.add_btn.clicked.connect(self.add_task)

        self.delete_btn = QPushButton('Delete')
        self.delete_btn.clicked.connect(self.delete_task)

        self.complete_btn = QPushButton('Complete')
        self.complete_btn.clicked.connect(self.complete_task)

        self.delete_completed_btn = QPushButton('Delete Completed')
        self.delete_completed_btn.clicked.connect(self.delete_completed)

        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(QLabel('Tasks:'))
        self.vlayout.addWidget(self.todo_list)
        self.vlayout.addWidget(self.task_input)
        self.vlayout.addWidget(self.add_btn)
        self.vlayout.addWidget(self.delete_btn)
        self.vlayout.addWidget(self.complete_btn)

        self.vlayout2 = QVBoxLayout()
        self.vlayout2.addWidget(QLabel('Completed:'))
        self.vlayout2.addWidget(self.completed_list)
        self.vlayout2.addWidget(self.delete_completed_btn)

        self.layout.addLayout(self.vlayout)
        self.layout.addLayout(self.vlayout2)

        self.setLayout(self.layout)

        self.load_data()
        self.set_dark_theme()

    def add_task(self):
        task_name = self.task_input.text()
        if task_name:
            self.todo_list.addItem(task_name)
            self.task_input.setText('')
            self.save_data()

    def delete_task(self):
        current_item = self.todo_list.currentItem()
        if current_item:
            self.todo_list.takeItem(self.todo_list.row(current_item))
            self.save_data()

    def complete_task(self):
        current_item = self.todo_list.currentItem()
        if current_item:
            self.completed_list.addItem(current_item.text())
            self.todo_list.takeItem(self.todo_list.row(current_item))
            self.save_data()

    def delete_completed(self):
        self.completed_list.clear()
        self.save_data()

    def set_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1f2126;
                font-size: 15px;
                font-family: Arial;
            }
            QLabel {
                color: #cfd2d8;
            }
            QPushButton {
                background-color: #313441;
                color: #cfd2d8;
                border: none;
                padding: 10px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #414b5c;
            }
            QLineEdit {
                background-color: #282a36;
                color: #cfd2d8;
                border: none;
                padding: 10px;
            }
            QListWidget {
                background-color: #282a36;
                color: #cfd2d8;
                border: none;
                padding: 10px;
            }
            QListWidget::item {
                padding: 10px;
                margin: 5px;
            }
        """)

    def closeEvent(self, event):
        self.save_data()

    def save_data(self):
        if not os.path.exists(self.app_dir):
            os.makedirs(self.app_dir)
        with open(self.todo_file, 'wb') as f:
            pickle.dump([self.todo_list.item(i).text() for i in range(self.todo_list.count())], f)
        with open(self.completed_file, 'wb') as f:
            pickle.dump([self.completed_list.item(i).text() for i in range(self.completed_list.count())], f)

    def load_data(self):
        try:
            with open(self.todo_file, 'rb') as f:
                tasks = pickle.load(f)
                self.todo_list.addItems(tasks)
        except (OSError, IOError) as e:
            pass
        try:
            with open(self.completed_file, 'rb') as f:
                tasks = pickle.load(f)
                self.completed_list.addItems(tasks)
        except (OSError, IOError) as e:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo = TodoApp()
    todo.show()
    sys.exit(app.exec_())
