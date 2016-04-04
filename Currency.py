# currency

class Currency:
    def __init__(self, amount, currency_code):
        self.code = currency_code
        self.amount = amount

    def __eq__(self, other):
        if currency_code == other.currency_code and amount == other.amount:
            return True
        else:
            return False
