from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider

class HorizontalSlider(QSlider):
    def __init__(self, parent, x: int, y: int, w: int, h: int):
        super().__init__(parent)
        self.__initUI(x, y, w, h)
    def __initUI(self, x: int, y: int, w: int, h: int):
        self.setGeometry(x, y, w, h)
        self.setOrientation(Qt.Orientation.Horizontal)
