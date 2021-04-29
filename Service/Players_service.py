from DataAccess.players_data_access import PlayersDataAccess


class Players_Service:
    def __init__(self):
        self.data_access = PlayersDataAccess()

    def update_player_stat(self, player: object):
        """
        Service update or create(If player not exist in database) stats of player.
        Args:
            player: Player Object.
        Returns: Nothing.
        """
        # If player exist in database
        player_exist_db = self.data_access.read_player_if_exist(player.pseudo)

        # if player exist : update.
        if player_exist_db:
            # add + 1 to total_game
            total_game = player_exist_db['total_game'] + 1
            # if player has no life
            if player.life <= 0:
                win = player_exist_db['win']
            # Else player win, add +1 to win.
            else:
                win = player_exist_db['win'] + 1
            self.data_access.update_stats_player(player_exist_db['pseudo'], win, total_game)

        # if player doesn't exist : create.
        else:
            # if player has no life, win = 0.
            if player.life <= 0:
                win = 0
            # Else player win, add +1 to win.
            else:
                win = 1
            self.data_access.create_new_player(player.pseudo, win, 1)
