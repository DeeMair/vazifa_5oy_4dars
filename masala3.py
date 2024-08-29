from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class RestaurantMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restoran Menyusi")
        self.setGeometry(100, 100, 800, 600)

        self.menu = {
            "1-taomlar": [("Pizza", 15), ("Burger", 10), ("Pasta", 12), ("Salad", 8), ("Soup", 7)],
            "2-taomlar": [("Steak", 20), ("Chicken", 18), ("Fish", 17), ("Ribs", 22), ("Lamb", 25)],
            "Ichimliklar": [("Cola", 3), ("Juice", 4), ("Water", 2), ("Tea", 3), ("Coffee", 5)],
            "Desert": [("Ice Cream", 6), ("Cake", 7), ("Pie", 5), ("Pudding", 4), ("Cookies", 3)]
        }

        self.images = {
            "Pizza": "restoran_pictures/pizza.jpg",
            "Burger": "restoran_pictures/burger.jpg",
            "Pasta": "restoran_pictures/pasta.jpg",
            "Salad": "restoran_pictures/salad.jpg",
            "Soup": "restoran_pictures/soup.jpg",
            "Steak": "restoran_pictures/steak.jpg",
            "Chicken": "restoran_pictures/chicken.jpg",
            "Fish": "restoran_pictures/fish.jpg",
            "Ribs": "restoran_pictures/ribs.jpg",
            "Lamb": "restoran_pictures/lamb.jpg",
            "Cola": "restoran_pictures/cola.jpg",
            "Juice": "restoran_pictures/juice.jpg",
            "Water": "restoran_pictures/water.jpg",
            "Tea": "restoran_pictures/tea.jpg",
            "Coffee": "restoran_pictures/coffee.jpg",
            "Ice Cream": "restoran_pictures/ice_cream.jpg",
            "Cake": "restoran_pictures/cake.jpg",
            "Pie": "restoran_pictures/pie.jpg",
            "Pudding": "restoran_pictures/pudding.jpg",
            "Cookies": "restoran_pictures/cookies.jpg"
        }

        self.selected_items = {
            "1-taomlar": [],
            "2-taomlar": [],
            "Ichimliklar": [],
            "Desert": []
        }

        self.widget = QWidget()
        self.layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout()

        self.checkboxes = {}
        for category, items in self.menu.items():
            label = QLabel(category, self)
            self.scroll_layout.addWidget(label)
            self.checkboxes[category] = []
            for item, price in items:
                checkbox_layout = QVBoxLayout()
                checkbox = QCheckBox(f"{item} - ${price}", self)
                checkbox_layout.addWidget(checkbox)

                image_label = QLabel(self)
                pixmap = QPixmap(self.images[item])
                image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
                checkbox_layout.addWidget(image_label)

                self.scroll_layout.addLayout(checkbox_layout)
                self.checkboxes[category].append((checkbox, item, price))

        self.check_button = QPushButton("Chek", self)
        self.check_button.clicked.connect(self.show_checklist)
        self.scroll_layout.addWidget(self.check_button)

        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)

        self.layout.addWidget(self.scroll_area)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.load_styles()

    def show_checklist(self):
        result = []
        for category, checkboxes in self.checkboxes.items():
            selected_items = [f"{item} - ${price}" for checkbox, item, price in checkboxes if checkbox.isChecked()]
            if selected_items:
                result.append(f"{category}: {', '.join(selected_items)}")

        if not result:
            result = ["Hech narsa tanlanmagan."]
        else:
            result = '\n'.join(result)

        msg_box = QMessageBox()
        msg_box.setText(result)
        msg_box.exec_()

    def load_styles(self):
        with open("restoran.css", "r") as file:
            style = file.read()
            self.setStyleSheet(style)

app = QApplication([])
window = RestaurantMenu()
window.show()
app.exec_()
