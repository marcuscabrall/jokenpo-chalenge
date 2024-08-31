import random
from entities.player import Player


class Computer(Player):
    def make_choice(self):
        self.choice = random.choice(['pedra', 'papel', 'tesoura'])