from PyQt5 import QtWidgets
from PyQt5.QtGui import *

from PIL import Image
import collections

from ui.ui import Ui_MainWindow
from ui.ui2 import Ui_MainWindow2
from ui.info import Ui_infoForm


class ModalWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Победа")
        self.setFixedSize(200, 100)
        self.textLabel = QtWidgets.QLabel(self)
        self.textLabel.setText("Вы прошли этот уровень!")


class InfoWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.infoForm = Ui_infoForm()
        self.infoForm.setupUi(self)


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui2 = Ui_MainWindow2()
        self.ui.setupUi(self)

        self.game = GameLogic(self)

        self.gameButtonsList = [self.ui.gameFieldButton1, self.ui.gameFieldButton2, self.ui.gameFieldButton3,
                                self.ui.gameFieldButton4, self.ui.gameFieldButton5, self.ui.gameFieldButton6,
                                self.ui.gameFieldButton7, self.ui.gameFieldButton8, self.ui.gameFieldButton9]
        self.pressedButtonsDict = {}
        self.imagesPathDict = {1: "images/blueCircle.png", 2: "images/redCircle.png",
                               3: "images/blueSquare.png", 4: "images/redSquare.png",
                               5: "images/greenCircle.png", 6: "images/greenSquare.png", 7: 'images/cross.png',
                               8: "images/whiteCross.png", 9: "images/white.png"}
        self.usedFigures = []
        self.levels = ["levels/level1", "levels/level2", "levels/level3", "levels/level4"]
        self.curLevel = 1
        self.curGameFieldSize = 3
        self.game.updateLevel()

        self.ui.gameFieldButton1.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton1.click()
        for button in self.gameButtonsList:
            button.clicked.connect(self.game.makeAmove)

        self.ui.backButton.clicked.connect(self.reduceLevel)
        self.ui.nextButton.clicked.connect(self.increaseLevel)
        self.ui.restartButton.clicked.connect(self.restartLevel)
        self.ui.infoButton.clicked.connect(self.openInfoWindow)

    def switchToUi(self, uiNum):
        # Сохраняем текущие значения
        curLevel = self.curLevel
        levelLable = self.ui.levelLable.text()
        pressedButtonsDict = self.pressedButtonsDict
        colorPathsDict = self.imagesPathDict
        usedFigures = self.usedFigures
        levels = self.levels

        if uiNum == 1:
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setFixedSize(400, 420)
            self.curGameFieldSize = 3
            # Обновляем список кнопок
            self.gameButtonsList = [self.ui.gameFieldButton1, self.ui.gameFieldButton2, self.ui.gameFieldButton3,
                                    self.ui.gameFieldButton4, self.ui.gameFieldButton5, self.ui.gameFieldButton6,
                                    self.ui.gameFieldButton7, self.ui.gameFieldButton8, self.ui.gameFieldButton9]
        if uiNum == 2:
            self.ui = self.ui2
            self.ui.setupUi(self)
            self.curGameFieldSize = 4
            a = self.size()
            # Обновляем список кнопок
            self.gameButtonsList = [self.ui.gameFieldButton1, self.ui.gameFieldButton2, self.ui.gameFieldButton3,
                                    self.ui.gameFieldButton4, self.ui.gameFieldButton5, self.ui.gameFieldButton6,
                                    self.ui.gameFieldButton7, self.ui.gameFieldButton8, self.ui.gameFieldButton9,
                                    self.ui.gameFieldButton10, self.ui.gameFieldButton11, self.ui.gameFieldButton12,
                                    self.ui.gameFieldButton13, self.ui.gameFieldButton14, self.ui.gameFieldButton15,
                                    self.ui.gameFieldButton16]

        # Восстанавливаем сохраненные значения
        self.curLevel = curLevel
        self.ui.levelLable.setText(levelLable)
        self.pressedButtonsDict = pressedButtonsDict
        self.imagesPathDict = colorPathsDict
        self.usedFigures = usedFigures
        self.levels = levels

        # Подключаем кнопки
        for button in self.gameButtonsList:
            button.clicked.connect(self.game.makeAmove)
        self.ui.backButton.clicked.connect(self.reduceLevel)
        self.ui.nextButton.clicked.connect(self.increaseLevel)
        self.ui.restartButton.clicked.connect(self.restartLevel)
        self.ui.infoButton.clicked.connect(self.openInfoWindow)


    def openVictoryWindow(self):
        self.modalWindow = ModalWindow(self)
        self.modalWindow.exec_()

    def openInfoWindow(self):
        self.infoWindow = InfoWindow()
        self.infoWindow.show()

    def increaseLevel(self):
        if self.curLevel < len(self.levels):
            self.curLevel += 1
            a = self.ui.levelLable.text()
            self.ui.levelLable.setText(str(self.curLevel))
            b = self.ui.levelLable.text()
            self.game.updateLevel()
            self.ui.gameFieldButton1.click()

    def reduceLevel(self):
        if self.curLevel > 1:
            a = self.ui.levelLable.text()
            self.curLevel -= 1

            self.ui.levelLable.setText(str(self.curLevel))
            b = self.ui.levelLable.text()

            self.game.updateLevel()
            self.ui.gameFieldButton1.click()

    def restartLevel(self):
        self.game.updateLevel()
        self.ui.gameFieldButton1.click()


