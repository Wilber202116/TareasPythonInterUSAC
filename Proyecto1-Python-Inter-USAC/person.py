from rol import Rol
from photo import Photo
from place import Place



class Person:
    def __init__(self, name: str, lastname: str, photo):
        self.__name = name
        self.__lastname = lastname
        self.__rol = Rol.SIN_VERIFICAR.name
        self.__places = []
        self.__photo = photo
        self.tipofoto = "JPG"
    
    def getname(self):
        name = self.__name
        return name

    def getlastname(self):
        return self.__lastname

    def getphoto(self):
        return self.__photo

    def setPhoto(self, photo: str):
        self.__photo = photo

    def getRol(self):
        return self.__rol
    
    def getPlace(self):
        return self.__places
    
    def listplaces(self):
        return "\n \t" .join(map(str, self.getPlace()))

    def setRol(self, rol: str):
        self.__rol = rol
    
    def addFavoritePlace(self, place):
        self.__places.append(place)
        return self.__places

    def setTipoFoto(self, tipo):
        self.tipofoto = tipo
        return self.tipofoto


    def __str__(self):
        return f'''
        El usuario con nombre: {self.getname()} {self.getlastname()},
        con foto tipo .{self.tipofoto} ubicada en {self.getphoto()},
        y su cuenta esta {self.getRol()}, tiene los lugares: 
        {self.listplaces()}'''