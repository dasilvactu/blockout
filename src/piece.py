from collections import deque
class Piece():
    def __init__(self, block_index, width, height,depth, shape):
        self.__block_index = block_index
        self.__width = width
        self.__height = height
        self.__depth = depth
        self.__shape = shape
        self.__matrix = None
    def getBlockIndex(self):
        return self.__block_index
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getDepth(self):
        return self.__depth
    def getShape(self):
        return self.__shape
    def getMatrix(self):
        return self.__matrix
    def setMatrix(self,pit):
        sizeShape = len(self.__shape)
        diffPit = [0 for i in range(len(pit.getShape()) - sizeShape)] #cria a representação equivalente da peça no formato do pit
        shapeInt = [0 if self.__shape[i] == '.' else 1 for i in range(sizeShape)] + diffPit
        lists = [shapeInt[x:x+pit.getWidht()] for x in range(0, len(shapeInt),pit.getWidht())]
        matrix = []
        for j in range(pit.getHeight()):
            matrix.append([lists[i] for i in range(j,len(lists),pit.getHeight())])
        position = self.__height + pit.getHeight()
        self.__matrix =movePiece(matrix, -position ) #posiciona a peça no topo do pit, respeitando a altura da peça
    def movePiece(self, matrix, height):
        items = deque(matrix)
        items.rotate(height) # negativo desce o elemento em hight niveis, positivo sobe o elemento
        return list(items)