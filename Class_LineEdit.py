from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    def __init__(self, parent, x: int, y: int, w: int, h: int):
        super().__init__(parent)
        self.__initUI(x, y, w, h)
    def __initUI(self, x: int, y: int, w: int, h: int):
        self.setGeometry(x, y, w, h)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setStyleSheet(
            """
                font: 24pt;
            """
        )

