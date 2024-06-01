#Creat bank account
```py
import datetime

class Client:
  number_of_clients = 0  

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.accounts = []
    Client.number_of_clients += 1

  def add_account(self, account):
    self.accounts.append(account)

class Account:
  def __init__(self, number, currency, balance = 0.0):
    self.number = number
    self.currency = currency
    self.balance = balance
    self.transactions = []

  def make_deposit(self, amount, note):
    self.transactions.append(Transaction(self.currency, amount, note))
    self.balance += amount

  def make_withdrawal(self, amount, note):
    self.transactions.append(Transaction(self.currency, -amount, note))
    self.balance -= amount

class Transaction:
  def __init__(self, currency, amount, note):
    self.currency = currency
    self.amount = amount
    self.note = note
    self.time_stamp = datetime.datetime.now()

# now, let us work using those classes
# adding clients to a list
clients = []
clients.append(Client('123456', 'Anna'))
clients.append(Client('987654', 'Oskar'))
clients.append(Client('456123', 'Jenifer'))

# adding accounts to clients
clients[0].add_account(Account('EE654987564321', 'EUR', 1000.0))
clients[0].add_account(Account('JP582147859635', 'JPY', 25000.30))
clients[0].add_account(Account('US654987643214', 'USD'))
clients[1].add_account(Account('PL849512635445', 'PLN', 47800.00))
clients[2].add_account(Account('SE741254956587', 'SEK', 200.18))


# let's make some transactions
clients[0].accounts[0].make_deposit(1200, 'Salary')
clients[0].accounts[0].make_withdrawal(50, 'Grocery')
clients[0].accounts[0].make_withdrawal(140, 'Clothes')
clients[0].accounts[0].make_withdrawal(20, 'Dinner')

# printing some data
print(f'We have {Client.number_of_clients} clients in our bank:')

for client in clients:
  print(f'Client {client.name} has the following accounts:')
  for account in client.accounts:
    print(f'    {account.number} ({account.currency}) {account.balance}')
    for transaction in account.transactions:
      print(f'        {transaction.time_stamp} {transaction.currency} {transaction.amount}')
```
