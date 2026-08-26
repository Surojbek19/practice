print("==== ENCAPSUALTION ====")
'''
Encapsualtions means keeping the data and methods that works with that datainside a class, 
while controlling how the data can be accessed or modified from outside  
'''
# C++, JAVA > public, private, protected
# Python > name(public), __name(private), _name(protected)


class Account():
    # state
    description = "The class makes bank accounts!"

    # constructure
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} usd!")

    def deposite(self, amount):
        print("Deposite:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("Withdraw:", amount)
        self.__amount -= amount

    # This decorater lets us use tis holder method as a state. This also called "getter"
    @property
    def holder(self):
        return self.__owner

    # This is "setter" that works with "getter", and we can use it as a state
    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    # This is ordinary way of changing the private state, but we could do it with "setter"
    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("*******")
my_account.deposite(5000)
my_account.withdraw(2500)
my_account.get_balance()

print("*******")

try:
    result = my_account.amount
    print("Result:", result)
except Exception as err:
    print("No target state founs:", err)


account_owner = my_account.holder
print("owner before:", account_owner)

# my_account.change_ownership("Michael") # This was for ordinary way

my_account.holder = "Michael"  # This is how "setter" works
print("owner after:", my_account.holder)
