from PySide6.QtWidgets import QMainWindow, QApplication

class MyWindow(QMainWindow):  # QMainWindow is the direct base class
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
