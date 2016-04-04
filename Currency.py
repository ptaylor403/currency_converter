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
            return(self.amount + other.amount)
        else:
            return False
