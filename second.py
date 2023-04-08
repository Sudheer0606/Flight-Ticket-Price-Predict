import requests
from bs4 import BeautifulSoup

url = 'https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-09/04/2023&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

img_tag = soup.find_all('img')

for element in img_tag:
    print(element.get('src'))
