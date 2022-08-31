import os
import utils
import scraper

if __name__ == "__main__":

	teamID = input("Enter team ID (play.esea.net/teams/~ID~): ")
	timer = utils.stopwatch()
	driver = scraper.initializeDriver()
	print(f"Driver initialized in {timer.tick()}s")
	
	try:		
		timer.tick()
		scraper.get_team_matches(driver, teamID, False)
		print(f"Team {teamID} retrieved in {timer.tick()}s")
		scraper.get_team_matches(driver, 8778400, False)
		print(f"Team 8778400 retrieved in {timer.tick()}s")

	finally:
		driver.quit()
		os._exit(0)


	