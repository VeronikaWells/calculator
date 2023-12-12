import math
# This is my program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

# First, there is a greeting message, then the user chooses what he would like to use either "investment" or "bond" calculator using the input.

greeting1 = "Hello! Welcome to your fantastic financial calculator!"
greeting2 = "Please choose the calculator you would like to access. There are 2 options: "
greeting3 = "   Investment - to calculate the amount of interest you'll earn on your investment"
greeting4 = "   Bond - to calculate the amount you'll have to pay on a home loan"
print(greeting1)
print(greeting2)
print(greeting3)
print(greeting4)
option = input("Please enter either 'investment' or 'bond' here to proceed: ").lower()

# Then here is the code for the investment calculator using if statements and extra user input.

if option == 'investment':
    principal = float(input("Enter the amount of money being deposited: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years for investment: "))
    interest = input("Please choose either 'simple' or 'compound' interest: ").lower()

# Now implement the math formulas to calculate either simple or compound interest using if-elif-else statements.

    if interest == 'simple':
        amount = principal * (1 + (rate/100)  * years)
    elif interest == 'compound':
        amount = principal * math.pow(1 + rate / 100, years)
    else:
        print("Invalid interest type entered. Please enter either 'simple' or 'compound.'")

    if interest == 'simple' or interest == 'compound':
        print(f"The total amount after {years} years will be: {amount:.2f}. Thank you for using our calculator!")

# There is the code for the bond calculator using if-elif-else statements and extra user input.

elif option == 'bond':
    value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    num_months = int(input("Enter the number of months they plan to take to repay the bond: "))

# Implement the  math formula to calculate the repayment.

    monthly_payment = ((interest_rate / 100)/ 12 * value) / (1 - (1 + (interest_rate / 100)/ 12) ** -num_months)
    print(f"The monthly repayment amount will be: {monthly_payment:.2f}. Thank you for using our calculator!")