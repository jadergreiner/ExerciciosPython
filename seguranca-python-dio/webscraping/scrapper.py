from bs4 import BeautifulSoup
import requests

site = requests.get("http://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

title = soup.find("li", class_ = "item -title")

print(title.string)