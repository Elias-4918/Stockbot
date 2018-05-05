import urllib2
import json
import progressbar

URL = "https://api.iextrading.com/1.0/"
def load_symbols():
	print '[+] Loading Symbols...'
	symbols_data_notJSON = urllib2.urlopen(URL+"ref-data/symbols").read()
	print "[+] "+ str(len(symbols_data_notJSON)) +" Symbols Loaded."
	return json.loads(symbols_data_notJSON)

class stock_class:

	def __init__(self, stock_info):  #stock info looks like this: {u'name': u'Agilent Technologies Inc.', u'symbol': u'A', u'iexId': u'2', u'date': u'2018-05-04', u'type': u'cs', u'isEnabled': True}
		self.name = stock_info["name"]
		self.symbol = stock_info["symbol"]
		self.iexId = stock_info["iexId"]
		self.date = stock_info["date"]
		self.type = stock_info["type"]
		self.isEnabled = stock_info["isEnabled"]

	def printName(self):
		print self.symbol
'''
	def getPE(stock):
		return 0

	def getEPS():
		return 0
'''

def load_stocks(symbols):
	symbolsdict = {i: None for i in range(len(symbols))}
	for stock in symbols:
		symbolsdict[stock['symbol']]=stock_class(stock)
	return symbolsdict


def main():
	symbols = load_symbols()
	symboldict = load_stocks(symbols)


main()