class GameLogic:
    def __init__(self, window: MyMainWindow):
        self.window = window

    def makeAmove(self):
        button = self.window.sender()
        # можно ли ходить или нет
        if len(self.window.pressedButtonsDict) > 0:
            if not self.movePermission:
                return
        if hasattr(button, 'is_clicked') and button.is_clicked == True:
            return
        button.is_clicked = True
        index = self.window.gameButtonsList.index(button)
        i, j = index // self.window.curGameFieldSize, index % self.window.curGameFieldSize

        with open(self.window.levels[self.window.curLevel - 1], 'r') as file:
            lines = file.readlines()
            matrix = [[int(num) for num in line.strip().split()] for line in lines]

        img_path = self.window.imagesPathDict[matrix[i][j]]
        img = Image.open(img_path)
        self.window.usedFigures.append(img_path)

        cross = Image.open('images/cross.png')
        img.paste(cross, (40, 40), cross)
        img.save('images/newImage.png')
        button.setIcon(QIcon('images/newImage.png'))

        if len(self.window.pressedButtonsDict) > 0:
            self.addWhiteCrossToPrevButton()

        self.window.pressedButtonsDict[button] = img
        # проверяем победили или нет
        self.victoryRule()

    def updateLevel(self):
        with open(self.window.levels[self.window.curLevel - 1], 'r') as file:
            lines = file.readlines()
            matrix = [[int(num) for num in line.strip().split()] for line in lines]

        if len(matrix) > 3 and self.window.curGameFieldSize != 4:
            self.window.switchToUi(2)
        elif len(matrix) < 4 and self.window.curGameFieldSize != 3:
            self.window.switchToUi(1)

        # шобы кнопки нажимались после обновления экрана
        for button in self.window.gameButtonsList:
            button.is_clicked = False

        # i - счётчик шобы понимать какую кнопку менять
        i = 0
        while i < len(self.window.gameButtonsList):
            for j in range(0, len(matrix)):
                for k in range(0, len(matrix[0])):
                    if matrix[j][k] in self.window.imagesPathDict:
                        self.window.gameButtonsList[i].setIcon(QIcon(self.window.imagesPathDict[matrix[j][k]]))
                        i += 1
                    elif matrix[j][k] == 0:
                        self.window.gameButtonsList[i].setIcon(QIcon('images/white.png'))
                        self.window.gameButtonsList[i].is_clicked = True
                        i += 1

        self.window.pressedButtonsDict.clear()

    @property
    def movePermission(self):
        # кнопка которую хочу нажать (её индексы будут i,j)
        button = self.window.sender()
        index = self.window.gameButtonsList.index(button)
        # последня нажатая кнопка(её индексы будут k,n)
        [button2] = collections.deque(self.window.pressedButtonsDict, maxlen=1)
        index2 = self.window.gameButtonsList.index(button2)

        i, j = index // self.window.curGameFieldSize, index % self.window.curGameFieldSize
        k, n = index2 // self.window.curGameFieldSize, index2 % self.window.curGameFieldSize

        with open(self.window.levels[self.window.curLevel - 1], 'r') as file:
            lines = file.readlines()
            matrix = [[int(num) for num in line.strip().split()] for line in lines]

        lastButtonFigure = self.window.usedFigures[-1]

        a = matrix[i][j]
        if i == k or j == n:
            figure_dict = {
                # если синий круг
                1: ['images/blueCircle.png', 'images/redCircle.png', 'images/blueSquare.png', 'images/greenCircle.png'],
                # если красный круг
                2: ['images/redCircle.png', 'images/blueCircle.png', 'images/redSquare.png', 'images/greenCircle.png'],
                # если синий квадрат
                3: ['images/blueSquare.png', 'images/blueCircle.png', 'images/redSquare.png', 'images/greenSquare.png'],
                # если след клетка красный квадрат
                4: ['images/redSquare.png', 'images/redCircle.png', 'images/blueSquare.png', 'images/greenSquare.png'],
                # если след клетка зелёный круг
                5: ['images/greenCircle.png', 'images/redCircle.png', 'images/blueCircle.png',
                    'images/greenSquare.png'],
                # если след клетка зелёный квадрат
                6: ['images/greenSquare.png', 'images/redSquare.png', 'images/blueSquare.png',
                    'images/greenCircle.png'],
                # если клетка пустая
                0: ['images/blueCircle.png', 'images/redCircle.png', 'images/blueSquare.png', 'images/greenCircle.png',
                    'images/redSquare.png', 'images/greenSquare.png', 'images/greenCircle.png']
            }
            if lastButtonFigure in figure_dict[matrix[i][j]]:
                return True
            return False
        return False


    def victoryRule(self):
        file = open(self.window.levels[self.window.curLevel - 1], 'r')
        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]
        empyFieldsCount = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    empyFieldsCount += 1
        if len(self.window.pressedButtonsDict) == len(self.window.gameButtonsList) - empyFieldsCount:
            self.window.openVictoryWindow()

    @staticmethod
    def addWhiteCrossToPrevButton():
        for button, old_image in window.pressedButtonsDict.items():
            new_image = Image.open("images/whiteCross.png")
            old_image.paste(new_image, (40, 40), new_image)
            old_image.save('images/combinedImage.png')

            button.setIcon(QIcon('images/combinedImage.png'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    game = GameLogic(window)
    window.show()
    sys.exit(app.exec_())
