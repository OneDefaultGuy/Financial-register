import os
from datetime import datetime


def get_balance():
    with open("transactions.txt", "r") as file:
        lines = file.readlines()
        last_transaction = lines[-1].split("\t")
        balance = int(last_transaction[-1])
        return balance


def create_table():
    if not os.path.exists("transactions.txt"):
        with open("transactions.txt", "a") as file:
            file.write("Timestamp\t\tTransaction\tAmount\tBalance\n")


def insert_transaction(transaction_type, amount, balance):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("transactions.txt", "a") as file:
        file.write(f"{timestamp}\t{transaction_type}\t{amount}\t{balance}\n")


class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)


class Bank(User):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.amount = None
        self.balance = get_balance()

    def deposits(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated: ₴", self.balance)
        insert_transaction('Deposit', amount, self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : ₴", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ₴", self.balance)
            insert_transaction('Withdrawal', amount, self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance : ₴", self.balance)


def main():
    create_table()
    user1 = Bank("James", 25, "Male")
    print("Welcome to the Banking App")
    while True:
        print("\n1. Balance")
        print("2.Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user1.view_balance()
        elif choice == 2:
            user1.deposits(int(input("Enter the amount to deposit: ")))
        elif choice == 3:
            user1.withdraw(int(input("Enter the amount to withdraw: ")))
        else:
            break


if __name__ == '__main__':
    main()
