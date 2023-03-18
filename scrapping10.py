import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the Python tutorials page
url = "https://www.w3schools.com/python/default.asp"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the tutorial titles and links on the page
tutorials = soup.select("#leftmenuinnerinner a")

# Write the tutorial titles and links to a CSV file
with open("w3schools_python_tutorials.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for tutorial in tutorials:
        title = tutorial.text.strip()
        link = "https://www.w3schools.com/python/" + tutorial["href"]
        writer.writerow([title, link])
