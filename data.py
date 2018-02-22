
import requests
import pygal
import json
import cryptocompare

class Currencies:


	def __init__(self):
		self.url 	 = 'https://rest.coinapi.io/v1/exchanges'
		self.headers = {'X-CoinAPI-Key':'79D6A8A6-E274-46D7-93F4-6168C6BC8132'}


	def names(self):
		''' return the Cryptocurrencies names'''
		response 	= requests.get(self.url, headers=self.headers)
		data 	 	= response.json()
		names 		= []
		self.id_ex 	= []

		for currency in data:
			names.append(currency['name'])
			self.id_ex.append(currency['exchange_id'])
		return names


	def rates(self):

		ccurrencies = []

		response 	= requests.get(self.url, headers=self.headers)
		data 	 	= response.json()

		for ccurrency in data:
			ccurrencies.append(ccurrency)
		return ccurrencies


	def exchangerate(self):
		''' stores all the exchange rates '''
		rates 	= []
		names	= self.names()
		spaces 	= [] # names with spaces.
		for kk in self.id_ex:
			print (kk)

		for cc in self.id_ex:
			if ' ' in cc:
				spaces.append(cc)
			else:
				url = 'https://rest.coinapi.io/v1/exchangerate/%s' %cc
				response 	= requests.get(url, headers=self.headers)
				data 	 	= response.json()
				rates.append({
					'name': cc,
					'data': data
					})
		return rates



	def assets(self):
		''' stores all the assets names '''
		url = 'https://rest.coinapi.io/v1/assets'
		response 	= requests.get(url, headers=self.headers)
		data 	 	= response.json()
		asset_names = []

		for name in data:
			asset_names.append(name['asset_id'])
		return asset_names


	def exchange_rate (self):
		'''  '''
		ex_rate = []
		asset_names = self.assets()

		for name in asset_names:
			url = 'https://rest.coinapi.io/v1/exchangerate/{}'.format(name)
			response = requests.get(url, headers=self.headers)
			data = response.json()
			ex_rate.append({
			'data' : data
			})

		return ex_rate




class Tables:

	def __init__(self):
		pass


	def graphtest(self):

		#Then create a bar graph object
		bar_chart = pygal.Line()
		#Add some values
		bar_chart.add('Bit Coin',[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
		bar_chart = bar_chart.render_data_uri()

		return bar_chart




'''
make a list of the Currencies
and try to make a db

'''



class CryptocompareAPI(object):
	"""Cryptocurrencies using APIS... """
	def __init__(self):
		self.url = 'https://www.cryptocompare.com/api/data/coinlist/'

	def get_data(self):
		response 	= requests.get(self.url)
		data 	 	= response.json()
		print (json.dumps(data, indent=4, sort_keys=True)) # pretty print json



class CryptocompareMOD(object):

	''' Cryptocurrencies using cryptocompare module '''

	def __init__(self):
		pass

	def coinlist(self):
		s = cryptocompare.get_coin_list(format=False)
		print (json.dumps(s, indent=4, sort_keys=True))

	def ccompare(self):
		pass

	def history(self):
		pass

	def __str__(self):
		return 'cryptocompare module'


a = CryptocompareMOD()
a.coinlist()
