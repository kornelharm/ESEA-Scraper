from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import os
import json


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def instantiate(credPath="local/credentials.json"):
	"""
	Constructs and authenticates an instance of the Google Sheets API service
	
	Arguments
		`credPath="local/credentials.json` (str) : Filepath to service account credentials

	Returns:
		Sheets API instance
	"""
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credPath
	creds = None
	if os.path.exists(credPath):
		accountInfo = json.load(open(credPath))
		creds = service_account.Credentials.from_service_account_info(accountInfo, scopes=SCOPES)
	else:
		raise Exception("Credentials file could not be found")
	try:
		service = build('sheets', 'v4', credentials=creds)
		return service.spreadsheets()	
	except HttpError as err:
		print(err)

def getSpreadsheet(path):
	"""
	Finds the locally stored spreadsheet ID to interact with

	Arguments
		`path` (str) : Path to file with the ID

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

def readColumn(service, sheet, spreadsheetID, column, ignoreHeader):
	"""
	Reads content in the column of the specified sheet on the given spreadsheet. 

	Arguments
		`service` (?) : The Sheets API service
		`sheet` (str) : The name of the sheet to be cleared
		`spreadsheetID` (str) : The ID of the spreadsheet
		`column` (str) : Letter indicating desired column
		`ignoreHeader` (bool) : Determines whether first row is read
	"""
	columnRange = f"{sheet}!{column}"
	if(ignoreHeader):
		columnRange = f"{sheet}!{column}2:{column}"
	resp = service.values().get(
				spreadsheetId=spreadsheetID,
				range=columnRange,
				valueRenderOption="FORMATTED_VALUE").execute()
	return resp["values"]



