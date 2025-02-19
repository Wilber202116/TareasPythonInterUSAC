
class Place:
    def __init__(self, namePlace: str, address: str, phonePlace: str):
        self.__nameplace = namePlace
        self.__address = address
        self.__phonePlace = phonePlace

    def getNamePlace(self):
        nombrelugar = self.__nameplace
        return nombrelugar
    
    def getAddress(self):
        return self.__address

    def getphone(self):
        return self.__phonePlace

    def __str__(self):
        return f"- {self.getNamePlace()} - {self.getAddress()}"