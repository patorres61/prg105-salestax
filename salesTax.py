# Phyllis Torres
# Compute Sales Tax Program
# This program will total the sales amount input by the user and calculate the sales tax

# initialize the variables)
amount = 1
totalAmount = 0

# program title, describe the program and print instructions for the user
print ('                   Sales Tax Program\n\n')
# Instructions for the user
print("Input your sales amounts.")
print ("\nAfter entering all of your purchases, enter 0 to get your sales total, sales tax, and grand total.\n")

# this code will continue to loop until the user enters the value 0
while amount != 0:
    strCost = raw_input("Please enter the amount of your item: ")
    # the raw input is moved to the variable cost after changed from string type
    amount = float(strCost)
    # the following code accumulates all costs into the total variable
    totalAmount += amount
else:
    # when the user enters 0, the total will appear on screen
    print ("\nYour sales total is $" + '%.2f' % totalAmount)

# compute and print sales tax
salesTax = (totalAmount * .06)
print("\nYour sales tax is $" + str(round(salesTax, 2)))

# compute and print grand total
grandTotal = salesTax + totalAmount
print("\nYour grand total with the sales tax is: $" + str(round(grandTotal, 2)))

