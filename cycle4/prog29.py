class BankAccount:
    account_number_start = 102512
    instances = []
    def __init__(self,name, atype="savings"):
        self.name = name
        self.type = atype
        self.balance = 0
        self.account_number_start += 1
        self.account_number = self.account_number_start
        self.withdraw_limit = 20000 if atype == "Savings" else 50000
        self.instances.append(self)

    
    def withdraw(self, amount):
        if self.balance < amount:
            return print("Not enough balance! your balance is", self.balance)
        
        if self.atype == "Savings" and amount > self.withdraw_limit:
            return print("Sorry, the amount exceeds your withdraw limit")
        
        self.balance -= amount
        print(f"{amount} withdrawn. your balance is: {self.balance}") 

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. your balance is: {self.balance}")


def get_object():
    number = int(input("Enter your account number: "))
    obj = None
    for account in BankAccount.instances:
        if account.account_number == number:
            obj = account
    return obj



while True:
    choice = input("1. Create account\n2.Deposit\n3.Withdraw\n4.Exit\n")
    
    match choice:
        case "1":
            name = input("Enter your name: ")
            atype = input('Choose between: savings/current: ')
            obj = BankAccount(name, atype)
            print("Account created, your account number is", obj.account_number)
        
        case "2":
            account = get_object()
            if account:   
                amount = int(input("Enter the amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account number doesn't exist")
        case "3":
            account = get_object()
            if account:
                amount = int(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account number doesn't exist")

        case "4":
            exit()