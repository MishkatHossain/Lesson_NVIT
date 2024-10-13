# Encapsulation

# Public: Accessible from anywhere.
# A public attribute or method has no underscore prefix.


# Protected: Accessible within the class & its subclasses.
# A protected attribute or method has a single underscore prefix (_).

# Private: Accessible only within the class.
# A private attribute or method has a double underscore prefix (__).

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute (data hiding)

    # Getter method to access the private balance attribute
    def get_balance(self):
        return self.__balance

    # Setter method to modify the private balance attribute
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Amount cannot be negative")

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)    
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Private method
    def __update_balance(self, amount):
        self.__balance += amount

# Creating an object of BankAccount class
mishkat_account = BankAccount("Mishkat", 1000)

# Accessing public attribute
print(mishkat_account.account_holder)  # Output: Alice

# Accessing private attribute directly (Not allowed - will raise an AttributeError)
# print(account.__balance)  # Uncommenting this line would raise an error

# Using getter method to access the private attribute
print(mishkat_account.get_balance())  # Output: 1000

# Using setter method to modify the private attribute
mishkat_account.set_balance(1500)
print(mishkat_account.get_balance())  # Output: 1500

# Using public method to modify the private balance
mishkat_account.deposit(500)  # Output: $500 deposited. New balance: $2000

# Trying to access private method directly (Not allowed)
# account.__update_balance(100)  # Uncommenting this line would raise an error



muntasir_acc = BankAccount("Muntasir Hoque", 500)
print(muntasir_acc.account_holder)
print(muntasir_acc.get_balance())

muntasir_acc.set_balance(700)
print(muntasir_acc.get_balance())
muntasir_acc.set_balance(300)
print(muntasir_acc.get_balance())

muntasir_acc.deposit(1000)
muntasir_acc.deposit(1000)
muntasir_acc.deposit(1000)
