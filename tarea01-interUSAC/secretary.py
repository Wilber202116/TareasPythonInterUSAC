from person import Person

class Secretary(Person):
    
    def __init__(self, paramgen: str, paramname: str, paramheight:int, paramweight:int, paramrol: str = "Secretaria"):
        super().__init__( paramgen, paramname, paramheight, paramweight, paramrol)

    def Setupdate(self):
        print(f"la secretaria {self.name} procede a agendar la cita con tus datos personales")

    def ClienteSeQuejaPorAlgoQueNoVaConMiProfesion(self):
        print(f"La señorita {self.name} le dijo a los clientes: Lo siento, solo soy la secretaria (no soy un super humano)")