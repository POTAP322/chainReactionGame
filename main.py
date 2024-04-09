from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image

from ui import Ui_MainWindow


class MyMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.button_list = [self.ui.gameFieldButton1, self.ui.gameFieldButton2, self.ui.gameFieldButton3,
                            self.ui.gameFieldButton4, self.ui.gameFieldButton5, self.ui.gameFieldButton6,
                            self.ui.gameFieldButton7, self.ui.gameFieldButton8, self.ui.gameFieldButton9]
        self.pressedButtonsDict = {}
        self.levels = ["levels/level1", "levels.level2"]
        self.curLevel = 1
        self.updateLevel(self.curLevel)


        self.ui.gameFieldButton1.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton2.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton3.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton4.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton5.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton6.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton7.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton8.clicked.connect(self.addCrossToButton)
        self.ui.gameFieldButton9.clicked.connect(self.addCrossToButton)
        self.ui.backButton.clicked.connect(self.reduceLevel)
        self.ui.nextButton.clicked.connect(self.increaseLevel)
        self.ui.restartButton.clicked.connect(self.restartLevel)




    def addCrossToButton(self):
        button = self.sender()

        #шобы кнопки по два раза не нажимались
        if hasattr(button, 'is_clicked') and button.is_clicked:
            return
        button.is_clicked = True

        index = self.button_list.index(button)
        i, j = index // 3, index % 3

        if self.curLevel == 1:
            file = open('levels/level1', 'r')
        elif self.curLevel == 2:
            file = open('levels/level2', 'r')
        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        if matrix[i][j] == 0:
            img = Image.open('images/blueCircle.png')
        elif matrix[i][j] == 1:
            img = Image.open('images/redCircle.png')
        elif matrix[i][j] == 2:
            img = Image.open('images/blueSquare.png')
        elif matrix[i][j] == 3:
            img = Image.open('images/redSquare.png')

        cross = Image.open('images/cross.png')
        img.paste(cross, (40, 40), cross)
        img.save('new_image.png')

        button.setIcon(QIcon('new_image.png'))

        if len(self.pressedButtonsDict) > 0:
            self.addWhiteCrossToButtons()

        self.pressedButtonsDict[button] = img



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

            self.updateLevel(self.curLevel)

    def reduceLevel(self):
        if self.curLevel > 1:
            self.curLevel -= 1
            self.ui.levelLable.setText(str(self.curLevel))

            self.updateLevel(self.curLevel)

    def updateLevel(self, level):
        if level == 1:
            file = open('levels/level1', 'r')
        elif level == 2:
            file = open('levels/level2', 'r')
        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        # i - счётчик шобы понимать какую кнопку менять
        i = 0
        while i < len(self.button_list):
            for j in range(0, len(matrix)):
                for k in range(0, len(matrix[0])):
                    if matrix[j][k] == 0:
                        self.button_list[i].setIcon(QIcon('images/blueCircle.png'))
                        i += 1
                    elif matrix[j][k] == 1:
                        self.button_list[i].setIcon(QIcon('images/redCircle.png'))
                        i += 1
                    elif matrix[j][k] == 2:
                        self.button_list[i].setIcon(QIcon('images/blueSquare.png'))
                        i += 1
                    elif matrix[j][k] == 3:
                        self.button_list[i].setIcon(QIcon('images/redSquare.png'))
                        i += 1
        self.pressedButtonsDict.clear()

        #шобы кнопки нажимались после обновления экрана
        for button in self.button_list:
            button.is_clicked = False
    def restartLevel(self):
        self.updateLevel(self.curLevel)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
