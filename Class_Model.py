from PyQt6.QtCore import QObject, pyqtSignal


class Model(QObject):

    changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.__number_a = 0
        self.__number_b = 0
        self.__number_c = 0

        self.__min_value = 0
        self.__max_value = 100

        self.__loadData()

    def __makeInRange(self, number: int):
        if self.__min_value <= number <= self.__max_value:
            return number
        elif abs(number - self.__max_value) < abs(number - self.__min_value):
            return self.__max_value
        return self.__min_value

    def getNumberA(self):
        return self.__number_a
    def getNumberB(self):
        return self.__number_b
    def getNumberC(self):
        return self.__number_c
    def getMinValue(self):
        return self.__min_value
    def getMaxValue(self):
        return self.__max_value


    def __handlingNumber(self, number: str):
        number = int(number)
        return self.__makeInRange(number)

    def setNumberA(self, number_a: str):
        try:
            self.__number_a = self.__handlingNumber(number_a)
        except ValueError:
            self.__number_a = self.getNumberA()

        if self.__number_a > self.__number_c:
            self.__number_c = self.__number_a
            self.__number_b = self.__number_a
        elif self.__number_a > self.__number_b:
            self.__number_b = self.__number_a
        self.__update()

    def setNumberB(self, number_b: str):
        try:
            self.__number_b = self.__handlingNumber(number_b)
        except ValueError:
            self.__number_b = self.getNumberB()

        if self.__number_b > self.__number_c:
            self.__number_b = self.__number_c
        elif self.__number_b < self.__number_a:
            self.__number_b = self.__number_a
        self.__update()

    def setNumberC(self, number_c: str):
        try:
            self.__number_c = self.__handlingNumber(number_c)
        except ValueError:
            self.__number_c = self.getNumberC()

        if self.__number_c < self.__number_a:
            self.__number_a = self.__number_c
            self.__number_b = self.__number_c
        elif self.__number_c < self.__number_b:
            self.__number_b = self.__number_c
        self.__update()

    def __update(self):
        self.changed.emit("Модель обновлена")

    def saveData(self):
        with open("data.txt", "w") as file:
            file.write(f"{str(self.__number_a)}\n")
            file.write(f"{str(self.__number_b)}\n")
            file.write(f"{str(self.__number_c)}\n")
    def __loadData(self):
        try:
            with open("data.txt", "r") as file:
                a = file.readline()
                b = file.readline()
                c = file.readline()
                self.setNumberC(c)
                self.setNumberB(b)
                self.setNumberA(a)
        except FileNotFoundError:
            pass
