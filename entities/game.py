from entities.computer import Computer
from entities.player import Player


class Game:
    def __init__(self, player_name, rounds_to_win):
        self.player = Player(player_name)
        self.computer = Computer('Computador')
        self.rounds_to_win = rounds_to_win
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0

    def show_winner(self):
        if self.player.choice == self.computer.choice:
            self.draws += 1
            return 'Empate!'
        elif (self.player.choice == 'papel' and self.computer.choice == 'pedra') or \
             (self.player.choice == 'tesoura' and self.computer.choice == 'papel') or \
             (self.player.choice == 'pedra' and self.computer.choice == 'tesoura'):
            self.player_wins += 1
            return f'{self.player.get_name()} ganhou!!!'
        else:
            self.computer_wins += 1
            return f'{self.computer.get_name()} ganhou!!!'

    def is_game_over(self):
        return self.player_wins >= self.rounds_to_win or self.computer_wins >= self.rounds_to_win

    def reset_game(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0
        self.player.choice = None
        self.computer.choice = None