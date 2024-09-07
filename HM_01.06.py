#Here I create an online shop where a customer can be a buyer to purchase other people's items and also a seller of his own items.
import datetime

class Client:
    number_of_clients = 0  

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.accounts = []
        self.transactions = []
        Client.number_of_clients += 1

    def add_account(self, account):
        self.accounts.append(account)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def total_spent(self):
        total = sum(transaction.amount for transaction in self.transactions if transaction.type == "purchase")
        return total

    def total_earned(self):
        total = sum(transaction.amount for transaction in self.transactions if transaction.type == "sale")
        return total

    def __str__(self):
        return (f"Client: {self.name} {self.surname}, Total Spent: {self.total_spent()} Eur, "
                f"Total Earned: {self.total_earned()} Eur")

class Account:
    def __init__(self):
        self.transactions = []
        self.balance = 0

    def bought_items(self, amount, narrative):
        self.transactions.append(Transaction(amount, narrative, "purchase"))
        self.balance -= amount

    def sold_items(self, amount, narrative):
        self.transactions.append(Transaction(amount, narrative, "sale"))
        self.balance += amount

    def __str__(self):
        return "Balance: " + str(self.balance) + " Eur"

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "Item: " + self.name + ", Price: " + str(self.price) + " Eur"

class Transaction:
    def __init__(self, amount, narrative, transaction_type):
        self.amount = amount
        self.narrative = narrative
        self.type = transaction_type
        self.items = []
        self.time_stamp = datetime.datetime.now()

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        result = f"Transaction ({self.type}) at " + str(self.time_stamp) + ":\n"
        for item in self.items:
            result += "  - " + str(item) + "\n"
        return result

clients = []
client1 = Client("Liene", "Berzina")
client2 = Client("Janis", "Kalnins")
clients.append(client1)
clients.append(client2)

item1 = Item("T_shirt", 10)
item2 = Item("Trousers", 30)
item3 = Item("Lee Couper Jeans", 70)
item4 = Item("Jacket", 100)
item5 = Item("Phase 8 Dress", 150)

transaction1 = Transaction(80, "Bought T_shirt and Jeans", "purchase")
transaction1.add_item(item1)
transaction1.add_item(item3)

transaction2 = Transaction(130, "Bought Trousers and Jacket", "purchase")
transaction2.add_item(item2)
transaction2.add_item(item4)

transaction3 = Transaction(150, "Sold Dress", "sale")
transaction3.add_item(item5)

client1.add_transaction(transaction1)
client2.add_transaction(transaction2)
client2.add_transaction(transaction3)

print('We have ' + str(Client.number_of_clients) + ' clients in our AndeleMandele online shop:')
for client in clients:
    print(client)
    for transaction in client.transactions:
        print(transaction)
