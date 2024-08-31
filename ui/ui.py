import pygame
from entities.game import Game
from ui.styles import COLORS


class UI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Numen - Jokenpô")
        self.font = pygame.font.Font(None, 36)
        self.input_box = pygame.Rect(200, 150, 200, 50)
        self.color_inactive = COLORS["inactive"]
        self.color_active = COLORS["active"]
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.player_name = ''
        self.game = None
        self.game_started = False
        self.mode_selection = False
        self.showing_stats = False
        self.running = True
        self.result_message = ''
        self.buttons = {
            "pedra": pygame.Rect(50, 250, 150, 50),
            "papel": pygame.Rect(225, 250, 150, 50),
            "tesoura": pygame.Rect(400, 250, 150, 50),
            "best_of_3": pygame.Rect(50, 200, 150, 50),
            "best_of_5": pygame.Rect(225, 200, 150, 50),
            "best_of_7": pygame.Rect(400, 200, 150, 50),
            "continue": pygame.Rect(200, 300, 200, 50)
        }

    def draw_text(self, text, position, color=None, center=False):
        color = color if color else COLORS["text"]
        rendered_text = self.font.render(text, True, color)
        text_rect = rendered_text.get_rect()
        if center:
            text_rect.center = position
        else:
            text_rect.topleft = position
        self.screen.blit(rendered_text, text_rect.topleft)

    def draw_buttons(self):
        for button_key in ["pedra", "papel", "tesoura"]:
            pygame.draw.rect(self.screen, COLORS[f"button_{button_key}"], self.buttons[button_key], border_radius=10)
            pygame.draw.rect(self.screen, COLORS["border"], self.buttons[button_key], 3, border_radius=10)
            self.draw_text(button_key.capitalize(), self.buttons[button_key].center, center=True)

    def draw_game_mode(self):
        for button_key in ["best_of_3", "best_of_5", "best_of_7"]:
            pygame.draw.rect(self.screen, COLORS["button_mode"], self.buttons[button_key], border_radius=10)
            pygame.draw.rect(self.screen, COLORS["border"], self.buttons[button_key], 3, border_radius=10)
            mode_text = "Melhor de " + button_key.split("_")[-1]
            self.draw_text(mode_text, self.buttons[button_key].center, center=True)

    def show_winner(self, winner):
        self.screen.fill(COLORS["background"])
        self.draw_text(f"Resultado: {winner}", (300, 120), COLORS["border"], center=True)
        self.draw_text(f"O computador escolheu: {self.game.computer.choice}", (300, 160), center=True)
        pygame.display.flip()
        pygame.time.wait(2000)

    def show_statistics(self):
        self.showing_stats = True
        self.screen.fill(COLORS["background"])
        self.draw_text(">>> Estatísticas do Jogo <<<", (300, 80), COLORS["border"], center=True)
        self.draw_text(self.result_message, (300, 120), center=True)
        self.draw_text(f"Vitórias: {self.game.player_wins}", (300, 160), center=True)
        self.draw_text(f"Derrotas: {self.game.computer_wins}", (300, 200), center=True)
        self.draw_text(f"Empates: {self.game.draws}", (300, 240), center=True)
        pygame.draw.rect(self.screen, COLORS["button_mode"], self.buttons["continue"], border_radius=10)
        pygame.draw.rect(self.screen, COLORS["border"], self.buttons["continue"], 3, border_radius=10)
        self.draw_text("Continuar", self.buttons["continue"].center, center=True)
        pygame.display.flip()

    def reset_game(self):
        self.game.reset_game()
        self.mode_selection = True
        self.showing_stats = False
        self.game_started = False
        self.result_message = ''

    def run(self):
        while self.running:
            self.screen.fill(COLORS["background"])
            if not self.game_started:
                if self.showing_stats:
                    self.show_statistics()
                elif not self.mode_selection:
                    self.draw_text("Digite seu nome:", (300, 100), center=True)
                    txt_surface = self.font.render(self.text, True, self.color)
                    width = max(200, txt_surface.get_width() + 10)
                    self.input_box.w = width
                    self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 10))
                    pygame.draw.rect(self.screen, self.color, self.input_box, 2)
                else:
                    self.draw_text("Escolha o modo de jogo:", (300, 150), center=True)
                    self.draw_game_mode()
            else:
                self.draw_text(f"Jogador: {self.game.player.get_name()}", (20, 20))
                self.draw_text(f"Vitórias: {self.game.player_wins} | Derrotas: {self.game.computer_wins} | Empates: {self.game.draws}", (20, 60))
                self.draw_text("Escolha: Pedra, Papel ou Tesoura", (300, 120), center=True)
                self.draw_buttons()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if not self.game_started:
                    if self.showing_stats:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.buttons["continue"].collidepoint(event.pos):
                                self.reset_game()
                    elif not self.mode_selection:
                        if event.type == pygame.MOUSEBUTTONDOWN and self.input_box.collidepoint(event.pos):
                            self.active = not self.active
                            self.color = self.color_active if self.active else self.color_inactive
                        if event.type == pygame.KEYDOWN and self.active:
                            if event.key == pygame.K_RETURN:
                                self.player_name = self.text
                                self.mode_selection = True
                            elif event.key == pygame.K_BACKSPACE:
                                self.text = self.text[:-1]
                            else:
                                self.text += event.unicode
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.buttons["best_of_3"].collidepoint(event.pos):
                                self.start_game(2)
                            elif self.buttons["best_of_5"].collidepoint(event.pos):
                                self.start_game(3)
                            elif self.buttons["best_of_7"].collidepoint(event.pos):
                                self.start_game(4)
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if self.buttons["pedra"].collidepoint(mouse_pos):
                            self.make_choice("pedra")
                        elif self.buttons["papel"].collidepoint(mouse_pos):
                            self.make_choice("papel")
                        elif self.buttons["tesoura"].collidepoint(mouse_pos):
                            self.make_choice("tesoura")

    def start_game(self, rounds_to_win):
        if self.player_name == '':
            self.player_name = self.text
        self.game = Game(self.player_name, rounds_to_win)
        self.game_started = True

    def make_choice(self, choice):
        self.game.player.make_choice(choice)
        self.game.computer.make_choice()
        winner = self.game.show_winner()
        self.show_winner(winner)
        if self.game.is_game_over():
            self.result_message = "Você ganhou!" if self.game.player_wins == self.game.rounds_to_win else "Você perdeu!"
            self.showing_stats = True
            self.game_started = False