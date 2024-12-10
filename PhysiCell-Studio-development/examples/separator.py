import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QFrame, QVBoxLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()

    label1 = QLabel("Label 1")
    layout.addWidget(label1)

    separator = QFrame()
    separator.setFrameShape(QFrame.HLine)
    separator.setFrameShadow(QFrame.Sunken) 
    layout.addWidget(separator)

    label2 = QLabel("Label 2")
    layout.addWidget(label2)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())
