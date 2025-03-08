from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.input_label = QLabel("Введите название конфигурации:")
        self.input_text = QLineEdit()
        self.apply_button = QPushButton("Применить")
        self.apply_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.apply_button)

        self.setLayout(layout)
        self.setWindowTitle("")

    def get_input_text(self):
        return self.input_text.text()
