# Use Py2Wasm to compile a simple PySide6 application
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello from PySide6 in WebAssembly!")
label.show()
app.exec_()
