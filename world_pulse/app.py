from __future__ import annotations
import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("World Pulse")
        self.resize(1200, 760)
        self.setCentralWidget(QLabel("World Pulse is ready"))

def run() -> None:
    application = QApplication.instance() or QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec())