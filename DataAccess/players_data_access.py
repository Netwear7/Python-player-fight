"""
Data access table players in db players_fight
"""
import pymysql
from DataAccess.db_connect import db_connect


class PlayersDataAccess:
    """
    Class with static function persist players in db.
    Static methods:
        - create_new_player
        - read_player_if_exist
        - update_stats_player
    """
    # ________________________________________________________________________________________
    # CREATE
    @staticmethod
    def create_new_player(pseudo, win, total_game):
        """
        Create new player
        Args:
            pseudo: name of Player
            win: number of victory (0-1)
            total_game: 1 (First game)

        Returns: Nothing.
        """
        connection = db_connect()
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO players (pseudo, win, total_game) VALUES (%s, %s, %s)"
            try:
                cursor.execute(sql, (pseudo, win, total_game))
            except pymysql.Error as element:
                print("Error %d: %s" % (element.args[1], element.args[0]))
            finally:
                connection.commit()
                cursor.close()

    # ________________________________________________________________________________________
    # READ
    @staticmethod
    def read_player_if_exist(pseudo):
        """
        Get player if exist
        Args:
            pseudo: Name of player in database
        Returns: Name of player
        """
        connection = db_connect()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM players WHERE pseudo = %s;"
            try:
                cursor.execute(sql, pseudo)
                result = cursor.fetchone()
            except pymysql.Error as element:
                print("Error %d: %s" % (element.args[1], element.args[0]))
            finally:
                cursor.close()
            return False if result is None else result

    # ________________________________________________________________________________________
    # UPDATE
    @staticmethod
    def update_stats_player(pseudo, win, total_game):
        """
        Update stat player
        Args:
            pseudo: name of Player in database
            win: number of victory (0-1)
            total_game: 1 (First game)
        Returns: Nothing.
        """
        connection = db_connect()
        with connection.cursor() as cursor:
            sql = "UPDATE players SET win = %s, total_game = %s WHERE pseudo = %s;"
            try:
                cursor.execute(sql, (win, total_game, pseudo))
            except pymysql.Error as element:
                print("Error %d: %s" % (element.args[1], element.args[0]))
            finally:
                connection.commit()
                cursor.close()

# ________________________________________________________________________________________
# Memo formation

# Table bdd :
# Joueur, pseudo - partie total - partie gagnée
# Duels, vainqueur - perdant - date - nombre tours
