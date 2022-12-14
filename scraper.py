from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import json
import time
from objects import *

def initializeDriver():
	"""
	Initializes chromium web driver used for data retrieval
	
	Returns: 
		`Chrome` : Chromium web driver instance
	"""
	chromeOptions = Options()
	chromeOptions.headless = True
	# Instantiation of the undetected_chromedriver driver. Used to bypass cloudflare
	driver = uc.Chrome(options=chromeOptions)
	driver.implicitly_wait(30)
	return driver

def team_id_to_matches(teamID):
	"""
	Return the API URL for the team's respective matches

	Arguments: 
		`teamID (str)` : numerical ID for a team

	Returns: 
		`str` : API URL to the team's matches
	"""
	return f"https://play.esea.net/api/teams/{teamID}/matches"

def match_id_to_match(matchID):
	"""
	Return the API URL for the detailed match information

	Arguments: 
		`matchID (str)` : numerical ID for a team

	Returns: 
		`str` : API URL to the match page information
	"""
	return f"https://play.esea.net/api/match/{matchID}/overview"

def team_id_to_stats(teamID):
	"""
	Returns the API URL for the team's respective statistics

	Arguments:
		`teamID (str)` : numerical ID for a team

	Returns: 
		`str` : API URL to the team's statistics
	"""
	return f"https://play.esea.net/api/teams/{teamID}/stats"


# Returns a list of matches representing the specified team's matches
def get_team_matches(driver, teamID):
	"""
	Retrieves the basic information for the specified team's matches
	For more match information, see `get_match_information()`

	Arguments: 
		`driver (Chrome)` : Chromium web driver instance
		`teamID (str)` : numerical ID for a team

	Returns: 
		`list[BasicMatch]` : List with elements representing a match
	"""
	result : list[BasicMatch] = []
	driver.get(team_id_to_matches(teamID))
	info = driver.page_source
	time.sleep(2) # Sleep for RAM reasons ¯\_(ツ)_/¯ not willing to touch
	soup = BeautifulSoup(info, "lxml")
	body = soup.body.contents[0].contents[0]
	bodyJSON = json.loads(body)
	matches = bodyJSON["data"]
	count=0
	for match in matches:
		# Each match is guaranteed to have a date and map (even if TBD) 
		# Teams are assigned once match page is created
		# Result and score are assigned at match conclusion
		_match = BasicMatch()
		team1JSON = match["home"] if "home" in match else None
		team2JSON = match["away"] if "away" in match else None
		team1 = Team()
		team2 = Team()
		# Establish which team is which
		if(team1JSON != None and team2JSON != None):
			if(team1JSON["id"] == teamID):
				team1.id = team1JSON["id"]
				team1.name = team1JSON["name"]
				team1.tag = team1JSON["tag"]
				team2.id = team2JSON["id"]
				team2.name = team2JSON["name"]
				team2.tag = team2JSON["tag"]
				_match.contextTeam = team1
				_match.team1 = team1
				_match.team2 = team2
			else:
				team1.id = team2JSON["id"]
				team1.name = team2JSON["name"]
				team1.tag = team2JSON["tag"]
				team2.id = team1JSON["id"]
				team2.name = team1JSON["name"]
				team2.tag = team1JSON["tag"]
				_match.contextTeam = team2
				_match.team2 = team2
				_match.team1 = team1

		if("map" in match):
			if(match["map"] == "Multiple"):
				_match.map = "Multiple"
			elif("id" in match["map"]):
				_match.map = match["map"]["id"]
			else:
				_match.map = "TBD"
		_match.result = ("WON" if match["result"] == 1 else "LOST") if "result" in match else None
		_match.finalScore = match["score"] if "score" in match else None
		_match.date = match["date"]
		result.append(_match)

	return result

# TODO: Implement
def get_match_information(driver, matchID):
	"""
	Retrieves the advanced information for a specific
	To retrieve the matchID, see `get_team_matches()`

	Arguments: 
		`driver (Chrome)` : Chromium web driver instance
		`teamID (str)` : numerical ID for a team

	Returns: 
		`list[DetailedMatch]` : List with elements representing a match
	"""
	pass