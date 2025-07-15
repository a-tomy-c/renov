from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from skin_renov import Ui_Renov


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Renov()
        self.ui.setupUi(self)
        self._config_Ventana()

    def _config_Ventana(self):
        ...


if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    vn = Ventana()
    vn.show()
    sys.exit(app.exec())