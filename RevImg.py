import requests
import json
from bs4 import BeautifulSoup

class RevImg:

	def __execute_query(self, img_url, count=0):
		base_google = "https://www.google.com/searchbyimage?hl=en-US&image_url="
		headers = {
		    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
		}
		url = "{}{}&start={}".format(base_google, img_url, count)
		r = requests.get(url, headers=headers, allow_redirects = True)
		return r.text

	def get_similar(self, img_url):

		q = self.__execute_query(img_url)
		soup = BeautifulSoup(q, 'html.parser')

		results = []

		for similar_image in soup.findAll('div', attrs={'rg_meta'}):
			tmp = json.loads(similar_image.get_text())
			img_url = tmp['ou']
			results.append(img_url)

		return results

	def get_best_guess(self, img_url):
		q = self.__execute_query(img_url)
		soup = BeautifulSoup(q, 'html.parser')
		for best_guess in soup.findAll('a', attrs={'class':'fKDtNb'}):
			result = best_guess.get_text()
		return result

	def get_related_results(self, img_url):
		count = 0
		keep_searching = True
		while keep_searching:
			q = self.__execute_query(img_url, count)
			soup = BeautifulSoup(q, 'html.parser')

			results = {
				'links': [],
				'descriptions': [],
			}
			for div in soup.findAll('div', attrs={'class':'rc'}):
				sLink = div.find('a')
				results['links'].append(sLink['href'])

			for desc in soup.findAll('span', attrs={'class':'st'}):
				results['descriptions'].append(desc.get_text())

			for link, description in zip(results["links"], results["descriptions"]):
				ret = {
					"link": link,
					"description": description
				}
				yield ret
			count += 10
			check_end_cur = soup.find("td", attrs={"class": "cur"})
			try:
				test = check_end_cur.next_sibling.td
			except AttributeError:
				keep_searching = False

