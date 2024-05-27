class Transaction:
    def __init__(self, account_number, transaction_type, amount):
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount

    def record_transaction(self):
        # Logic to record transaction in database or file
        pass
