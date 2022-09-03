# ESEA Scraper

### **Overview**

This is a project aimed towards gathering various sets of information from ESEA's website for research, scheduling and other processing.

### **Goals**

1. Easily obtain team, match, and statistical information from ESEA
2. Process retrieved information into a common format
3. Export information to Google Sheets for other uses
4. Accelerate what would be manually triggered requests, avoid pointless traffic

### **Obstacles**

1. ESEA has safeguards (Cloudflare) to prevent bots from easily scraping data
	- A modified chromium web-driver is used to imitate a browser and circumvent cloudflare
2. Creating a common format for various items (teams, matches) as the structure can be inconsistent
	- Error-checking is emphasized at each possible step

### **Setup**

1. Download dependencies:
```
pip install -r requirements.txt
```
2. Ensure Chrome is installed in its default location *(support for custom paths are planned)*

3. Initialize the chromium web-driver
```python
driver = scraper.initializeDriver()
```
4. Use the implemented scraper functions towards your desired goal
```python
# Print the dates for all of a team's matches
matches = scraper.get_team_matches(driver, teamID)
count = 1
for match in matches:
	print(f"Match #{count}: {match.date}")
	count += 1
```