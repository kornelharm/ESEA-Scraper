class Team:
	def __init__(self):
		self.name : str = None
		self.id : str = None
		self.tag : str = None
		self.league : str = None
		self.record : dict = {"win":None,"loss":None,"tie":None}
		self.roster : list[Player] = None
		self.statistics : list = None
		self.matches : list[Match] = None

class Player:
	def __init__(self):
		self.name : str = None
		self.id : str = None
		self.tier : str = None

class Match:
	def __init__(self):
		self.id : str = None
		self.map : str = None
		self.team1 : Team = None
		self.tSideStart : Team = None
		self.ctSideStart : Team = None
		self.team2 : Team = None
		self.timeStarted : str = None
		self.timeFinished : str = None
		self.halfScore : str = None
		self.finalScore : str = None



