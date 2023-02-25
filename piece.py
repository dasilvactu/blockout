class Piece():
    def __init__(self, block_index, width, height,depth, shape):
        self.__block_index = block_index
        self.__width = width
        self.__height = height
        self.__depth = depth
        self.__shape = shape
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