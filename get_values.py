from bs4 import BeautifulSoup
import json
import urllib3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pangrams', action='store_true', help='Only output pangrams')
parser.add_argument('-u', '--url', type=str, help='URL to the spelling bee site', default='https://www.nytimes.com/puzzles/spelling-bee')
args = parser.parse_args()

http = urllib3.PoolManager()
nyt_page = http.request('GET', args.url).data.decode('utf-8')
http.clear()

soup = BeautifulSoup(nyt_page, 'html.parser')
div = soup.find('div', class_='pz-content pz-hide-loading')
game_data = json.loads(div.find('script').string.removeprefix('window.gameData = '))

if args.pangrams:
    answers = game_data['today']['pangrams']
else:
    answers = game_data['today']['answers']

for item in answers:
    print(item)