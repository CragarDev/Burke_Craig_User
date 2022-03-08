
# * Craig Burke - Assignment: User

""" 
 Practice creating a class and making instances from it
 Practice accessing the methods and attributes of different instances
If you've been following along, you're going to utilize the User class we've been discussing for this assignment.
For this assignment, we'll add some functionality to the User class:
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150
BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's
balance by the amount and add that amount to other other_user's balance
"""

# // 1. Create a file with the User class, including the __init__ and make_deposit methods
# // 2. Add a make_withdrawal method to the User class
# // 3. Add a display_user_balance method to the User class
# //  8. BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances


class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(
            f"{self.name}, Your deposit of {amount} has been accepted,\nYour balance is {self.account_balance}.\nThank You!")
        print("")

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(
            f"{self.name}, Your withdrawal of {amount} has been accepted,\nYour balance is {self.account_balance}.\nThank You!")
        print("")

    def display_user_balance(self):
        print(
            f"{self.name}, Your balance is: {self.account_balance}.\nThank You!")
        print("")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(
            f"{self.name}, the transfer to {other_user.name}\nfor the amount of {amount}, has been processed.\nThank You!")
        print("")


""" 
#// 1. Create a file with the User class, including the __init__ and make_deposit methods
#// 2. Add a make_withdrawal method to the User class
#// 3. Add a display_user_balance method to the User class
#// 4. Create 3 instances of the User class
#// 5. Have the first user make 3 deposits and 1 withdrawal and then display their balance
#// 6. Have the second user make 2 deposits and 2 withdrawals and then display their balance
#// 7. Have the third user make 1 deposits and 3 withdrawals and then display their balance
#// 8. BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

"""


# // 4. Create 3 instances of the User class
jbgoode = User("Johnny B Goode", "jbgoode@berrymail.com", 24)
guido = User("Guido van Rossum", "guido@python.com", 36)
monty = User("Monty Python", "monty@python.com", 42)

# // 5. Have the first user make 3 deposits and 1 withdrawal and then display their balance
jbgoode.make_deposit(600)
jbgoode.make_deposit(100)
jbgoode.make_deposit(70)
jbgoode.make_withdrawal(200)
jbgoode.display_user_balance()

# // 6. Have the second user make 2 deposits and 2 withdrawals and then display their balance
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_withdrawal(37)
guido.make_withdrawal(125)
guido.display_user_balance()

# // 7. Have the third user make 1 deposits and 3 withdrawals and then display their balance
monty.make_deposit(400)
monty.make_withdrawal(20)
monty.make_withdrawal(153)
monty.make_withdrawal(67)
monty.display_user_balance()

# // 8. BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
jbgoode.transfer_money(monty, 80)
jbgoode.display_user_balance()
monty.display_user_balance()


#  Playing.............

# #  print out the different attributes of the class/Object for each user
# print(guido.name)
# print(jbgoode.name)
# print(jbgoode.email)
# print(jbgoode.age)
# print(jbgoode.bank_name)
# print(jbgoode.account_balance)
# print("")

# print(guido.bank_name)
# print(jbgoode.bank_name)


# # Changing them in the entire class after changing in the instance ??? not working??
# User.bank_name = "Bank of Dojo"
# print(guido.bank_name)
# print(jbgoode.bank_name)
# print("")

# print(guido.name)
# print(monty.name)
# print(guido.email)
# print(monty.email)
# print(guido.age)
# print(monty.age)
# print(guido.account_balance)
# print(monty.account_balance)
# print(guido.bank_name)
# print(monty.bank_name)
# monty.make_deposit(100)
# monty.make_deposit(300)
# monty.make_deposit(400)
# monty.make_deposit(50)
# jbgoode.make_deposit(600)
# jbgoode.make_deposit(100)
# jbgoode.make_deposit(70)
# guido.make_deposit(700)
# guido.make_deposit(200)
# guido.make_deposit(100)
# monty.display_user_balance()
# guido.display_user_balance()
# jbgoode.display_user_balance()
# monty.make_withdrawal(65)
# monty.make_withdrawal(150)
# monty.make_withdrawal(20)
# jbgoode.make_withdrawal(200)
# jbgoode.make_withdrawal(50)
# jbgoode.make_withdrawal(300)
# guido.make_withdrawal(30)
# guido.make_withdrawal(301)
# guido.make_withdrawal(37)
# monty.display_user_balance()
# guido.display_user_balance()
# jbgoode.display_user_balance()
# monty.transfer_money(jbgoode, 65)
# jbgoode.display_user_balance()
# monty.display_user_balance()
