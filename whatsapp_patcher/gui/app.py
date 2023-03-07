import sys
from PySide6.QtWidgets import QApplication
from whatsapp_patcher.gui.windows.mainwindow_ui import MainWindow_Ui


def main():
    app = QApplication(sys.argv)

    window = MainWindow_Ui()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
