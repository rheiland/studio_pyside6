from PySide6.QtWidgets import QRadioButton, QButtonGroup

class MyRadioButton(QRadioButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        # Add custom functionality here
        self.clicked.connect(self.handle_click)

    def handle_click(self):
        print("MyRadioButton clicked:", self.text())

def handle_click():
    print("handle_click(): ---- ")

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    random_seed_gp = QButtonGroup()
    random_seed_gp.idToggled.connect(handle_click)
    random_seed_gp_next_id = 0

    radio1 = MyRadioButton("Option 1")
    radio2 = MyRadioButton("Option 2")
    random_seed_gp.addButton(radio1)
    random_seed_gp.addButton(radio2)
    layout.addWidget(radio1)
    layout.addWidget(radio2)
    radio1.setChecked(True)
    radio2.setChecked(True)

    window.setLayout(layout)
    window.show()
    app.exec()
