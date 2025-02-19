

class Photo:
    def __init__(self, fileLocation: str, size: float):
        self.__fileLocation = fileLocation
        self.__fileType = "JPG"
        self.__size =  size
        self.__unit = "KB"
    
    def getFileLocation(self):
        return self.__fileLocation
    
    def getFileType(self):
        return self.__fileType

    def getsize(self):
        return self.__size
    
    def getunit(self):
        return self.__unit
    
    def setfiletype(self, file: str):
        self.__fileType = file
        return self.__fileType

    def setunit(self, newunit):
        self.__unit = newunit
        return self.__unit

    def __str__(self):
        return f'''Prueba de variables: 
        {self.getFileLocation()}, 
        {self.getFileType()}, y
        {self.getsize()} {self.getunit()}'''