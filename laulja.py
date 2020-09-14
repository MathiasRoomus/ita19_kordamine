class Laulja:

    def __init__(self, nimi):
        self.nimi = nimi
        self.albumid = []

    def naita_nimi(self):
        print(self.nimi)

    def naita_albumid(self):
        for album in self.albumid:
            album.naita_nimi()

    def lisa_album(self, album):
        self.albumid.append(album)
