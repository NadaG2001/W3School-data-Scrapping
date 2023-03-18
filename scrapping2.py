import requests
from bs4 import BeautifulSoup
import csv

# Make a GET request to the HTML tutorial page
url = 'https://www.w3schools.com/html/default.asp'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the left sidebar containing links to the HTML tutorial pages
sidebar = soup.find('div', {'class': 'w3-sidebar'})

# Find all the links in the sidebar and their corresponding names
links = sidebar.find_all('a')

# Store the links and names in a list of dictionaries
html_tutorials = []
for link in links:
    tutorial = {}
    tutorial['name'] = link.get_text()
    tutorial['link'] = link.get('href')
    html_tutorials.append(tutorial)

# Save the data to a CSV file
with open('html_tutorials.csv', mode='w', newline='') as csv_file:
    fieldnames = ['name', 'link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for tutorial in html_tutorials:
        writer.writerow(tutorial)
