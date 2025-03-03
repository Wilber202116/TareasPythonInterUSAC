class Person:
    def __init__(self, identificacion: int, nombre:str, apellido:str, edad: int, fotografia, correo_electronico:str, contraseña:str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.fotografia = fotografia
        self.correo = correo_electronico
        self.contraseña = contraseña
    
    @staticmethod
    def iniciar_sesion(correo, contraseña, personas):
        print(correo)
        print(contraseña)
        for persona in personas:
            if persona.correo == correo and persona.contraseña == contraseña:
                return "Inicio de sesion exitoso", persona
        return "correo y/o contraseña incorrectos", None
    '''
    @staticmethod
    def registro_persona(identificacion: int, nombre:str, apellido:str, edad: int, fotografia, correo_electronico:str, contraseña:str):
        newPerson = Person(identificacion, nombre,apellido,edad,fotografia,correo_electronico,contraseña)
        database.personas.append(newPerson)
    '''