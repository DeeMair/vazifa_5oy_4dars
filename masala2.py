from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap

class DeeMair(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gpt tuzgan savollar")
        self.setGeometry(100, 100, 400, 500)

        self.savollar = [
            {"savol": "Quyosh qaysi sayyora atrofida aylanadi?", "javoblar": ["Yer", "Savol xato tuzilgan", "Mars"], "to'g'ri": 1, "rasm": "solar_system.jpeg"},
            {"savol": "Suvning kimyoviy formulasi qaysi?", "javoblar": ["H2O", "CO2", "O2"], "to'g'ri": 0, "rasm": "woter.jpg"},
            {"savol": "7 + 3 nechiga teng?", "javoblar": ["8", "9", "10"], "to'g'ri": 2, "rasm": "math.gif"},
            {"savol": "Eng katta okean qaysi?", "javoblar": ["Atlantika okeani", "Tinch okeani", "Hind okeani"], "to'g'ri": 1, "rasm": "ocean.jpg"},
            {"savol": "Eng tez yuguruvchi hayvon qaysi?", "javoblar": ["Sher", "Gepard", "Fil"], "to'g'ri": 1, "rasm": "animals.jpg"}
        ]

        self.score = 0
        self.current_question = 0

        self.widget = QWidget()
        self.layout = QVBoxLayout()

        self.savol_label = QLabel(self)
        self.layout.addWidget(self.savol_label)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.buttons = []
        for i in range(3):
            button = QRadioButton(self)
            self.layout.addWidget(button)
            self.buttons.append(button)

        self.next_button = QPushButton("Keyingisi", self)
        self.next_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.next_button)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.load_question()

    def load_question(self):
        question = self.savollar[self.current_question]
        self.savol_label.setText(question["savol"])
        pixmap = QPixmap(question["rasm"])
        pixmap = pixmap.scaled(400, 300)
        self.image_label.setPixmap(pixmap)

        for i, button in enumerate(self.buttons):
            button.setText(question["javoblar"][i])
            button.setChecked(False)

    def check_answer(self):
        selected = -1
        for i, button in enumerate(self.buttons):
            if button.isChecked():
                selected = i

        if selected == self.savollar[self.current_question]["to'g'ri"]:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.savollar):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        result = f"Sizning umumiy balingiz: {self.score}/{len(self.savollar)}"
        msg_box = QMessageBox()
        msg_box.setText(result)
        msg_box.exec_()
        self.close()

app = QApplication([])
window = DeeMair()
window.show()
app.exec_()
