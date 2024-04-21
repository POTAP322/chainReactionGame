import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PIL import Image
import collections

# Импортируем ваши пользовательские модули
from ui import Ui_MainWindow
from ui.ui2 import Ui_MainWindow2
from ui.info import Ui_infoForm

# Ваш класс ModalWindow остается без изменений
class ModalWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Победа")
        self.setFixedSize(200, 100)
        self.textLabel = QtWidgets.QLabel(self)
        self.textLabel.setText("Вы прошли этот уровень!")

# Ваш класс InfoWindow остается без изменений
class InfoWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.infoForm = Ui_infoForm()
        self.infoForm.setupUi(self)

# Ваш класс Game остается без изменений
class Game:
    def __init__(self):
        self.button_list = []
        self.pressedButtonsDict = {}
        self.colorPathsDict = {1: "images/blueCircle.png", 2: "images/redCircle.png",
                               3: "images/blueSquare.png", 4: "images/redSquare.png",
                               5: "images/greenCircle.png", 6: "images/greenSquare.png"}
        self.usedFigures = []
        self.levels = ["levels/level1", "levels/level2", "levels/level3", "levels/level4"]
        self.curLevel = 1
        self.curGameFieldSize = 3

    # Ваш код для класса Game здесь...
    def makeAmove(self):
        button = self.sender()
        # можно ли ходить или нет
        if len(self.pressedButtonsDict) > 0:
            if not self.movePermission():
                return

        # шобы кнопки по два раза не нажимались
        if hasattr(button, 'is_clicked') and button.is_clicked == True:
            return
        button.is_clicked = True

        index = self.button_list.index(button)
        if self.curGameFieldSize == 3:
            i, j = index // 3, index % 3

        elif self.curGameFieldSize == 4:
            i, j = index // 4, index % 4

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
        elif matrix[i][j] == 5:
            img = Image.open('images/greenCircle.png')
            self.usedFigures.append('images/greenCircle.png')
        elif matrix[i][j] == 6:
            img = Image.open('images/greenSquare.png')
            self.usedFigures.append('images/greenSquare.png')
        elif matrix[i][j] == 0:
            img = Image.open('images/white.png')

        cross = Image.open('images/cross.png')

        img.paste(cross, (40, 40), cross)
        img.save('images/newImage.png')

        button.setIcon(QIcon('images/newImage.png'))

        if len(self.pressedButtonsDict) > 0:
            self.addWhiteCrossToButtons()

        self.pressedButtonsDict[button] = img

        self.victoryRule()

    def addWhiteCrossToButtons(self):
        for button, old_image in self.pressedButtonsDict.items():
            new_image = Image.open("images/whiteCross.png")
            old_image.paste(new_image, (40, 40), new_image)
            old_image.save('images/combinedImage.png')

            button.setIcon(QIcon('images/combinedImage.png'))

    def increaseLevel(self):
        if self.curLevel < len(self.levels):
            self.curLevel += 1
            a = self.ui.levelLable.text()
            self.ui.levelLable.setText(str(self.curLevel))
            b = self.ui.levelLable.text()
            self.updateLevel()
            self.ui.gameFieldButton1.click()

    def reduceLevel(self):
        if self.curLevel > 1:
            a = self.ui.levelLable.text()
            self.curLevel -= 1

            self.ui.levelLable.setText(str(self.curLevel))
            b = self.ui.levelLable.text()

            self.updateLevel()
            self.ui.gameFieldButton1.click()

    def updateLevel(self):

        file = open(self.levels[self.curLevel - 1], 'r')
        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        if len(matrix) > 3 and self.curGameFieldSize != 4:
            self.switchToUi(2)
        elif len(matrix) < 4 and self.curGameFieldSize != 3:
            self.switchToUi(1)

        # шобы кнопки нажимались после обновления экрана
        for button in self.button_list:
            button.is_clicked = False

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
                    elif matrix[j][k] == 5:
                        self.button_list[i].setIcon(QIcon('images/greenCircle.png'))
                        i += 1
                    elif matrix[j][k] == 6:
                        self.button_list[i].setIcon(QIcon('images/greenSquare.png'))
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
        # кнопка которую хочу нажать ( её индексы будут i,j)
        button = self.sender()
        index = self.button_list.index(button)
        # последня нажатая кнопка(её индексы будут k,n)
        [button2] = collections.deque(self.pressedButtonsDict, maxlen=1)
        index2 = self.button_list.index(button2)

        if self.curGameFieldSize == 3:
            i, j = index // 3, index % 3
            k, n = index2 // 3, index2 % 3

        elif self.curGameFieldSize == 4:
            i, j = index // 4, index % 4
            k, n = index2 // 4, index2 % 4
        file = open(self.levels[self.curLevel - 1], 'r')

        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]

        lastButtonFigure = self.usedFigures[-1]

        a = matrix[i][j]
        if i == k or j == n:
            if matrix[i][j] == 1:  # если след клетка синий круг
                if lastButtonFigure == 'images/blueCircle.png' or lastButtonFigure == 'images/redCircle.png' or lastButtonFigure == 'images/blueSquare.png' or lastButtonFigure == 'images/greenCircle.png':
                    return True
            elif matrix[i][j] == 2:  # если след клетка красный круг
                if lastButtonFigure == 'images/redCircle.png' or lastButtonFigure == 'images/blueCircle.png' or lastButtonFigure == 'images/redSquare.png' or lastButtonFigure == 'images/greenCircle.png':
                    return True
            elif matrix[i][j] == 3:  # если след клетка синий квадрат
                if lastButtonFigure == 'images/blueSquare.png' or lastButtonFigure == 'images/blueCircle.png' or lastButtonFigure == 'images/redSquare.png' or lastButtonFigure == 'images/greenSquare.png':
                    return True
            elif matrix[i][j] == 4:  # если след клетка красный квадрат
                if lastButtonFigure == 'images/redSquare.png' or lastButtonFigure == 'images/redCircle.png' or lastButtonFigure == 'images/blueSquare.png' or lastButtonFigure == 'images/greenSquare.png':
                    return True
            elif matrix[i][j] == 5:  # если след клетка зелёный круг
                if lastButtonFigure == 'images/greenCircle.png' or lastButtonFigure == 'images/redCircle.png' or lastButtonFigure == 'images/blueCircle.png' or lastButtonFigure == 'images/greenSquare.png':
                    return True
            elif matrix[i][j] == 6:  # если след клетка зелёный квадрат
                if lastButtonFigure == 'images/greenSquare.png' or lastButtonFigure == 'images/redSquare.png' or lastButtonFigure == 'images/blueSquare.png' or lastButtonFigure == 'images/greenCircle.png':
                    return True
            elif matrix[i][j] == 0:  # если след клетка пустая
                return True
            return False
        return False

    def victoryRule(self):

        file = open(self.levels[self.curLevel - 1], 'r')
        lines = file.readlines()
        matrix = [line.strip().split() for line in lines]
        matrix = [[int(num) for num in row] for row in matrix]
        empyFieldsCount = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    empyFieldsCount += 1
        if len(self.pressedButtonsDict) == len(self.button_list) - empyFieldsCount:
            self.openVictoryWindow()



