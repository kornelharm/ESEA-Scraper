import os
import utils
import scraper
import sheets
from googleapiclient.errors import HttpError

if __name__ == "__main__":

	teamID = input("Enter team ID (play.esea.net/teams/~ID~): ")
	timer = utils.Stopwatch()
	timer.tick()
	driver = scraper.initializeDriver()
	print(f"Driver initialized in {timer.tick()}s")
	
	try:		
		sheetsAPI = sheets.instantiate()
		spreadsheetID = sheets.getSpreadsheet()
		sheets.clearSheet(sheetsAPI, "Schedule", spreadsheetID)
		matches = scraper.get_team_matches(driver, teamID)
		content = []
		for match in matches:
			_match = []
			_match.append((match.team1.name if match.team1 != None else ""))
			_match.append((match.team2.name if match.team2 != None else ""))
			_match.append((match.map if match.map != None else ""))
			_match.append((match.date if match.date != None else ""))
			content.append(_match)
		
		sheets.writeTopLeft(sheetsAPI, "Schedule", spreadsheetID, content)


	finally:
		driver.quit()
		os._exit(0)


	