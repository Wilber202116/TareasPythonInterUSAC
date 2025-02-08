from person import Person

class Professor(Person):
    def __init__(self, paramgen: str, paramname: str, paramheight:int, paramweight:int, paramrol: str = "Profesor"):
        super().__init__( paramgen, paramname, paramheight, paramweight, paramrol)

    def Teach(self):
        print(f"el profesor {self.name} enseña un tema con un powerpoint (la compu no funciona)")

    def Answer(self):
        print(f"el profesor {self.name} responde las dudas de los estudiantes")