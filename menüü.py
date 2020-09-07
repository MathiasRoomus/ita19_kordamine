from laul import Laul
from album import Album
from laulja import Laulja

laul_1 = Laul("Für Oksana", "Nuble")
#print(laul_1.laulja, laul_1.pealkiri)
laul_2 = Laul("12", "Nuble")
#print(laul_2.laulja, laul_2.pealkiri)
laul_3= Laul("Crousandid", "Nuble")
#print(laul_1.laulja, laul_1.pealkiri)
laul_4 = Laul("Öölaps", "Nuble")
#print(laul_2.laulja, laul_2.pealkiri)

album_1 = Album("Uus album 1", 2019, "Numblu")

album_1.lisa_laul(laul_1)
album_1.lisa_laul(laul_2)

album_2 = Album("Uus album 2", 2019, "Numblu")

album_2.lisa_laul(laul_3)
album_2.lisa_laul(laul_4)

#print(album_2.pealkiri)
#for laul in album_2.laulud:
    #print(laul.laulja, laul.pealkiri)

laulja = Laulja("Nublu")
laulja.lisa_album(album_1)
laulja.lisa_album(album_2)

for album in laulja.albumid:
    print(album.pealkiri)
    for laul in album.laulud:
        print(laul.laulja, laul.pealkiri)