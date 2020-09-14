from laul import Laul
from album import Album
from laulja import Laulja
import csv

tabel = []
with open("albumid.txt", encoding="utf-8") as file:
    file_reader = csv.reader(file, delimiter="\t")
    for row in file_reader:
        tabel.append(row)

albumid = []
lauljad = []
laulud = []

first_albumid = []
first_lauljad = []

for row in tabel:
    laul = Laul(row[3], row[0])
    laulud.append(laul)

    if row[0] not in first_lauljad:
        laulja = Laulja(row[0])
        lauljad.append(laulja)
        first_lauljad.append(laulja.nimi)

    if row[1] not in first_albumid:
        album = Album(row[1], row[2], row[0])
        laulja.lisa_album(album)
        albumid.append(album)
        first_albumid.append(row[1])

    album.lisa_laul(laul)

kas_jatkata = True
while kas_jatkata:
    print("Tee valik:")
    print("1: väljasta albumid ja laulud")
    print("2: otsing albumi pealkirja või aasta järgi")
    print("3: otsing laulu järgi")
    print("4: otsing laulja järgi")

    valik = input("Valik [1, 2, 3, 4]: ")

    if valik == "1":
        print("Albumid: ")
        for album in albumid:
            album.naita_laulja_ja_nimi()
            album.naita_laulud()
            print("----------------")
    elif valik == "2":
        otsitav = input("Sisesta otsitav album või aasta: ")
        for album in albumid:
            if otsitav.lower() in album.nimetus.lower() or otsitav == album.aasta:
                album.naita_laulja_ja_nimi()
                album.naita_laulud()
    elif valik == "3":
        otsitav = input("Sisesta otsitav laul: ")
        for album in albumid:
            for laul in album.laulud:
                if otsitav.lower() in laul.pealkiri.lower():
                    album.naita_laulja_ja_nimi()
                    laul.naita_pealkiri()
    elif valik == "4":
        otsitav = input("Sisesta otsitav laulja: ")
        for laulja in lauljad:
            if otsitav.lower() in laulja.nimi.lower():
                for album in laulja.albumid:
                    album.naita_laulja_ja_nimi()
    else:
        print("Lõpp")
        kas_jatkata = False
    print("++++++++++++++++++++++++++++++++++++++++")




