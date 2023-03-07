from PySide6.QtWidgets import QMainWindow


class MainWindow_Ui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WhatsApp Patcher")
        self.resize(410, 510)
