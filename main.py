from operator import truediv
import os
import utils
import scraper
import sheets

if __name__ == "__main__":

	teamID = input("Enter team ID (play.esea.net/teams/~ID~): ")
	timer = utils.Stopwatch()
	timer.tick()
	driver = scraper.initializeDriver()
	print(f"Driver initialized in {timer.tick()}s")
	
	try:		
		sheetsAPI = sheets.instantiate()
		inSheet = sheets.getSpreadsheet("local/inSheet.txt")
		outputSheet = sheets.getSpreadsheet("local/outSheet.txt")
		teams = sheets.readColumn(sheetsAPI, "Tracker", inSheet, "A", True)
		sheets.clearSheet(sheetsAPI, "Schedule", outputSheet)
		content = []
		for team in teams:
			_team = team[0]
			print(f"Working on {_team}")
			_matches = scraper.get_team_matches(driver, _team)
			print(f"Retrieved schedule for {_team}")
			for match in _matches:
				_date = (match.date if match.date != None else "")
				hoursLeft = utils.hoursUntil(utils.strGMTtoStruct(_date))
				if((hoursLeft > 0) and (hoursLeft < 48)):
					print(hoursLeft)
					_match = []
					_match.append((match.team1.name if match.team1 != None else ""))
					_match.append((match.team2.name if match.team2 != None else ""))
					_match.append((match.map if match.map != None else ""))
					_match.append(_date)
					content.append(_match)
				else:
					continue
		
		sheets.writeTopLeft(sheetsAPI, "Schedule", outputSheet, content)
	except Exception as e:
		print(e)

	finally:
		driver.quit()
		os._exit(0)


	