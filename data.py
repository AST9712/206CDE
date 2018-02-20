
from bokeh.plotting import figure, output_file, show
import requests
import pygal


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


	def bit_coin(self):
		'''
			{
			  "time": "2017-08-09T14:31:18.3150000Z",
			  "asset_id_base": "BTC",
			  "asset_id_quote": "USD",
			  "rate": 3260.3514321215056208129867667
			}
		'''
		# self.url 	= 'https://rest.coinapi.io/v1/exchangerate'
		response 	= requests.get(self.url, headers=self.headers)
		data 		= response.json()
		rate = {}
		print (data)
		return data


	def x_axis(self):
		response = requests.get(self.url, headers=self.headers)
		data 	 = response.json()
		names = []
		for currency in data:
			names.append(currency['name'])	

		return names

a = Currencies()
b = a.bit_coin()
print (b)



class Tables:

	def __init__(self):
		pass


	def graphtest(self):


		bar_chart = pygal.Line()                                                #Then create a bar graph object
		bar_chart.add('Bit Coin',[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])      #Add some values
		bar_chart = bar_chart.render_data_uri()

		return bar_chart




