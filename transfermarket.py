from lxml import html
import requests


url = 'https://www.transfermarkt.com/ac-mailand/transfers/verein/5/saison_id/2017'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
page = requests.get(url, headers=headers)
tree = html.fromstring(page.content)
players = tree.xpath('//a[@class="spielprofil_tooltip"]/text()')

print('Players: ', players)

