class BankAccount:
    # don't forget to add some default values for these parameters!
    
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate=int_rate
        self.balance=balance

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    
    
    
    def deposit(self, amount):
        # your code here
        self.balance=self.balance +amount
        return self
    
    
    def withdraw(self, amount):
        # your code here
        if self.balance<amount and self.balance>5 :
            print ("Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-5
        else :
            self.balance=self.balance- amount
        return self    
    
    
    def display_account_info(self):
        # your code here

        print(f"Balance :${self.balance}") 
        return self

    
    def yield_interest(self):
        # your code here
        if self.balance>0 :
            self.balance=self.balance + (self.balance*self.int_rate)
        return self


AlexUser=BankAccount(0.2,250)
SmithUser=BankAccount(0.1,150)
AlexUser.deposit(150).deposit(80).deposit(280).withdraw(300).yield_interest().display_account_info()
SmithUser.deposit(650).deposit(520).withdraw(100).withdraw(50).withdraw(200).withdraw(150).yield_interest().display_account_info()
