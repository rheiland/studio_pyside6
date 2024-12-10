import sys
from PySide6.QtWidgets import QRadioButton
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

class MyRadioButton(QRadioButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def setChecked(self, checked):
        super().setChecked(checked)
        # Add any additional functionality here if needed


app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

radio1 = MyRadioButton("Option 1")
radio2 = MyRadioButton("Option 2")

layout.addWidget(radio1)
layout.addWidget(radio2)
window.setLayout(layout)
window.show()

# Set the second radio button to checked
radio2.setChecked(True)

sys.exit(app.exec())
