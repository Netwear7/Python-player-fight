"""
Module create database
"""
import pymysql
from DataAccess.db_connect import db_connect


class CreateDatabase:
    """
    Class with static function create database
    Static methods:
        - create_db
        - create_table_players
        - create_table_duels
    """

    @staticmethod
    def create_db():
        """
        Create Database if not exist.
        Returns: Nothing
        """
        connection = db_connect(False)
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE DATABASE IF NOT EXISTS players_fight"
            try:
                cursor.execute(sql)
            except pymysql.Error as element:
                print("Error %d : %s" % (element.args[1], element.args[0]))
            finally:
                connection.commit()
                cursor.close()

    @staticmethod
    def create_table_players():
        """
        Create table players if not exist.
        Returns: Nothing
        """
        connection = db_connect()
        with connection.cursor() as cursor:
            # Create a new record
            sql = """CREATE TABLE IF NOT EXISTS players
            (pseudo varchar(255) NOT NULL, win int(11) DEFAULT NULL,
            total_game int(11) DEFAULT NULL)"""
            try:
                cursor.execute(sql)
            except pymysql.Error as element:
                print(f"Error {element.args[0]} : {element.args[1]}")
            finally:
                connection.commit()
                cursor.close()

    @staticmethod
    def create_table_duels():
        """
        Create table duels if not exist.
        Returns: Nothing.
        """
        connection = db_connect()
        with connection.cursor() as cursor:
            # Create a new record
            sql = """CREATE TABLE IF NOT EXISTS duels(winner varchar(255)
            DEFAULT NULL,looser varchar(255) DEFAULT NULL,
            date_duel date DEFAULT NULL, tours int(11) DEFAULT NULL)"""
            try:
                cursor.execute(sql)
            except pymysql.Error as element:
                print(f"Error {element.args[0]} : {element.args[1]}")
            finally:
                connection.commit()
                cursor.close()

    @classmethod
    def generate_bdd(cls):
        """
        Generate database with tables.
        Returns: Nothing.
        """
        cls.create_db()
        cls.create_table_players()
        cls.create_table_duels()
