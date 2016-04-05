# currency converter

from currency import *

class CurrencyConverter(Currency):
    exchange_rates = {
        'USD': 1,
        'EUR': 0.87,
        'JPY': 111.3
    }

    def __init__(self, rate):
        self.rate = rate

    def convert(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code
        


class UnknownCurrencyCodeError(Exception):
    pass

def main():

if __name__ == '__main__':
    main()
