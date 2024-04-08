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
        self.levels = ["levels/level1","levels.level2"]
        self.curLevel = 1
        self.updateLevel(self.curLevel)

        self.ui.gameFieldButton1.clicked.connect(self.buttonClicked)
        self.ui.backButton.clicked.connect(self.reduceLevel)
        self.ui.nextButton.clicked.connect(self.increaseLevel)
        self.ui.restartButton.clicked.connect(self.restartLevel)




        #self.ui.levelLable.setText("Level: " + level)
    def buttonClicked(self):
        button = self.sender()

        button.setDisabled(True)
        button.setIconSize(QtCore.QSize(50,50))
        image = Image.open('images/blueCircle.png')
        cross = Image.open('images/cross.png')

        image.paste(cross, (40, 40), cross)

        image.save('new_image.png')

        # Измените изображение на кнопке
        button.setIcon(QIcon('new_image.png'))

        # button.setText("X")
        # print("click")

    def increaseLevel(self):
        currentLevel = int(self.ui.levelLable.text())
        if currentLevel <len(self.levels):
            newLevel = currentLevel + 1
            self.ui.levelLable.setText(str(newLevel))

            self.updateLevel(newLevel)


    def reduceLevel(self):
        currentLevel = int(self.ui.levelLable.text())
        if currentLevel > 1:
            newLevel = currentLevel - 1
            self.ui.levelLable.setText(str(newLevel))

            self.updateLevel(newLevel)


    def updateLevel(self, level):
        if level == 1:
            file = open('levels/level1', 'r')
        elif level == 2:
            file = open('levels/level2', 'r')
        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        #i - счётчик шобы понимать какую кнопку менять
        i = 0
        while i < len(self.button_list):
            for j in range(0,len(matrix)):
                for k in range(0,len(matrix[0])):
                    if matrix[j][k] == 0:
                        self.button_list[i].setIcon(QIcon('images/blueCircle.png'))
                        i += 1
                    elif matrix[j][k] == 1:
                        self.button_list[i].setIcon(QIcon('images/redCircle.png'))
                        i+=1
                    elif matrix[j][k] == 2:
                        self.button_list[i].setIcon(QIcon('images/blueSquare.png'))
                        i+=1
                    elif matrix[j][k] == 3:
                        self.button_list[i].setIcon(QIcon('images/redSquare.png'))
                        i+=1

    def restartLevel(self):
        for button in self.button_list:
            button.setText("")
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
