from .overdrafterror import Over_draft_error

class Account:
    min_balance = 1000

    def __init__(self,acc_name, acc_type, acc_balance):
        self.acc_name =acc_name
        self.acc_tpye = acc_type
        self.acc_balance = acc_balance
    
    def withdraw(self, amt):
        print('Transaction Starts.')
        try:
            if self.acc_balance - amt < Account.min_balance:
                raise Over_draft_error('Account balance going below {0}'.format(Account.min_balance))
        
            if amt <= 0:
                raise ValueError('The Entered Amount is negative. Please enter the correct amount.')
            
            self.acc_balance -= amt
            return self.acc_balance
        finally:
            # Statements will execute irrective of what is happened in try block
            # 1. Even if you get any error
            # 2. Even if everything goes fine.
            print('Transaction ends.')