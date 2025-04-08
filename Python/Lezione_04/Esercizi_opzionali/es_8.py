'''8. ATM Machine Simulator:

Create a function that simulates an ATM machine.
Initialize an account with a starting balance.
Allow the user to perform transactions such as deposit, withdraw, and check balance.
Validate transactions against the account balance and available funds.
Provide appropriate feedback to the user for each transaction.
'''




def is_float(value) -> bool:
    try:
        if float(value) > 0:  # Try to convert the string to a float
            return True   # If successful, it's a float
    except ValueError:
        return False  # If conversion fails, it's not a float


def setAccountBalance(starting_balance:str = "") -> float:

    while not is_float(starting_balance):
        starting_balance = input("Set starting balance:\n==>")
        if not is_float(starting_balance):
            print("The balance should be a positive number\n")

    return float(starting_balance)



def deposit(balance:float, deposit_amount:str = "") -> float:

    while not is_float(deposit_amount):
        deposit_amount = input("What amount would you like to deposit:\n==>")
        if not is_float(deposit_amount):
            print("The balance should be a positive number\n")

    balance += float(deposit_amount)

    print(f"You deposited {deposit_amount} $ - Your total amount is now {balance} $\n")

    return balance


def withdraw(balance:float, withdraw_amount:str = "") -> float:
    
    while not is_float(withdraw_amount):
        withdraw_amount = input("What amount would you like to withdraw:\n==>")
        if not is_float(withdraw_amount):
            print("The balance should be a positive number\n")

    if balance - float(withdraw_amount) < 0:
        print("You don't have enough money to withdraw\n")
    else:    
        balance -= float(withdraw_amount)
        print(f"You withdrew {withdraw_amount} $ - Your total amount is now {balance} $\n")

    return balance


def checkBalance(balance:float):

    print(f"Your balance is: {balance} $\n")


def atm(choice:str = ""):
    
    balance:float = setAccountBalance()

    while choice.lower() != "finish":

        choice = input('Type "deposit" - to DEPOSIT money\n'
                       'Type "withdraw" - to WITHDRAW money\n'
                       'Type "check" - to CHECK the balance\n'
                       'Type "finish" - to STOP\n==>'
                      )

        if choice.lower() == "deposit":
            balance = deposit(balance)

        if choice.lower() == "withdraw":
            balance = withdraw(balance)

        if choice.lower() == "check":
            checkBalance(balance)
        

atm()