'''
    Richard Elgar
    SDEV220

    due 14 Sep 21


    -- Also change the account ID to 3345 and a balance of $35,000
'''

from account import Account

def main():
    testAccount = Account()
    testAccount.setId(3345)
    testAccount.setBalance(35000)
    testAccount.setAnnualInterestRate(4.5)

    testAccount.withdraw(2500)
    print("id: ", testAccount.getId(),"\nbalance: ",testAccount.getBalance(),"\nmonthly interest rate: ",testAccount.getMonthlyInterestRate(),"\nmonthly interest amount: ",testAccount.getMonthlyInterest())

    testAccount.deposit(3000)
    print("id: ", testAccount.getId(),"\nbalance: ",testAccount.getBalance(),"\nmonthly interest rate: ",testAccount.getMonthlyInterestRate(),"\nmonthly interest amount: ",testAccount.getMonthlyInterest())


#   call main()
main()