import pandas as pd
from bs4 import BeautifulSoup
from bs4.element import Tag

f = open('JoSAA.html', 'r')
lines = f.read()
f.close()

soup = BeautifulSoup(lines, 'html.parser')
table = soup.find('table')
tableRows = table.find_all('tr')

headingRow: Tag
headingRow = tableRows[0]
tableRows.pop(0)
headingData = headingRow.find_all('th')

headings = []
i: Tag
for i in headingData:
    headings.append(i.get_text())

data = []

for i in tableRows:
    contentData = i.find_all('td')

    contents = []
    x: Tag
    for x in contentData:
        contents.append(x.get_text().replace('\n', '').strip())
    data.append(contents)

dataframe = pd.DataFrame(data, columns=headings)

dataframe.to_excel('josaa-cutoff.xlsx', index=False)

print('Exported to excel file!')
print('Open the exported sheet and format it as per your need.')
