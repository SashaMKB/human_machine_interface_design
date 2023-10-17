import shutil
import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton, QApplication


class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Простой файловый работник")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.text_browser = QTextBrowser(self)
        self.layout.addWidget(self.text_browser)
        self.text_browser.setPlainText("ls - вывод всех файлов в директории\ncd - перейти в директорию\n"
                                       "cp - скопировать файлы в указанную директорию")

        self.command_input = QLineEdit(self)
        self.layout.addWidget(self.command_input)

        self.run_button = QPushButton("Выполнить", self)
        self.run_button.clicked.connect(self.execute_command)
        self.layout.addWidget(self.run_button)

        self.setLayout(self.layout)

    def execute_command(self):
        command = self.command_input.text()
        output = ""

        if command.startswith("cd "):
            directory = command[3:]
            try:
                os.chdir(directory)
                output = f"Директория изменена на {directory}"
            except FileNotFoundError:
                output = f"Директория '{directory}' не найдена"
        elif command == "ls":
            current_directory = os.getcwd()
            contents = os.listdir(current_directory)
            output = "\n".join(contents)
        elif command.startswith("cp "):
            files = command[3:command.find(">") - 1].split(" ")
            path = command[command.find(">") + 1:]
            for elem in files:
                shutil.copy(elem, path)

        else:
            output = "Неизвестная команда"

        self.text_browser.setPlainText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec_())
