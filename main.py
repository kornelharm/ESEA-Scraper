from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time
import json
import os

# Used for timing 
class stopwatch:
	def __init__(self, startTime=time.time()):
		self.currTime = startTime

	# Ticks the stopwatch, returns seconds passed since last tick
	def tick(self):
		temp = self.currTime
		self.currTime = time.time()
		return self.currTime - temp

# Initializes chromium web driver used for data retrieval
def initializeDriver():
	chromeOptions = Options()
	chromeOptions.headless = True
	# Instantiation of the undetected_chromedriver driver. Used to bypass cloudflare
	driver = uc.Chrome(options=chromeOptions)
	driver.implicitly_wait(30)
	return driver

# Takes a team's ID and returns an API link to their match information
def team_id_to_matches(teamID):
	return f"https://play.esea.net/api/teams/{teamID}/matches"


# Returns an array of Dicts representing the specified team's matches
def get_team_matches(driver, teamID, prettyPrint=False):
	
	driver.get(team_id_to_matches(teamID))
	info = driver.page_source
	time.sleep(2) # Sleep for RAM reasons ¯\_(ツ)_/¯
	soup = BeautifulSoup(info, "lxml")
	body = soup.body.contents[0].contents[0]
	bodyJSON = json.loads(body)
	matches = bodyJSON["data"]

	if(prettyPrint):
		header = '''      HOME      |      AWAY       |     MAP      | RESULT\n----------------+-----------------+--------------+-------'''
		print(header)
		for match in matches:
			home = match["home"]["name"] if "home" in match else "-"
			away = match["away"]["name"] if "away" in match else "-"
			location = (match["map"]["id"] if "id" in match["map"] else "-") if "map" in match else "-"
			won = ("WON" if match["result"] == 1 else "LOST") if "result" in match else "-"
			print(f"{home.center(15)[:15]} | {away.center(15)[:15]} | {location.center(12)[:12]} | {won.center(5)[:5]}")

	return matches

if __name__ == "__main__":

	teamID = input("Enter team ID (play.esea.net/teams/~ID~): ")
	timer = stopwatch()
	driver = initializeDriver()
	print(f"Driver initialized in {timer.tick()}s")
	
	try:		
		timer.tick()
		get_team_matches(driver, teamID, False)
		print(f"Team {teamID} retrieved in {timer.tick()}s")
		get_team_matches(driver, 8778400, False)
		print(f"Team 8778400 retrieved in {timer.tick()}s")

	finally:
		driver.quit()
		os._exit(0)


	