from PyQt6.QtWidgets import QMainWindow
from Class_HorizontalSlider import HorizontalSlider
from Class_Label import Label
from Class_LineEdit import LineEdit
from Class_Model import Model
from Class_SpinBox import SpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__model = Model()
        self.__model.changed.connect(self.__updateData)

        self.__label_a = Label(self, 40, 40, 150, 100)
        self.__label_b = Label(self, 340, 40, 150, 100)
        self.__label_c = Label(self, 640, 40, 150, 100)
        self.__label_comparison_operator_left = Label(self,190, 40, 150, 100)
        self.__label_comparison_operator_right = Label(self, 490, 40, 150, 100)


        self.__line_edit_a = LineEdit(self, 40, 140, 150, 50)
        self.__line_edit_b = LineEdit(self, 340, 140, 150, 50)
        self.__line_edit_c = LineEdit(self, 640, 140, 150, 50)
        self.__line_edit_a.editingFinished.connect(
            lambda: self.__model.setNumberA(self.__line_edit_a.text())
        )
        self.__line_edit_b.editingFinished.connect(
            lambda: self.__model.setNumberB(self.__line_edit_b.text())
        )
        self.__line_edit_c.editingFinished.connect(
            lambda: self.__model.setNumberC(self.__line_edit_c.text())
        )

        self.__spinbox_a = SpinBox(self, 40, 200, 150, 50)
        self.__spinbox_b = SpinBox(self, 340, 200, 150, 50)
        self.__spinbox_c = SpinBox(self, 640, 200, 150, 50)
        self.__spinbox_a.editingFinished.connect(
            lambda: self.__model.setNumberA(self.__spinbox_a.text())
        )
        self.__spinbox_b.editingFinished.connect(
            lambda: self.__model.setNumberB(self.__spinbox_b.text())
        )
        self.__spinbox_c.editingFinished.connect(
            lambda: self.__model.setNumberC(self.__spinbox_c.text())
        )

        self.__h_slider_a = HorizontalSlider(self, 40, 250, 150, 50)
        self.__h_slider_b = HorizontalSlider(self, 340, 250, 150, 50)
        self.__h_slider_c = HorizontalSlider(self, 640, 250, 150, 50)
        self.__h_slider_a.valueChanged.connect(
            lambda: self.__model.setNumberA(str(self.__h_slider_a.value()))
        )
        self.__h_slider_b.valueChanged.connect(
            lambda: self.__model.setNumberB(str(self.__h_slider_b.value()))
        )
        self.__h_slider_c.valueChanged.connect(
            lambda: self.__model.setNumberC(str(self.__h_slider_c.value()))
        )

        self.__initUI()

    def __initUI(self):
        self.setFixedSize(840, 400)
        self.setStyleSheet(
            """
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
            """
        )
        self.setFocus()

        self.__label_comparison_operator_left.setText("<=")
        self.__label_comparison_operator_right.setText("<=")

        self.__spinbox_a.setMaximum(self.__model.getMaxValue())
        self.__spinbox_a.setMinimum(self.__model.getMinValue())

        self.__spinbox_b.setMaximum(self.__model.getMaxValue())
        self.__spinbox_b.setMinimum(self.__model.getMinValue())

        self.__spinbox_c.setMaximum(self.__model.getMaxValue())
        self.__spinbox_c.setMinimum(self.__model.getMinValue())

        self.__h_slider_a.setMaximum(self.__model.getMaxValue())
        self.__h_slider_a.setMinimum(self.__model.getMinValue())

        self.__h_slider_b.setMaximum(self.__model.getMaxValue())
        self.__h_slider_b.setMinimum(self.__model.getMinValue())

        self.__h_slider_c.setMaximum(self.__model.getMaxValue())
        self.__h_slider_c.setMinimum(self.__model.getMinValue())

        self.__updateData()

    def __updateData(self):
        self.__label_a.setText(str(self.__model.getNumberA()))
        self.__label_b.setText(str(self.__model.getNumberB()))
        self.__label_c.setText(str(self.__model.getNumberC()))

        self.__line_edit_a.setText(str(self.__model.getNumberA()))
        self.__line_edit_b.setText(str(self.__model.getNumberB()))
        self.__line_edit_c.setText(str(self.__model.getNumberC()))

        self.__spinbox_a.setValue(self.__model.getNumberA())
        self.__spinbox_b.setValue(self.__model.getNumberB())
        self.__spinbox_c.setValue(self.__model.getNumberC())

        self.__h_slider_a.setValue(self.__model.getNumberA())
        self.__h_slider_b.setValue(self.__model.getNumberB())
        self.__h_slider_c.setValue(self.__model.getNumberC())



    def mousePressEvent(self, a0):
        self.setFocus()
    def closeEvent(self, a0):
        self.__model.saveData()

