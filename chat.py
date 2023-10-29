import random

class Robor:
    def __init__(self):
        self.saldações = ['ola', 'boa noite']
        self.ofenças = ['legal', 'kkk']
        self.educação = ['oh prazer', 'fico feliz', 'que bom']

    def menssagens(self, palavras):
        pala = random.choice(palavras)
        return pala

class User:
    def __init__(self):
        self.saldacao = ['bom dia', 'ola', 'tudo bem']
        self.ofenca = ['burra', 'idioata', 'trouxa']
        self.educacao = ['me chamo sans', 'q bot incrivel']


usuario = User()
bot = Robor()

while True:
    Pessoa = input(str('digite algo: '))
    if Pessoa in usuario.saldacao:
        print(bot.menssagens(bot.saldações))
    elif Pessoa in usuario.educacao:
        print(bot.menssagens(bot.educação))
    elif Pessoa in usuario.ofenca:
        print(bot.menssagens(bot.ofenças))
    elif Pessoa == '9999':
        break
    else:
        print('digite de novo')
