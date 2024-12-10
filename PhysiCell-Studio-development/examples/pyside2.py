from PySide6.QtWidgets import QLineEdit

class MyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Add custom behavior here

    # Example: Overriding a method
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            print("Enter key pressed!")
        super().keyPressEvent(event)
