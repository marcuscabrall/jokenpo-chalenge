import pytest
from entities.game import Game


@pytest.fixture
def game():
    return Game("Marcus", 2)


def test_game_init(game): # Testa a inicialização do jogo
    assert game.player.get_name() == "Marcus"
    assert game.rounds_to_win == 2
    assert game.player_wins == 0
    assert game.computer_wins == 0
    assert game.draws == 0


def test_player_choice(game): # Testa a escolha do jogador
    game.player.make_choice("pedra")
    assert game.player.choice == "pedra"


def test_computer_choice(game): # Testa a escolha do PC
    game.computer.make_choice()
    assert game.computer.choice in ["pedra", "papel", "tesoura"]


def test_game_logic(game): # Testa quando o jogador ganha
    game.player.make_choice("pedra")
    game.computer.choice = "tesoura"
    winner = game.show_winner()
    assert winner == "Marcus ganhou!!!"
    assert game.player_wins == 1
    assert game.computer_wins == 0
    assert game.draws == 0


    game.player.make_choice("pedra") # Testa quando o computador ganha
    game.computer.choice = "papel"
    winner = game.show_winner()
    assert winner == "Computador ganhou!!!"
    assert game.player_wins == 1
    assert game.computer_wins == 1
    assert game.draws == 0


def test_tie_scenario(game): # Empate
    game.player.make_choice("papel")
    game.computer.choice = "papel"
    winner = game.show_winner()
    assert winner == "Empate!"
    assert game.draws == 1


def test_game_over(game): # 2 vitórias do jogador
    game.player_wins = 1
    game.player.make_choice("pedra")
    game.computer.choice = "tesoura"
    game.show_winner()
    assert game.is_game_over() is True  # Se o jogo termina depois da segunda vitória do jogador

    game.reset_game() # 2 vitórias do computador
    game.computer_wins = 1
    game.player.make_choice("tesoura")
    game.computer.choice = "pedra"
    game.show_winner()
    assert game.is_game_over() is True  # Se o jogo termina depois de 2 vitórias do computador


def test_game_reset(game): # Testa se o jogo reseta
    game.player_wins = 1
    game.computer_wins = 1
    game.reset_game()
    assert game.player_wins == 0
    assert game.computer_wins == 0
    assert game.draws == 0
    assert game.player.choice is None
    assert game.computer.choice is None


def test_tie(game): # Testa empates
    game.player.make_choice("tesoura")
    game.computer.choice = "tesoura"
    winner = game.show_winner()
    assert winner == "Empate!"
    assert game.draws == 1

    game.player.make_choice("pedra") # Testa quando o jogador ganha perde em seguida
    game.computer.choice = "tesoura"
    winner = game.show_winner()
    assert winner == "Marcus ganhou!!!"
    game.player.make_choice("tesoura")
    game.computer.choice = "pedra"
    winner = game.show_winner()
    assert winner == "Computador ganhou!!!"