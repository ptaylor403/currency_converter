# currency converter

from currency import *

class CurrencyConverter(Currency):
    def __init__(self, currency_rates = {'USD': 1, 'EUR': 0.87}):
        self.currency_rates = currency_rates

    def convert(self, rate, currency_code):
        self.rate = rate
        self.currency_code = currency_code


class UnknownCurrencyCodeError(Exception):
    pass

def main():

if __name__ == '__main__':
    main()
