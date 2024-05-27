from flask import Flask, request
from account import Account
from transaction import Transaction

app = Flask(__name__)

accounts = {}


@app.route('/login', methods=['POST'])
def login():
    account_number = request.json['account_number']
    if account_number in accounts:
        return "Login successful"
    else:
        return "Account not found"


@app.route('/deposit', methods=['POST'])
def deposit():
    account_number = request.json['account_number']
    amount = request.json['amount']
    if account_number in accounts:
        accounts[account_number].deposit(amount)
        transaction = Transaction(account_number, "deposit", amount)
        transaction.record_transaction()
        return "Amount deposited successfully"
    else:
        return "Account not found"


@app.route('/withdraw', methods=['POST'])
def withdraw():
    account_number = request.json['account_number']
    amount = request.json['amount']
    if account_number in accounts:
        accounts[account_number].withdraw(amount)
        transaction = Transaction(account_number, "withdrawal", amount)
        transaction.record_transaction()
        return "Amount withdrawn successfully"
    else:
        return "Account not found"


if __name__ == '__main__':
    app.run()
