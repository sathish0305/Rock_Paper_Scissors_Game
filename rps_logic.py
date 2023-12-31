import random

class Game(Exception):
    def __init__(self):
        commands = {
            'rock':'Rock',
            'paper':'Paper',
            'scissors':'Scissors'
        }
        self.keys = []
        for command in commands:
            self.keys.append(command)
        self.userScore = 0
        self.botScore = 0

    def user(self):
        self.userScore+=1
        print('User Wins the round')
        print('-'*30)

    def bot(self):
        self.botScore+=1
        print('Bot Wins the round')
        print('-'*30)

    def play(self,data):
        self.data = data
        res = random.choice(self.keys)
        print('User Choice: ',self.data)
        print('Bot Choice: ',res)
        print('-'*20)
        if self.data.lower() == res:
            print('Both are same')
            print('-'*30)
        elif self.data == 'Rock' and res == 'paper':
            self.bot()
        elif self.data == 'Paper' and res == 'scissors':
            self.bot()
        elif self.data == 'Scissors' and res == 'rock':
            self.bot()
        else:
            self.user()

    def score(self):
        print('Game Summary')
        print('-'*30)
        print('User Score: ',self.userScore)
        print('Computer Score: ',self.botScore)
        print('-'*30)
        if self.userScore>self.botScore:
            print('User Wins the Game')
            print('-'*30)
        elif self.userScore<self.botScore:
            print('Bot wins the Game')
            print('-'*30)
        else:
            print('Tie Game!!!!')
            print('-'*30)
