from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image

from ui import Ui_MainWindow


class ModalWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Победа")
        self.setFixedSize(200, 100)
        self.textLabel = QtWidgets.QLabel(self)
        self.textLabel.setText("Вы прошли этот уровень!")


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.button_list = [self.ui.gameFieldButton1, self.ui.gameFieldButton2, self.ui.gameFieldButton3,
                            self.ui.gameFieldButton4, self.ui.gameFieldButton5, self.ui.gameFieldButton6,
                            self.ui.gameFieldButton7, self.ui.gameFieldButton8, self.ui.gameFieldButton9]
        self.pressedButtonsDict = {}
        self.colorPathsDict = {1: "images/blueCircle.png", 2: "images/redCircle.png",
                               3: "images/blueSquare.png", 4: "images/redSquare.png"}
        self.usedFigures = []
        self.levels = ["levels/level1", "levels/level2", "levels/level3"]
        self.curLevel = 1
        self.updateLevel()

        self.ui.gameFieldButton1.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton1.click()
        self.ui.gameFieldButton2.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton3.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton4.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton5.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton6.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton7.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton8.clicked.connect(self.makeAmove)
        self.ui.gameFieldButton9.clicked.connect(self.makeAmove)

        self.ui.backButton.clicked.connect(self.reduceLevel)
        self.ui.nextButton.clicked.connect(self.increaseLevel)
        self.ui.restartButton.clicked.connect(self.restartLevel)

    def open_modal_window(self):
        self.modal_window = ModalWindow(self)
        self.modal_window.exec_()

    def makeAmove(self):
        button = self.sender()

        if len(self.pressedButtonsDict) > 0:
            if not self.movePermission():
                return

        # шобы кнопки по два раза не нажимались
        if hasattr(button, 'is_clicked') and button.is_clicked == True:
            return
        button.is_clicked = True

        index = self.button_list.index(button)
        i, j = index // 3, index % 3

        # выбор уровня
        file = open(self.levels[self.curLevel - 1], 'r')

        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        if matrix[i][j] == 1:
            img = Image.open('images/blueCircle.png')
            self.usedFigures.append('images/blueCircle.png')
        elif matrix[i][j] == 2:
            img = Image.open('images/redCircle.png')
            self.usedFigures.append('images/redCircle.png')
        elif matrix[i][j] == 3:
            img = Image.open('images/blueSquare.png')
            self.usedFigures.append('images/blueSquare.png')
        elif matrix[i][j] == 4:
            img = Image.open('images/redSquare.png')
            self.usedFigures.append('images/redSquare.png')
        elif matrix[i][j] == 0:
            img = Image.open('images/white.png')



        cross = Image.open('images/cross.png')

        img.paste(cross, (40, 40), cross)
        img.save('new_image.png')

        button.setIcon(QIcon('new_image.png'))

        if len(self.pressedButtonsDict) > 0:
            self.addWhiteCrossToButtons()

        self.pressedButtonsDict[button] = img

        self.victoryRule()

    def addWhiteCrossToButtons(self):
        for button, old_image in self.pressedButtonsDict.items():
            new_image = Image.open("images/whiteCross.png")
            old_image.paste(new_image, (40, 40), new_image)
            old_image.save('combined_image.png')

            button.setIcon(QIcon('combined_image.png'))

    def increaseLevel(self):
        if self.curLevel < len(self.levels):
            self.curLevel += 1
            self.ui.levelLable.setText(str(self.curLevel))

            self.updateLevel()
            self.ui.gameFieldButton1.click()

    def reduceLevel(self):
        if self.curLevel > 1:
            self.curLevel -= 1
            self.ui.levelLable.setText(str(self.curLevel))

            self.updateLevel()
            self.ui.gameFieldButton1.click()

    def updateLevel(self):
        # шобы кнопки нажимались после обновления экрана
        for button in self.button_list:
            button.is_clicked = False

        file = open(self.levels[self.curLevel - 1], 'r')

        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        # i - счётчик шобы понимать какую кнопку менять
        i = 0
        while i < len(self.button_list):
            for j in range(0, len(matrix)):
                for k in range(0, len(matrix[0])):
                    a = matrix[j][k]
                    if matrix[j][k] == 1:
                        self.button_list[i].setIcon(QIcon('images/blueCircle.png'))
                        i += 1
                    elif matrix[j][k] == 2:
                        self.button_list[i].setIcon(QIcon('images/redCircle.png'))
                        i += 1
                    elif matrix[j][k] == 3:
                        self.button_list[i].setIcon(QIcon('images/blueSquare.png'))
                        i += 1
                    elif matrix[j][k] == 4:
                        self.button_list[i].setIcon(QIcon('images/redSquare.png'))
                        i += 1
                    elif matrix[j][k] == 0:
                        self.button_list[i].setIcon(QIcon('images/white.png'))
                        self.button_list[i].is_clicked = True
                        i += 1



        self.pressedButtonsDict.clear()





    def restartLevel(self):
        self.updateLevel()
        self.ui.gameFieldButton1.click()

    def movePermission(self):
        button = self.sender()
        index = self.button_list.index(button)
        i, j = index // 3, index % 3
        file = open(self.levels[self.curLevel - 1], 'r')

        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        lastButtonFigure = self.usedFigures[-1]

        a = matrix[i][j]
        if matrix[i][j] == 1:  # если след клетка синий круг
            if lastButtonFigure == 'images/blueCircle.png' or lastButtonFigure == 'images/redCircle.png' or lastButtonFigure == 'images/blueSquare.png':
                return True
        elif matrix[i][j] == 2:  # если след клетка красный круг
            if lastButtonFigure == 'images/redCircle.png' or lastButtonFigure == 'images/blueCircle.png' or lastButtonFigure == 'images/redSquare.png':
                return True
        elif matrix[i][j] == 3:  # если след клетка синий квадрат
            if lastButtonFigure == 'images/blueSquare.png' or lastButtonFigure == 'images/blueCircle.png' or lastButtonFigure == 'images/redSquare.png':
                return True
        elif matrix[i][j] == 4:  # если след клетка красный квадрат
            if lastButtonFigure == 'images/redSquare.png' or lastButtonFigure == 'images/redCircle.png' or lastButtonFigure == 'images/blueSquare.png':
                return True
        elif matrix[i][j] == 0:  # если след клетка пустая
            return True
        return False

    def victoryRule(self):
        self.modal_window = ModalWindow(self)
        if len(self.pressedButtonsDict) == len(self.button_list):
            self.modal_window.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
