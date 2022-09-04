class Team:
	""" 
	Contains relevant information about a team

	Variables:
		`name (str)` : Name of the team
		`id (str)` : numerical ID identifying the team
		`tag (str)` : Abbreviation for the team
		`league (str)` : Current division for the team
		`record (str)` : Current record for the team
		`roster (list[Player])` : All players listed on the roster
		`statistics (list[Player])` : League stats for the season
		`matches (list[Match])` : All matches for the current season
	"""
	def __init__(self):
		self.name : str = None
		self.id : str = None
		self.tag : str = None
		self.league : str = None
		self.record : str = None
		self.roster : list[Player] = None
		self.statistics : list[Statistic] = None
		self.matches : list[BasicMatch] = None

class Player:
	""" 
	Contains identifying information about a player

	Variables:
		`name (str)` : Alias of the player
		`id (str)` : numerical ID identifying the player
		`tier (str)` : Type of account the player has
	"""
	def __init__(self):
		self.name : str = None
		self.id : str = None
		self.tier : str = None

class BasicMatch:
	""" 
	Contains basic information for a match in reference to a team's results

	Variables:
		`contextTeam (Team)` : Team to which the information belongs
		`id (str)` : numerical ID identifying the match
		`map (str)` : Name of the map played in the match
		`team1 (Team)` : Team designated as "home"
		`team2 (Team)` : Team designated as "away"
		`date (str)` : GMT timestamp of the match start
		`result (str)` : The result for the team which this belongs to
		`finalScore (str)` : The score once the game concludes
	"""
	def __init__(self):
		self.contextTeam : Team = None
		self.id : str = None
		self.map : str = None
		self.team1 : Team = None
		self.team2 : Team = None
		self.date : str = None
		self.result : str = None
		self.finalScore : str = None

class Round:
	"""
	Contains relevent information for a specific round

	Variables:
		`number (str)` : Round number in question  
		`winner (Team)` : Team which won the round
		`win_reason (str)` : Indication of how the round concluded
		`score (str)` : Score at the time the round began
		`team1Value (str)` : Equipment value of team 1 at round start
		`team2Value (str)` : Equipment value of team 2 at round start
	"""
	def __init__(self):
		self.number : str = None
		self.winner : Team = None
		self.win_reason : str = None
		self.score : str = None
		self.team1Value : str = None
		self.team2Value : str = None

class Statistic:
	"""
	Contains a player's statistics over an undefined period

	Variables:
		`player (Player)` : Player to which the statistics belong  
		`allStats (dict)` : Contains all obtained statistics
		`ctStats (dict)` : Contains obtained statistics for the CT side
		`tStats (dict)` : Contains obtained statistics for the T side
	"""
	def __init__(self):
		self.player : Player = None
		self.allStats : dict = None
		self.ctStats : dict = None
		self.tStats : dict = None

class DetailedMatch:
	""" 
	Contains information for a match to the detail found on a match page

	Variables:
		`id (str)` : numerical ID for the match
		`map (str)` : name of the map played
		`team1 (Team)` : Team designated as "home"
		`team2 (Team)` : Team designated as "away"
		`tSideStart (Team)` : Team which started on the T side
		`ctSideStart (Team)` : Team which started on the CT side
		`timeStarted (str)` : GMT timestamp of the match start
		`timeFinished (str)` : GMT timestamp of the match end
		`halfScore (str)` : The score at halftime
		`finalScore (str)` : The score once the game concludes
	"""
	def __init__(self):
		self.id : str = None
		self.map : str = None
		self.team1 : Team = None
		self.team2 : Team = None
		self.tSideStart : Team = None
		self.ctSideStart : Team = None
		self.timeStarted : str = None
		self.timeFinished : str = None
		self.halfScore : str = None
		self.finalScore : str = None
		self.rounds : list[Round] = None
		self.stats : list[Statistic] = None



