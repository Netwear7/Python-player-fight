"""
Data access table duels in db players_fight
"""
import pymysql
from DataAccess.db_connect import db_connect


class DuelsDataAccess:
    """
    Class with static function persist duels in db.
    Static methods:
        - create_new_duel
        - read_fight_count_of_two_players
        - read_count_of_win
    """

    # ________________________________________________________________________________________
    # CREATE
    @staticmethod
    def create_new_duel(winner, looser, turn):
        """
        Create new duel in database.
        Args:
            winner: Player Object.
            looser: Player Object.
            turn: Number of turn

        Returns: Nothing.
        """
        connection = db_connect()
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO duels(winner, looser, date_duel, tours) VALUES (%s,%s, NOW(),%s)"
            try:
                cursor.execute(sql, (winner.pseudo, looser.pseudo, turn))
            except pymysql.Error as element:
                print("Error %d: %s" % (element.args[1], element.args[0]))
            finally:
                connection.commit()
                cursor.close()

    # ________________________________________________________________________________________
    # READ
    @staticmethod
    def read_fight_count_of_two_players(winner: object, looser: object):
        """
        Get count duels of two player
        Args:
            winner: Player Object.
            looser: Player Object.
        Returns: Nothing.
        """
        connection = db_connect()
        with connection.cursor() as cursor:
            sql = """SELECT count(*) as total_match FROM duels
                WHERE winner = %s and looser = %s or winner = %s and looser = %s;"""
            try:
                cursor.execute(sql, (winner.pseudo, looser.pseudo, looser.pseudo, winner.pseudo))
                result = cursor.fetchone()
            except pymysql.Error as element:
                print("Error %d: %s" % (element.args[1], element.args[0]))
            finally:
                cursor.close()
            return result

    @staticmethod
    def read_count_of_win(winner: object, looser: object):
        """
        Get count winning duels of winner
        Args:
            winner: Player Object.
            looser: Looser Object.

        Returns:

        """
        connection = db_connect()
        with connection.cursor() as cursor:
            sql = "SELECT count(*) as nbr_win FROM duels WHERE winner = %s and looser = %s;"
            try:
                cursor.execute(sql, (winner.pseudo, looser.pseudo))
                result = cursor.fetchone()
            except pymysql.Error as element:
                print("Error %d: %s" % (element.args[1], element.args[0]))
            finally:
                cursor.close()
            return result

# ________________________________________________________________________________________
# Memo formation

# Table bdd :
# Joueur, pseudo - partie total - partie gagnée
# Duels, vainqueur - perdant - date - nombre tours
