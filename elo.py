class ELO_management(object):
    def __init__(self):
        self.player_elo_cache = {}
        self.starting_elo = 1600

    def update_elo(self, player, new_elo):
        self.cache_checker(player)
        """Is this the intended functionality? This would be a situation where you're checking for
        the presence of a player and in the event that player isn't in the cache default value 
        would be applied, you would then come to the next line and be applying a new elo socre to
        them thus overrideing the default value placement"""
        self.player_elo_cache[player] = new_elo
        return 0

    # def calculate_elo(self, player1, player2):
    #     cached_scores = self.fetch_elos(player1, player2)

    def fetch_elo(self, player):
        """return `player1` and `player2` elo scores from the class cache.
        integrety check is completed by `cache_checker` to ensure players are available"""
        self.cache_checker(player)
        return self.player_elo_cache[player]

    def cache_checker(self, player):
        """Ensure that every player passed is either present in the cache with an active elo score.
        In the event a player is not in the cache calls `new_player` to update cache"""
        if player not in self.player_elo_cache.keys():
            self.new_player(player)
        return 0

    def new_player(self, player):
        """ When passed a player, adds the player to the cache of players using the default starting
        elo value, referenced from `self.starting_elo`"""
        self.player_elo_cache.update({player:self.starting_elo})
        return 0

    def show_cache(self):
        print(self.player_elo_cache)


class ELO(object):
    def __init__(self, K=32, player_list=[]):
        self.EM = ELO_management()
        self.K = K
        if len(player_list) > 0:
            [self.EM.new_player(player) for player in player_list]

    @staticmethod
    def get_win_probibility(player1_elo, player2_elo):
        """Compute the head to head win probilbility for each player."""
        player1_w_prob = (1.0 / (1.0 + 10**((player2_elo - player1_elo) / 400)))
        player2_w_prob = (1.0 / (1.0 + 10**((player1_elo - player2_elo) / 400)))

        return player1_w_prob, player2_w_prob

    def do_competition(self, winner, loser):
        """Retrieve each of the players current elo ratings by using the ELO_management class.
        Then apply new ratings based on which player has won"""
        winner_elo = self.EM.fetch_elo(winner)
        loser_elo = self.EM.fetch_elo(loser)

        winner_w_prob, loser_w_prob = self.get_win_probibility(winner_elo, loser_elo)
        winner_new_elo = winner_elo + self.K * (1 - winner_w_prob)
        loser_new_elo = loser_elo + self.K * (0 - loser_w_prob)

        if loser_new_elo < 0:
            loser_new_elo = 0
        
        self.EM.update_elo(winner, winner_new_elo)
        self.EM.update_elo(loser, loser_new_elo)
        return 0

    def add_players(self, player_list):
        for player in player_list:
            self.EM.new_player(player)
        return 0

    # def 
    #     cached_scores = {}
    #     for player in [player1,player2]:
    #         cached_scores.update({player:self.player_elo_cache[player]})
    #     return cached_scores
    # def 