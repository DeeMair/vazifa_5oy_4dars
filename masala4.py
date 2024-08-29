from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QDialog, QVBoxLayout as DVBoxLayout
from PyQt5.QtCore import Qt

class InfoCollector(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ma'lumot to'plash")
        self.setGeometry(100, 100, 500, 400)

        self.widget = QWidget()
        self.layout = QVBoxLayout()

        self.province_combo = QComboBox()
        self.province_combo.addItems([
            "Toshkent viloyati", "Samarqand viloyati", "Farg'ona viloyati", "Andijon viloyati", "Buxoro viloyati",
            "Jizzax viloyati", "Qashqadaryo viloyati", "Namangan viloyati", "Navoiy viloyati", "Xorazm viloyati",
            "Sirdaryo viloyati", "Qoraqalpog'iston Respublikasi"
        ])
        self.province_combo.currentIndexChanged.connect(self.update_cities)
        self.layout.addWidget(QLabel("Tug'ilgan viloyat:"))
        self.layout.addWidget(self.province_combo)

        self.city_combo = QComboBox()
        self.layout.addWidget(QLabel("Tuman yoki shahar:"))
        self.layout.addWidget(self.city_combo)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Erkak", "Ayol"])
        self.layout.addWidget(QLabel("Jins:"))
        self.layout.addWidget(self.gender_combo)

        self.nationality_combo = QComboBox()
        self.nationality_combo.addItems(["O'zbek", "Rus", "Qozoq", "Tojik", "Qirg'iz"])
        self.layout.addWidget(QLabel("Millat:"))
        self.layout.addWidget(self.nationality_combo)

        self.show_button = QPushButton("Natijani ko'rsatish")
        self.show_button.clicked.connect(self.show_info)
        self.layout.addWidget(self.show_button)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.load_styles()
        self.update_cities()

    def update_cities(self):
        province = self.province_combo.currentText()
        cities = {
            "Toshkent viloyati": [
                "Toshkent", "Chirchiq", "Yunusabad", "Bektemir", "Yangiyo'l", "Olmazor", "Mirzo-Ulug'bek", "Yashnobod",
                "Sergeli", "Kichik Xalqa", "Uchtepa", "Bektemir", "Zangiota", "Bo'ka", "Qibray"
            ],
            "Samarqand viloyati": [
                "Samarqand", "Jomboy", "Kattaqo'rg'on", "Narpay", "Oqdaryo", "Ishtikhan", "Paxtachi", "Kishlok",
                "Samarqand", "Oqdaryo", "Urgut", "Buxoro", "Siyob", "Kattaqo'rg'on", "Shahrisabz"
            ],
            "Farg'ona viloyati": [
                "Farg'ona", "Andijon", "Marg'ilon", "Qo'qon", "Toshloq", "Rishton", "Farg'ona", "Beshariq",
                "Yozyovon", "Kokand", "Asaka", "Bag'dod", "Jalaquduq", "Quva", "Turon"
            ],
            "Andijon viloyati": [
                "Andijon", "Asaka", "Xo'jaobod", "O'qituvchi", "Marhamat", "Shahrihon", "Izboskan", "Jalaquduk",
                "Andijon", "Bog'ot", "Pakhtaabad", "Kurgantepa", "Xonabad", "Uzunboy", "Oqtepa"
            ],
            "Buxoro viloyati": [
                "Buxoro", "G'ijduvon", "Vobkent", "Kogon", "Peshku", "Jondor", "Shofirkon", "Olot", "Peshku",
                "G'ijduvon", "Vobkent", "Kogon", "Jondor", "Olot", "Romitan"
            ],
            "Jizzax viloyati": [
                "Jizzax", "G'allaorol", "Zarbdor", "Forish", "Yangiabad", "Arnasoy", "Balandcha", "Jizzax",
                "Zafarabad", "Paxtakor", "Yangiobod", "G'allaorol", "Forish", "Jizzax", "Dostluk"
            ],
            "Qashqadaryo viloyati": [
                "Qarshi", "Shahrisabz", "G'uzor", "Kitob", "Yakkabog'", "Koson", "Chirakchi", "Qarshi",
                "Shahrisabz", "Yakkabog'", "G'uzor", "Kitob", "Chirakchi", "Koson", "Oqoltin"
            ],
            "Namangan viloyati": [
                "Namangan", "Chust", "Kosonsoy", "Pop", "Uychi", "Namangan", "Chortoq", "Yangikurgan",
                "Davlatabad", "Jarkurgan", "To'raqo'rg'on", "Narin", "Yangiobod", "Nurobod", "Namangan"
            ],
            "Navoiy viloyati": [
                "Navoiy", "Zarafshon", "Karmana", "Uchquduq", "Konimex", "Navbahor", "Xatirchi", "Nurota",
                "Zarafshon", "Karmana", "Uchquduq", "Navoiy", "Konimex", "Nurota", "Navbahor"
            ],
            "Xorazm viloyati": [
                "Urganch", "Xiva", "Gurlan", "Shovot", "Hazarasp", "Yangiariq", "Khorazm", "Xiva",
                "Urganch", "Gurlan", "Shovot", "Hazarasp", "Yangiarik", "Khojeyli", "Beruniy"
            ],
            "Sirdaryo viloyati": [
                "Gulistan", "Sirdaryo", "Mirzaobod", "Boyovut", "Oqoltin", "Sirdaryo", "Gulistan",
                "Mirzaobod", "Boyovut", "Oqoltin", "Shirin", "Mingbulak", "Sirdaryo", "Sirdaryo", "Gulistan"
            ],
            "Qoraqalpog'iston Respublikasi": [
                "Nukus", "Muynak", "Chimboy", "Shumanay", "Qonliko'l", "Nukus", "Kokdumalak", "To'rtko'l",
                "Ellikqala", "Beruni", "Kegeyli", "Shumanay", "Nukus", "Qonliko'l", "Chimboy"
            ]
        }
        self.city_combo.clear()
        self.city_combo.addItems(cities.get(province, []))

    def show_info(self):
        province = self.province_combo.currentText()
        city = self.city_combo.currentText()
        gender = self.gender_combo.currentText()
        nationality = self.nationality_combo.currentText()

        info_dialog = QDialog(self)
        info_dialog.setWindowTitle("Tanlangan ma'lumotlar")
        info_dialog.setGeometry(150, 150, 400, 300)

        dialog_layout = DVBoxLayout()

        dialog_layout.addWidget(QLabel(f"Tug'ilgan viloyat: {province}"))
        dialog_layout.addWidget(QLabel(f"Tuman yoki shahar: {city}"))
        dialog_layout.addWidget(QLabel(f"Jins: {gender}"))
        dialog_layout.addWidget(QLabel(f"Millat: {nationality}"))

        info_dialog.setLayout(dialog_layout)
        info_dialog.exec_()

    def load_styles(self):
        with open("4masala.css", "r") as f:
            self.setStyleSheet(f.read())

app = QApplication([])
window = InfoCollector()
window.show()
app.exec_()
