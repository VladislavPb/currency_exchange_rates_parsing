import xml.etree.ElementTree as ET
import requests

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

file_object = requests.get(url)
with open('currency.xml', 'wb') as local_file:
    local_file.write(file_object.content)

xmlp = ET.XMLParser(encoding='utf-8')
response = open('currency.xml', mode='r')
root = ET.parse(response, parser=xmlp).getroot()
forint, krone = 0, 0

for i in range(len(root)):

    if root[i][1].text == 'HUF':
        forint += float(root[i][4].text.replace(',', '.'))
        nominal = int(root[i][2].text)
        forint /= nominal

    elif root[i][1].text == 'NOK':
        krone += float(root[i][4].text.replace(',', '.'))
        nominal = int(root[i][2].text)
        krone /= nominal

answer1 = round(krone / forint, 3)
answer2 = round(forint / krone, 3)

print(f'Exchange rate of Norwegian Krone to Hungarian Foring: {answer1}')
print(f'Exchange rate of Hungarian Forint to Norwegian Krone: {answer2}')
