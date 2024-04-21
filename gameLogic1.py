class Game():
    def __init__(self, matrix, imagesPathDict):
        self.matrix = matrix
        self.imagesPathDict = imagesPathDict

    def makeAmove(self, matrix, curButnIndex):
        gameFieldSize = len(matrix)
        if gameFieldSize == 3:
            i, j = curButnIndex // 3, curButnIndex % 3
        elif gameFieldSize == 4:
            i, j = curButnIndex // 4, curButnIndex % 4

        if matrix[i][j] == 1:
            img = self.imagesPathDict[1]
            self.usedFigures.append('images/blueCircle.png')
        elif matrix[i][j] == 2:
            img = self.imagesPathDict[2]
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
