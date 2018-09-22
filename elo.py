class ELO(object):
    def __init__(self):
        self.player_elo_cache = {}
        self.starting_elo = 1600

    def update_elo(self, team, new_elo):

    def calculate_elo(self, player1, player2):

    def fetch_elos(self, player1, player2):
    	"""return `player1` and `player2` elo scores from the class cache.
    	integrety check is completed by `cache_checker` to ensure players are available"""
        self.cache_checker(player1)
        self.cache_checker(player2)


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