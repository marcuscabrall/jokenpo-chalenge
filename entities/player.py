class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def get_name(self):
        return self.name

    def make_choice(self, choice):
        self.choice = choice