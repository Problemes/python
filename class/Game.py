class Game(object):
    score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help_info():
        print("let XIAOJS enter the gate...")

    @classmethod
    def show_current_score(cls):
        print("%s is current score..." % cls.score)

    def show_current_name(self):
        print("current player name is %s" % self.player_name)


Game.show_help_info()

Game.show_current_score()

game = Game("LetMe")
game.show_current_name()
Game.score += 1
Game.show_current_score()