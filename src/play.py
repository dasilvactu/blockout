class Play():
    def __init__(self,piece,position,score):
        self.__piece = piece
        self.__position = position
        self.__score = score
    def getPiece(self):
        return self.__piece
    def getPosition(self):
        return self.__position
    def getScore(self):
        return self.__score
    def setScore(self,score):
        self.__score = score