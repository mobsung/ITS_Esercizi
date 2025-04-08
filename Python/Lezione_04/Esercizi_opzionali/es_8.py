'''8. ATM Machine Simulator:

Create a function that simulates an ATM machine.
Initialize an account with a starting balance.
Allow the user to perform transactions such as deposit, withdraw, and check balance.
Validate transactions against the account balance and available funds.
Provide appropriate feedback to the user for each transaction.
'''


def setAccountBalance() -> float:

    starting_balance = float(input("Set starting balance:\n==>"))

    return starting_balance



def deposit(balance:float) -> float:

    deposit_amount:float = float(input("What amount would you like to deposit:\n==>"))
    balance += deposit_amount

    print(f"You deposited {deposit_amount} $ - Your total amount is now {balance} $\n")

    return balance


def withdraw(balance:float) -> float:
    
    withdraw_amount:float = float(input("What amount would you like to deposit:\n==>\n"))
    
    if balance - withdraw_amount < 0:
        print("You don't have enough money to withdraw\n")
    else:    
        balance -= withdraw_amount
        print(f"You withdrew {withdraw_amount} $ - Your total amount is now {balance} $\n")

    return balance


def checkBalance(balance:float):

    print(f"Your balance is: {balance} $\n")


def atm(choice:str = ""):
    
    balance:float = setAccountBalance()

    while choice != "finish":

        choice = input('Type "deposit" - to DEPOSIT money\n'
                       'Type "withdraw" - to WITHDRAW money\n'
                       'Type "check" - to CHECK the balance\n'
                       'Type "finish" - to STOP\n==>'
                      )
        choice.lower()

        if choice == "deposit":
            balance = deposit(balance)

        if choice == "withdraw":
            balance = withdraw(balance)

        if choice == "check":
            checkBalance(balance)
        

atm()