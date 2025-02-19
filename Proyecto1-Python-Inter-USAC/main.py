from person import Person
from photo import Photo
from place import Place
from rol import Rol

photo1 = Photo("c:/user3424/images/viajeachocomil.jpg", 2.00)
photo2 = Photo("c:/user3126/images/perfil2.png", 356)
photo3 = Photo("c:/discolocal/imagesdebatman.png", 4.00)
photo1.setunit("MB")
photo2.setfiletype("PNG")
photo3.setfiletype("PNG")
photo3.setunit("MB")


person1 = Person("wilber", "Mendez", photo1.getFileLocation())
person2 = Person("carlos", "rodriquez", photo2.getFileLocation())
person1.setRol(Rol.VERIFICADA.name)
person2.setTipoFoto(photo2.getFileType())

place1 = Place("Portales", "ZONA 17", "2535-1264")
place2 = Place("USAC", "ZONA 12", "5512-8864")
place3 = Place("LA LUUUUUUNA", "LUGAR DEL ESPACIO EXPLORADO", "+7 y +1 1957-1969")
place4 = Place("GHIBLI PARK", "Japan, 480-1342 Aichi, Nagakute, Ibaragabasama", "+81 50 3626 2455")
person1.addFavoritePlace(place1)
person1.addFavoritePlace(place4)
person2.addFavoritePlace(place2)
person2.addFavoritePlace(place3)

print(person1)
print(person2)