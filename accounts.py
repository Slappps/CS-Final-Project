class Account:
    
    def __init__(self,name,balance=0):
        self.x = 1
        self.__account_name = name
        self.__account_balance = balance
        self.set_balance(self.__account_balance)
    
    def deposit(self,amount):
        
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount):
        
        if (amount <= self.__account_balance) and (amount > 0):
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        
        return self.__account_balance
    
    def get_name(self):
        
        return self.__account_name
    
    def set_balance(self,value):
        
        if value > 0:
            self.__account_balance = value
        else:
            self.__account_balance = 0
    
    def set_name(self,value):
        
        self.value = value
        self.__name = self.value
    
    def __str__(self):
        
        return f'Account name = {self.get_name()}, Account Balance = {self.get_balance():.2f}'



class SavingAccount(Account):
    
    MINIMUM = 0
    RATE = 0.02
    
    def __init__(self,name):
        
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count = 0
        
        
    def apply_interest(self):
        
        bal = super().get_balance()
        print(self.x)
        bal = bal + (bal * 0.02)
        
        self.set_balance(bal)
    
    def deposit(self,amount):
        
        if amount <= 0:
            return False
        else:
            self.__deposit_count += 1
            self.set_balance(super().get_balance() + amount)
            
            if self.__deposit_count >= 5:
                self.__deposit_count = 0
                self.apply_interest()
            
            return True
        
        
            
        
    def withdraw(self,amount):
        
        if amount <= 0 or (super().get_balance() - amount) < SavingAccount.MINIMUM:
            return False
        else:
            self.set_balance(super().get_balance()-amount)
            
            return True
        
    
    def set_balance(self,value):
        
        # dont go below 100
        if value >= 0:
            super().set_balance(value)
        else:
            super().set_balance(0)
        
    def __str__(self):
        
        return f'SAVINGS ACCOUNT: {super().__str__()}'
        