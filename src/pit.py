class Pit():
    def __init__(self,widht,height,depth,shape):
        self.__width = widht
        self.__height = height
        self.__depth = depth
        self.__shape = shape
    def getMatrixPerLevel(self): #gera uma matriz que marca as posições preenchidas por altura
        shapeInt = [0 if self.__shape[i] == '.' else 1 for i in range(len(self.__shape))]
        lists = [shapeInt[x:x+self.__width] for x in range(0, len(shapeInt), self.__width)]
        matrix = []
        for j in range(self.__height):
            matrix.append([lists[i] for i in range(j,len(lists),self.__height)])
        return matrix