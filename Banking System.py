class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        if customer.id not in self.customers:
            self.customers[customer.id] = customer
            print(f"Customer {customer.name} added successfully.")
        else:
            print("Customer already exists with this ID.")

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print("Customer removed successfully.")
        else:
            print("Customer not found with this ID.")

    def display_all_customers(self):
        print("Customers:")
        for customer in self.customers.values():
            print(customer)
        print("")


class Customer:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal amount.")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Balance: {self.balance}"


# Example usage:
if __name__ == "__main__":
    bank = Bank("MyBank")

    customer1 = Customer(1001, "Alice", 5000)
    customer2 = Customer(1002, "Bob", 3000)
    customer3 = Customer(1003, "Charlie", 10000)

    bank.add_customer(customer1)
    bank.add_customer(customer2)
    bank.add_customer(customer3)

    bank.display_all_customers()

    customer1.deposit(1000)
    customer2.withdraw(500)
    customer3.withdraw(1500)

    bank.display_all_customers()

    bank.remove_customer(1002)

    bank.display_all_customers()
