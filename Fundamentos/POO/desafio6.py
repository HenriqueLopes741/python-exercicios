class Gamer:
    def __init__(self, nome, nick, fav):
        self.nome = nome
        self.nick = nick
        self.fav = fav  # agora sim

    def ficha(self):
        print('====== FICHA DO GAMER ======')
        print(f"Nome: {self.nome}")
        print(f"Nick: {self.nick}")
        print("Jogos favoritos:")
        
        for jogo in self.fav:
            print(f"- {jogo}")


# lista de jogos
jogos = ["FIFA", "God of War", "Valorant"]

# criando o objeto corretamente
p1 = Gamer("Henrique", "Cochinha", jogos)

# chamando o método
p1.ficha()