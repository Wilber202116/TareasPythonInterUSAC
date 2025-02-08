from person import Person

class Student(Person):
    def __init__(self, paramgen: str, paramname: str, paramheight:int, paramweight:int, paramrol: str = "estudiante" ):
        super().__init__( paramgen, paramname, paramheight, paramweight, paramrol)

    def asuntosTraseros(self):
        print(f"{self.name} procede a hacer un asado en la parte de atras")

    def Starving(self):
        print(f"{self.name} procede a desayunar en la clase (solo tiene un tortrix y agua)")