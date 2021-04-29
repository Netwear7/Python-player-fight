"""
Connect to MariaDb or connect to database
"""
import pymysql


def db_connect(database_created=True):
    """
    Get database pymysql connect, without database_name if database_created = false.
    Args:
        database_created: Boolean
    Returns: Nothing.
    """
    username = 'Your_database_username'
    password = 'Your_database_password'

    if database_created:
        access_db = pymysql.connect(
            host='localhost',
            user=username,
            password=password,
            database='players_fight',
            cursorclass=pymysql.cursors.DictCursor)
    else:
        access_db = pymysql.connect(
            host='localhost',
            user=username,
            password=password,
            cursorclass=pymysql.cursors.DictCursor)
    return access_db
