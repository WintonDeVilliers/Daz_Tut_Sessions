import requests
from bs4 import BeautifulSoup
import pandas as pd


## Lesson one
'''
 pseudo code  - what and why
    python fundamentals - variables, data-types
    .get(URL) functions
    relative keywords(based on use-case/context)

    Walkthrough code ( ! variable naming) 

    pseudo code  we want to do this in/using python:

    get data from absa and print on python

    url = ""
    table= url_content
    connect to db
    for record in table:
        print on python

'''


# url = ""
# page= requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")

# I wrote this because I copied the absa HTML content to a local file...will use url during lesson


with open('output.html', mode='w', newline='') as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    writer = html_content.writer(file)

# print(soup.prettify()) # to make local html look better in the console

table = soup.find('table')
header_row = table.find('tr')
headers = [header.text.strip() for header in header_row.find_all('th')]

header1_idx = headers.index('Currency')
header2_idx = headers.index('Buy Transfers')
print(header1_idx)
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')

    header1_data = cells[header1_idx].text.strip()
#     if header1_idx < len(cells): # pseudo code  - what and why
#         print("do Somethin") # python fundamentals
#     else:
#         None



    header2_data = cells[header2_idx].text.strip()
#     if header2_idx < len(cells): # pseudo code  - what and why
#         print("do Somethin") # python fundamentals
#     else: #  relative keywords(based on use-case/context)
#         None # relative keywords(based on use-case/context)

    print(f"Currency: {header1_data}, Buy Transfer: {header2_data}")





