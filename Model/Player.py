from random import randint


class Player:
    """
    ---Class Player : Create new player with different methods and attributes.
    Attributes:
        - life (Type: integer and positive), the life of the player
        - pseudo (Type: str, name of player
    Methods:
        - attack            : -- Attack Opponent
        - attack_attempt    : -- attempt to attack Opponent, 50% chance to make damage
        - fight_start       : -- let's fight, first player without life die. turn by turn game.
        - fight_end         : -- Print in Terminal for a fight end.
        - attack_success    : -- Print in Terminal for a successful attack.
        - attack_failed     : -- Print in Terminal for a loosing attack.
    Static methods:
        - random_attack_damage   : -- Returns random int between 1 and 100 (100 inside).
        - is_last_hitting   : -- Returns true if is the last hitting.
    """

    def __init__(self, pseudo: str):
        """
        Args:
            pseudo (str): 
        """
        self.life = 200
        self.pseudo = pseudo

    def fight_start(self, opponent: object):
        """
        ---Start fight with opponent, attack turn by turn.
        Arguments:
            - opponent, It's another player Object, it's the player we're try to attack.
        Local Variable:
            - index_turn : boolean for turn player.
        Returns: Winner(Player), Looser(Player), Lap counter (the number of turn).
        """
        index_turn = True
        turn = 0

        while self.life > 0 and opponent.life > 0:
            # Dans mon cas, un tour de jeu = une tentative d'attaque(attack_attempt).
            # Dans un tour, un seul joueur attaque, pas deux.
            turn += 1

            if index_turn:
                self.attack_attempt(opponent)
                index_turn = False
            else:
                opponent.attack_attempt(self)
                index_turn = True
        # Return winner first
        return (opponent, self, turn) if self.life <= 0 else (self, opponent, turn)

    def fight_end(self, opponent: object, attack_damage: int):
        """
        ---Print in Terminal for a fight end.
        Args:
            attack_damage:
            opponent: Other player.
        """
        print(f'\n\n\nVie du joueur {opponent.pseudo} : {opponent.life}.')
        print(f'{self.pseudo} tue d\'un coup fatale {opponent.pseudo}: {attack_damage}.')
        opponent.life = 0
        print(f'Vie {opponent.pseudo}: {opponent.life} | WINNER : {self.pseudo}.')

    def attack_attempt(self, opponent: object):
        """
        ---Attack tentative on another player
        Arguments:
            opponent: It's another player Object, it's the player we're try to attack.
        Returns: Nothing, just call player.attack()
        """
        if bool(randint(0, 1)):
            self.attack(opponent)
        else:
            self.attack_failed(opponent)

    def attack(self, opponent: object):
        """
        ---Attack : Attack Opponent
        Args:
            opponent: Other Player
        Return : Nothing, If attack not failed call player.attack_success() else call player.attack_loose()
        """
        attack_damage = self.random_attack_damage()
        # If is last attack, fight end:
        if self.is_last_hitting(opponent, attack_damage):
            self.fight_end(opponent, attack_damage)
        else:
            # else remove life of opponent:
            opponent.life -= attack_damage
            self.attack_success(opponent, attack_damage)

    def attack_success(self, opponent: object, attack_damage: int):
        """
        ---Print in Terminal for a successful attack.
        Args:
            opponent: Other Player.
            attack_damage: (int) number of attack damage.
        Returns: Nothing, it's a template for terminal.
        """
        print("\n_________________________________________________________")
        print(f"{self.pseudo} attaque, --- {attack_damage} pt(s) de dégat(s) infligé à {opponent.pseudo}")
        print(f"{opponent.pseudo} >>> Vie : {opponent.life}")
        print("_________________________________________________________\n")

    def attack_failed(self, opponent: object):
        """
        ---Print in Terminal for a failed attack.
        Args:
            opponent: Other Player.
        Returns: Nothing
        """
        print(f"{self.pseudo} rate son attaque. --- {opponent.pseudo} ne perd aucun pt(s) de dégats.")

    @staticmethod
    def do_the_price_is_right():
        """
        Easter egg attached to Player Object.
        https://sametmax.com/alternative-au-do-while-en-python/
        Returns:

        """
        choice = randint(0, 100)
        while "L'utilisateur n'a pas encore deviné le prix":
            response = int(input('Devinez le prix: '))
            if response < choice:
                print('Plus grand')
            elif response > choice:
                print('Plus petit')
            else:
                break
        print('Bravo !')

    @staticmethod
    def random_attack_damage():
        return randint(1, 100)

    @staticmethod
    def is_last_hitting(opponent: object, attack_damage: int):
        """
        ---returns true if is last hitting.
        Args:
            opponent: Other player.
            attack_damage: Attack damage opponent taking.
        Returns: Boolean
        """
        return True if opponent.life - attack_damage < 0 else False

# Memo perso:
# fonction intéressante:
# - Lancer le combat : faire continuer le combat tant que quelqu'un a de la vie
# - tentative appeler la fonction attaque si elle est réussie ou print un message attaque non réussie
# - attack : attaque un autre joueur