import requests
import unicodedata


user_id = 12345
url = 'https://www.transfermarkt.com/ac-mailand/transfers/verein/5/saison_id/2017'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
r = requests.get(url, headers=headers)
convert_text = unicodedata.normalize('NFKD', r.text).encode('ascii', 'ignore').decode('ascii')
with open('test.html', 'w') as output_file:
    output_file.write(convert_text)