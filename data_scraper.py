import bs4 as bs
import requests

class GetData:

	def __init__(self, url):
		self.url = url
		self.data_rows = []
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
		self.html = ''

	def get_html(self):
		req = requests.get(self.url, headers=self.headers)
		self.html = bs.BeautifulSoup(req.text, "lxml")

	def get_data(self):
		self.get_html()
		for tbl in self.html.find_all('table', attrs={'id':'curr_table'}):
			for i in tbl.find_all('tr'):
				self.data_rows.append([x.text for x in i.find_all('td')])	

auddata = GetData('https://www.investing.com/currencies/usd-aud-historical-data')
auddata.get_data()
print(auddata.data_rows)
