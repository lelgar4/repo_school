'''
    Richard Elgar
    SDEV220
    The Account class
    due 14 Sep 21

Design a class named Accoutn that contains:
    -- private int id (account id)
    -- private float balance
    -- private float annualInterestRate
    -- a constructor with id,bal,and interest rate params (default vals 0,100,0)
    -- accessor and mutators for id,bal, and int rate
    -- method getMonthlyInterestRate() that returns monthly int rate
            >> monthlyIntRate = annIntRate / 12
    -- method getMonthlyInterest() returns monthly int AMOUNT
            >> formula:     bal * monthlyRate 
    -- methods withdraw(), deposit()
'''


class Account:

#   default constructor for instantiating account class objects. three class vars: id, balance, and annualInterestRate
    def __init__(self):
        self.__id = 0                         #  set class vars as private w/ __varName 
        self.__balance = 100                  #  set default vals for class vars
        self.__annualInterestRate = 0         # 


#   accessors and mutators for class vars
    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id
    
    def getBalance(self):
        return self.balance

    def setBalance(self,balance):
        self.balance = balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def setAnnualInterestRate(self,annualInterestRate):
        self.annualInterestRate = annualInterestRate


#   methods for monthly interest rate and amount
    def getMonthlyInterestRate(self):
        monthlyInterestRate = (self.annualInterestRate / 100) / 12
        return monthlyInterestRate

    def getMonthlyInterest(self):
        monthlyInterest = ((self.annualInterestRate / 100) / 12) * self.balance
        return monthlyInterest


#   methods for withdrawing and depositing 
    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
