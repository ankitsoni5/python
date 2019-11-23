from com.ankit.banking.account import Account
from com.ankit.banking.overdrafterror import Over_draft_error
from traceback import print_exc

a = Account(acc_name='Ankit', acc_type='Saving', acc_balance=10000)
try:
    ab = a.withdraw(500)
except Over_draft_error:
    print_exc() # It will the complete error traceback
except ValueError:
    print_exc()
else:
    print(ab)
'''
try:
    ab = a.withdraw(-9500)
except Exception:
    print_exc()
else:
    print(ab)
''' # please avoid it.