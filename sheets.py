from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def instantiate(tokenPath="local/token.json", credPath="local/credentials.json"):
	"""
	Constructs and authenticates an instance of the Google Sheets API service
	
	Arguments
		`tokenPath="local/token.json` (str) : Filepath to token.json
		`credPath="local/credentials.json` (str) : Filepath to credentials.json

	Returns:
		Sheets API instance
	"""
	creds = None
	if os.path.exists(tokenPath):
		creds = Credentials.from_authorized_user_file(tokenPath, SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(credPath, SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open(tokenPath, 'w') as token:
			token.write(creds.to_json())	
	try:
		service = build('sheets', 'v4', credentials=creds)
		return service.spreadsheets()	
	except HttpError as err:
		print(err)

def getSpreadsheet(path="local/sheetID.txt"):
	"""
	Finds the locally stored spreadsheet ID to interact with

	Arguments
		`path="local/sheetID.txt"` (str) : Path to file with the ID

	Returns:
		`str` : locally stored spreadsheet ID
	"""
	with open(path) as file:
		return file.readline()


def clearSheet(service, sheet, spreadsheetID):
	"""
	Clears the specified sheet on the given spreadsheet

	Arguments
		`service` (?) : The Sheets API service
		`sheet` (str) : The name of the sheet to be cleared
		`spreadsheetID` (str) : The ID of the spreadsheet

	Returns:
		`str` : locally stored spreadsheet ID
	"""
	service.values().clear( 
		spreadsheetId=spreadsheetID, 
		range=sheet,               
		body={}).execute()

def writeTopLeft(service, sheet, spreadsheetID, content):
	"""
	Writes content to the top left of the specified sheet on the given spreadsheet. 

	Arguments
		`service` (?) : The Sheets API service
		`sheet` (str) : The name of the sheet to be cleared
		`spreadsheetID` (str) : The ID of the spreadsheet
		`content` (List[List]) : 2-D List of JSON serializable content

	"""
	_body = {"values" : content}
	service.values().update(
				spreadsheetId=spreadsheetID,
				range=f"{sheet}!A1",
				valueInputOption="RAW",
				body=_body).execute()