# Ваш класс MyMainWindow теперь будет использовать экземпляр класса Game для управления логикой игры
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui2 = Ui_MainWindow2()
        self.ui.setupUi(self)

        # Создаем экземпляр класса Game
        self.game = Game()

        # Используем атрибуты класса Game вместо атрибутов класса MyMainWindow
        self.button_list = self.game.button_list
        self.pressedButtonsDict = self.game.pressedButtonsDict
        self.colorPathsDict = self.game.colorPathsDict
        self.usedFigures = self.game.usedFigures
        self.levels = self.game.levels
        self.curLevel = self.game.curLevel
        self.curGameFieldSize = self.game.curGameFieldSize

        # Ваш код для класса MyMainWindow здесь...
        self.game.updateLevel()

        self.ui.gameFieldButton1.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton1.click()
        self.ui.gameFieldButton2.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton3.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton4.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton5.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton6.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton7.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton8.clicked.connect(self.game.makeAmove)
        self.ui.gameFieldButton9.clicked.connect(self.game.makeAmove)

        self.ui.backButton.clicked.connect(self.game.reduceLevel)
        self.ui.nextButton.clicked.connect(self.game.increaseLevel)
        self.ui.restartButton.clicked.connect(self.game.restartLevel)
        self.ui.infoButton.clicked.connect(self.openInfoWindow)

    def switchToUi(self, uiNum):
        # Сохраняем текущие значения
        curLevel = self.curLevel
        levelLable = self.ui.levelLable.text()
        pressedButtonsDict = self.pressedButtonsDict
        colorPathsDict = self.colorPathsDict
        usedFigures = self.usedFigures
        levels = self.levels

        if uiNum == 1:
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setFixedSize(400, 420)
            self.curGameFieldSize = 3
            # Обновляем список кнопок
            self.button_list = [self.ui.gameFieldButton1, self.ui.gameFieldButton2, self.ui.gameFieldButton3,
                                self.ui.gameFieldButton4, self.ui.gameFieldButton5, self.ui.gameFieldButton6,
                                self.ui.gameFieldButton7, self.ui.gameFieldButton8, self.ui.gameFieldButton9]
        if uiNum == 2:
            self.ui = self.ui2
            self.ui.setupUi(self)
            self.curGameFieldSize = 4
            a = self.size()
            # Обновляем список кнопок
            self.button_list = [self.ui.gameFieldButton1, self.ui.gameFieldButton2, self.ui.gameFieldButton3,
                                self.ui.gameFieldButton4, self.ui.gameFieldButton5, self.ui.gameFieldButton6,
                                self.ui.gameFieldButton7, self.ui.gameFieldButton8, self.ui.gameFieldButton9,
                                self.ui.gameFieldButton10, self.ui.gameFieldButton11, self.ui.gameFieldButton12,
                                self.ui.gameFieldButton13, self.ui.gameFieldButton14, self.ui.gameFieldButton15,
                                self.ui.gameFieldButton16]

        # Восстанавливаем сохраненные значения
        self.curLevel = curLevel
        self.ui.levelLable.setText(levelLable)
        self.pressedButtonsDict = pressedButtonsDict
        self.colorPathsDict = colorPathsDict
        self.usedFigures = usedFigures
        self.levels = levels

        # Подключаем кнопки
        for button in self.button_list:
            button.clicked.connect(self.game.makeAmove)
        self.ui.backButton.clicked.connect(self.game.reduceLevel)
        self.ui.nextButton.clicked.connect(self.game.increaseLevel)
        self.ui.restartButton.clicked.connect(self.game.restartLevel)
        self.ui.infoButton.clicked.connect(self.openInfoWindow)

    def openVictoryWindow(self):
        self.modalWindow = ModalWindow(self)
        self.modalWindow.exec_()

    def openInfoWindow(self):
        self.infoWindow = InfoWindow()
        self.infoWindow.show()


# Ваш основной блок кода остается без изменений
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())