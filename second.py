import requests
from bs4 import BeautifulSoup

url = 'https://flight.easemytrip.com/FlightList/Index?org=DEL-Delhi,India&dept=BOM-Mumbai,India&adt=1&chd=0&inf=0&cabin=0&airline=Any&deptDT=09/04/2023&arrDT=undefined&isOneway=true&isDomestic=true&&CCODE=IN&curr=INR'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

img_tag = soup.find_all(id='spnPrice1')
for element in img_tag:
    print(element.text)
