"""
Programme fight since two players.
"""
from Model.Player import Player
from Service.Players_service import Players_Service
from Service.Duels_service import Duels_Service
from DataAccess.create_database import CreateDatabase

# Initialisation database if not exist:
CreateDatabase.generate_bdd()
# _____________________________________
# Instance two player:
player1 = Player(input("Nommez le joueur n°1: "))
player2 = Player(input("Nommez le joueur n°2: "))
# _____________________________________

# Print life of 2 players:
print(f'{player1.pseudo}, vie: {player1.life} | {player2.pseudo}, vie: {player2.life}')
# _____________________________________

# Multiple assignment :
# arr[0]: winner(Player object)  |
# arr[1]: looser(Player object)  |
# arr[2]: lap_counter: number of attack turn.
winner, looser, turn = player1.fight_start(player2)
# _____________________________________

# Update or create player in Database:
players_serv = Players_Service()
players_serv.update_player_stat(winner)
players_serv.update_player_stat(looser)
# _____________________________________

# Create duels in Database:
duels_serv = Duels_Service()
duels_serv.create_duels_stat(winner, looser, turn)
# _____________________________________

# Get stat player:
duels_serv.stat_player(winner, looser)
duels_serv.stat_player(looser, winner)
# _____________________________________

# _______________________________________________
# Memo  :                                       |
#                                               |
# Récupérer les attributs de l'objet:           |
#   print(vars(player1))                        |
#                                               |
# Récupérer les méthodes de l'objet:            |
#   print(dir(player1))                         |
#                                               |
# Lire la documentation de la classe Player :   |
#   player_object = Player("Helper")            |
#   print(player_object.__doc__)                |
# ______________________________________________|
