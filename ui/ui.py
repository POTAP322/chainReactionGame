# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(400, 420))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setObjectName("centralwidget")
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setEnabled(True)
        self.restartButton.setGeometry(QtCore.QRect(150, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.restartButton.setFont(font)
        self.restartButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.restartButton.setMouseTracking(True)
        self.restartButton.setTabletTracking(False)
        self.restartButton.setDefault(False)
        self.restartButton.setFlat(True)
        self.restartButton.setObjectName("restartButton")
        self.levelLable = QtWidgets.QLabel(self.centralwidget)
        self.levelLable.setGeometry(QtCore.QRect(360, 10, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.levelLable.setFont(font)
        self.levelLable.setObjectName("levelLable")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(320, 30, 21, 21))
        self.backButton.setFlat(True)
        self.backButton.setObjectName("backButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(350, 30, 21, 21))
        self.nextButton.setFlat(True)
        self.nextButton.setObjectName("nextButton")
        self.gameFieldButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton1.setGeometry(QtCore.QRect(50, 80, 100, 100))
        self.gameFieldButton1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../1695961206_gas-kvas-com-p-kartinki-png-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gameFieldButton1.setIcon(icon)
        self.gameFieldButton1.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton1.setFlat(False)
        self.gameFieldButton1.setObjectName("gameFieldButton1")
        self.gameFieldButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton2.setGeometry(QtCore.QRect(150, 80, 100, 100))
        self.gameFieldButton2.setText("")
        self.gameFieldButton2.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton2.setFlat(False)
        self.gameFieldButton2.setObjectName("gameFieldButton2")
        self.gameFieldButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton3.setGeometry(QtCore.QRect(250, 80, 100, 100))
        self.gameFieldButton3.setText("")
        self.gameFieldButton3.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton3.setFlat(False)
        self.gameFieldButton3.setObjectName("gameFieldButton3")
        self.gameFieldButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton5.setGeometry(QtCore.QRect(150, 180, 100, 100))
        self.gameFieldButton5.setText("")
        self.gameFieldButton5.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton5.setFlat(False)
        self.gameFieldButton5.setObjectName("gameFieldButton5")
        self.gameFieldButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton6.setGeometry(QtCore.QRect(250, 180, 100, 100))
        self.gameFieldButton6.setText("")
        self.gameFieldButton6.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton6.setFlat(False)
        self.gameFieldButton6.setObjectName("gameFieldButton6")
        self.gameFieldButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton4.setGeometry(QtCore.QRect(50, 180, 100, 100))
        self.gameFieldButton4.setText("")
        self.gameFieldButton4.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton4.setFlat(False)
        self.gameFieldButton4.setObjectName("gameFieldButton4")
        self.gameFieldButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton8.setGeometry(QtCore.QRect(150, 280, 100, 100))
        self.gameFieldButton8.setText("")
        self.gameFieldButton8.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton8.setFlat(False)
        self.gameFieldButton8.setObjectName("gameFieldButton8")
        self.gameFieldButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton9.setGeometry(QtCore.QRect(250, 280, 100, 100))
        self.gameFieldButton9.setText("")
        self.gameFieldButton9.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton9.setFlat(False)
        self.gameFieldButton9.setObjectName("gameFieldButton9")
        self.gameFieldButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.gameFieldButton7.setGeometry(QtCore.QRect(50, 280, 100, 100))
        self.gameFieldButton7.setText("")
        self.gameFieldButton7.setIconSize(QtCore.QSize(88, 88))
        self.gameFieldButton7.setFlat(False)
        self.gameFieldButton7.setObjectName("gameFieldButton7")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(330, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.infoButton.setObjectName("infoButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.restartButton.setText(_translate("MainWindow", "Restart"))
        self.levelLable.setText(_translate("MainWindow", "1"))
        self.backButton.setText(_translate("MainWindow", "<"))
        self.nextButton.setText(_translate("MainWindow", ">"))
        self.label1.setText(_translate("MainWindow", "Level:"))
        self.infoButton.setText(_translate("MainWindow", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
