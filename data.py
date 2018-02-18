
from bokeh.plotting import figure, output_file, show
import requests


class Currencies:
	

	def __init__(self):
		self.url 	 = 'https://rest.coinapi.io/v1/exchanges'
		self.headers = {'X-CoinAPI-Key':'79D6A8A6-E274-46D7-93F4-6168C6BC8132'}

	def names(self):
		''' return the Cryptocurrencies names'''
		response = requests.get(self.url, headers=self.headers)
		data 	 = response.json()
		names = []

		for currency in data:
			names.append(currency['name'])
		return names


	def rates(self):
		ccurrencies = []

		response 	= requests.get(self.url, headers=self.headers)
		data 	 	= response.json()

		for ccurrency in data:
			print (ccurrency)
			ccurrencies.append(ccurrency)
		return ccurrencies


	def rates_according(self):
		''' will return the rates '''
		pass

	def x_axis(self):
		response = requests.get(self.url, headers=self.headers)
		data 	 = response.json()
		names = []
		for currency in data:
			names.append(currency['name'])	

		return x






class Tables:

	def __init__(self):
		pass


