import os
import utils
import scraper

if __name__ == "__main__":

	teamID = input("Enter team ID (play.esea.net/teams/~ID~): ")
	timer = utils.Stopwatch()
	driver = scraper.initializeDriver()
	print(f"Driver initialized in {timer.tick()}s")
	
	try:		
		timer.tick()
		matches = scraper.get_team_matches(driver, teamID)
		print(f"Team {teamID} retrieved in {timer.tick()}s")
		for match in matches:
			team1 = match.team1.name if not (match.team1 == None) else "-"
			team2 = match.team2.name if not (match.team1 == None) else "-"
			print(f"{team1} vs. {team2} : {match.date}")

	finally:
		driver.quit()
		os._exit(0)


	