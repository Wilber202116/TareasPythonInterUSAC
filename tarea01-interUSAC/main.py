from person import Person
from student import Student
from professor import Professor
from secretary import Secretary

estudiante1 = Student("hombre", "carlos godiñez", 170, 65)
estudiante2 = Student("Mujer", "Julieta Ramirez", 154, 55)

profesor1 = Professor("hombre", "Hugo Lumberto", 165, 75)
profesor2 = Professor("hombre", "Lucion Calderon", 175, 68)

secretary1 = Secretary("mujer", "carla quiñonez", 185, 72)
secreatry2 = Secretary("mujer", "Elizabeth Schawarz", 168, 62)

print(estudiante1)
print(estudiante2)
estudiante1.asuntosTraseros()
estudiante2.Starving()

print(profesor1)
print(profesor2)
profesor1.Answer()
profesor2.WakeyWakey()

print(secretary1)
print(secreatry2)
secretary1.Rol()
secreatry2.Setupdate()