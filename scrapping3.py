import requests
import csv
from bs4 import BeautifulSoup

# Make a GET request to the HTML tutorial page
url = 'https://www.w3schools.com/html/default.asp'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the left sidebar containing links to the HTML tutorial pages
sidebar = soup.find('div', {'class': 'w3-sidebar'})

# Find all the links in the sidebar and their corresponding names
links = sidebar.find_all('a')
link_names = [link.text for link in links]
link_urls = [url + link['href'] for link in links]

# Write the link names and URLs to a CSV file
with open('html_tutorial_links.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Tutorial Name', 'Tutorial URL'])
    for i in range(len(links)):
        writer.writerow([link_names[i], link_urls[i]])

print('CSV file created successfully!')
