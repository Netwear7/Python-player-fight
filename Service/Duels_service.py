from DataAccess.duels_data_access import DuelsDataAccess


class Duels_Service:
    def __init__(self):
        self.data_access = DuelsDataAccess()

    @staticmethod
    def create_duels_stat(winner: object, looser: object, turn):
        """
        Service create stats of player vs player.
        Args:
            winner: Player Object.
            looser: Player Object
            turn: Number of turn in the fight
        Returns: Nothing.
        """
        DuelsDataAccess.create_new_duel(winner, looser, turn)

    @staticmethod
    def read_fight_count_of_two_players(winner, looser):
        return DuelsDataAccess.read_fight_count_of_two_players(winner, looser)

    @staticmethod
    def read_count_of_win(winner, looser):
        return DuelsDataAccess.read_count_of_win(winner, looser)

    @classmethod
    def stat_player(cls, player, opponent):
        nbr_fight = cls.read_fight_count_of_two_players(player, opponent)
        win_count = cls.read_count_of_win(player, opponent)
        percentage = round(win_count['nbr_win'] / nbr_fight['total_match'] * 100, 2)
        print(f"\n{player.pseudo} a gagné {win_count['nbr_win']} Victoire(s) contre {opponent.pseudo}")
        print(f"Ratio de victoire/défaite : {percentage}%")
