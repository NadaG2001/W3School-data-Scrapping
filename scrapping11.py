import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the Java tutorials page
url = "https://www.w3schools.com/java/default.asp"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the tutorial titles and links on the page
tutorials = soup.select("#leftmenuinnerinner a")

# Write the tutorial titles and links to a CSV file
with open("w3schools_java_tutorials.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for tutorial in tutorials:
        title = tutorial.text.strip()
        link = "https://www.w3schools.com" + tutorial["href"]
        writer.writerow([title, link])
