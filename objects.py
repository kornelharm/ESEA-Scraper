class Team:
	""" 
	Class representing a team and its relevant information.
	Depending on their use, not all fields are guaranteed to exist
	"""
	def __init__(self):
		self.name : str = None
		self.id : str = None
		self.tag : str = None
		self.league : str = None
		self.record : dict = {"win":None,"loss":None,"tie":None}
		self.roster : list[Player] = None
		self.statistics : list = None
		self.matches : list[BasicMatch] = None

class Player:
	""" 
	Class representing a player and their relevant information.
	Depending on their use, not all fields are guaranteed to exist
	"""
	def __init__(self):
		self.name : str = None
		self.id : str = None
		self.tier : str = None

class BasicMatch:
	""" 
	Class representing a match in reference to a team's results.
	Depending on their use, not all fields are guaranteed to exist
	"""
	def __init__(self):
		self.contextTeam : str = None
		self.id : str = None
		self.map : str = None
		self.team1 : Team = None
		self.team2 : Team = None
		self.date : str = None
		self.result : str = None
		self.finalScore : str = None

# Class representing a match page
class DetailedMatch:
	""" 
	Class representing a match in reference to a match page.
	Depending on their use, not all fields are guaranteed to exist

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



