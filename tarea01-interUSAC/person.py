class Person():
    def __init__(self, paramgen: str, paramname: str, paramheight:int, paramweight:int, paramrol: str ):
        self.gen = paramgen
        self.name = paramname
        self.height = paramheight
        self.weight = paramweight
        self.rol = paramrol
    
    def WakeyWakey(self):
        print(f"{self.name} se levanta por la mañana")
    
    def Rol(self):
        print(f"{self.name} procede a hacer el rol que le toca")

    def __str__(self):
        return f'''
        La persona se llama {self.name}, 
        es un/a {self.gen},
        su altura es {self.height}, y
        pesa {self.weight} kg.
        Su rol es {self.rol}
        '''