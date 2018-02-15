
import requests


class Currencies:
	
	def __init__(self):

		self.url 	 = 'https://rest.coinapi.io/v1/exchanges'
		self.headers = {'X-CoinAPI-Key':'79D6A8A6-E274-46D7-93F4-6168C6BC8132'}

	def names(self):
		response = requests.get(self.url, headers=self.headers)
		data 	 = response.json()
		''' return the Cryptocurrencies names'''
		names = []
		for currency in data:
			names.append(currency['name'])
		return names











