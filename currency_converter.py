# currency converter

from currency import *

class CurrencyConverter(Currency):
    def __init__(self, currency_codes):
        self.currency_codes = currency_codes

    def convert(self, rate, currency_code):
        pass

class UnknownCurrencyCodeError(Exception):
    pass
