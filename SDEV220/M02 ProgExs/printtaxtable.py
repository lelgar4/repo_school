'''
    Richard Elgar
    SDEV220
    print a tax table
    Due:

     Listing 4.7 gives a program to compute tax. Write a function for computing tax using the following header: 
            >> def computeTax(status,taxableIncome):

    Use this function to write a program that prints a tax table for taxable taxableIncome from $50,000-$60,000, 
    in intervals of $100 for all four statuses
'''

#   function for assigning tax rate based on taxable taxableIncome and filing status
def computeTax(status,taxableIncome):
    if(status == 0):
        if(taxableIncome <= 8350):
            tax = taxableIncome * 0.10
        elif(taxableIncome <= 33950):
            tax = (8350 * 0.10) + ((taxableIncome - 8350) * 0.15)
        elif(taxableIncome <= 82250):
            tax = (8350 * 0.10) + ((33950 - 8350) * 0.15) + ((taxableIncome - 33950) * 0.25)

    elif(status == 1):
        if(taxableIncome <= 16700):
            tax = taxableIncome * 0.10
        elif(taxableIncome <=67900):
            tax = (16700 * 0.10) + ((taxableIncome - 16700) * 0.15)
        elif(taxableIncome <= 137050):
            tax = (16700 * 0.10) + ((67900 - 16700) * 0.15) + ((taxableIncome - 67900) * 0.25)

    elif(status == 2):
        if(taxableIncome <= 8350):
            tax = taxableIncome * 0.10
        elif(taxableIncome <= 33950):
            tax = (8350 * 0.10) + ((taxableIncome - 8350) * 0.15)
        elif(taxableIncome <= 68525):
            tax = (8350 * 0.10) + ((33950 - 8350) * 0.15) + ((taxableIncome - 33950) * 0.25)

    elif(status == 3):
        if(taxableIncome <= 11950):
            tax = taxableIncome * 0.10
        elif(taxableIncome <= 45500):
            tax = (11950 * 0.10) + ((taxableIncome - 11950) * 0.15)
        elif(taxableIncome <= 117450):
            tax = (11950 * 0.10) + ((45500 - 11950) * 0.15) + ((taxableIncome - 45500) * 0.25)

    return tax


#   Main func -- prints table of tax rates by taxable taxableIncome and filing status using computeTax()
def main():
    print("Taxable\t\tSingle\t\t\tMarried\t\t\tMarried\t\t\tHead of")
    print("Income\t\tFiler\t\t\tJointly\t\t\tSeparatly\t\tHousehold")
    print("----------------------------------------------------------------------------------------------------")
    for i in range(50000,60001,100):
       
        print(i,"\t\t",computeTax(0,i),"\t\t",computeTax(1,i),"\t\t",computeTax(2,i),"\t\t",computeTax(3,i))


#   call main()
main()

