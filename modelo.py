class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._avaliacao = 0

    @property
    def likes(self):
        return self._avaliacao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def like(self):
        self._avaliacao += 1

    def __str__(self):
        return "{} - {}: {}".format(self._nome, self.ano, self._avaliacao)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "{} - {} - {} minutos: {}".format(self._nome, self.ano, self.duracao, self._avaliacao)

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return "{} - {} - {} temporadas: {}".format(self._nome, self.ano, self.temporada, self._avaliacao)


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores: guerra infinita", 2018, 160)
flash = Serie("flash", 2014, 7)
ldj = Filme("liga da justica: snyder cut", 2021, 300)
supergirl = Serie('supergirl', 2015, 6)

vingadores.like()
vingadores.like()
flash.like()
supergirl.like()
supergirl.like()
supergirl.like()
ldj.like()
ldj.like()
ldj.like()
ldj.like()
ldj.like()

lista = [vingadores, ldj, supergirl, flash]
playlist = Playlist("playlist", lista)

for programa in playlist:
    print(programa)
