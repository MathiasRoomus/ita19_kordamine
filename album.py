class Album:

    def __init__(self, nimetus, aasta, laulja):
        self.nimetus = nimetus
        self.aasta = aasta
        self.laulja = laulja
        self.laulud = []

    def naita_nimi(self):
        print(self.nimetus)

    def naita_laulja_ja_nimi(self):
        print(self.laulja + ": " + self.nimetus + " (" + self.aasta + ")")

    def naita_laulud(self):
        for laul in self.laulud:
            laul.naita_pealkiri()

    def lisa_laul(self, laul):
        self.laulud.append(laul)
