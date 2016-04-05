# currency

class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    def __eq__(self, other):
        if currency_code == other.currency_code and amount == other.amount:
            return True
        else:
            return False

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount + other.amount, self.currency_code)
        else:
            raise DifferentCurrencyCodeError

    def __str__(self):
        return str(self.amount) + (' ') + (self.currency_code)

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount - other.amount, self.currency_code)
        else:
            raise DifferentCurrencyCodeError

    def __mul__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount * other.amount, self.currency_code)
        else:
            raise DifferentCurrencyCodeError

    def symbol(self):
        if self.amount[0] == '$':
            self.amount = float(self.amount[1:])
            self.currency_code = 'USD'
            return Currency(self.amount, self.currency_code)
        if self.amount[0] == '¥':
            self.amount = float(self.amount[1:])
            self.currency_code = 'JPY'
            return Currency(self.amount, self.currency_code)
        if self.amount[0] == '€':
            self.amount = float(self.amount[1:])
            self.currency_code = 'EUR'
            return Currency(self.amount, self.currency_code)

currency1 = Currency('$1.20', '')
currency2 = Currency('¥400', '')
currency3 = Currency('€7.00','')

print(currency1.symbol())
print(currency2.symbol())
print(currency3.symbol())

class DifferentCurrencyCodeError(Exception):
    pass
