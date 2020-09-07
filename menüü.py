from laul import Laul
from album import Album

laul_1 = Laul("Für Oksana", "Nuble")
print(laul_1.laulja, laul_1.pealkiri)
laul_2 = Laul("12", "Nuble")
print(laul_2.laulja, laul_2.pealkiri)

album = Album("Uus album", 2019, "Numblu")

album.laulud.append(laul_1)
album.laulud.append(laul_2)

for laul in album.laulud:
    print(laul.laulja, laul.pealkiri)