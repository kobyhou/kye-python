#asks for patient's name, age and total bill amount
name=str(input("What is the patient's name?: "))
age=int(input("What is the patient's age?: "))
billAmount=float(input("What is the bill cost?:"))
#applies VAT to bill
afterTax=float(billAmount) * 1.2
#checks for discount
if age < 18:
    discount = afterTax * 0.35
    print("You are eligible for discount.")
    print("Your total after tax is", discount,"pounds.")
else:
    print("You are not eligible for discount.")
    print("Your total is",afterTax,"pounds including tax.")
#lets user know they have payment plan options
if afterTax or discount > 1000:
    print("We have payment plan options set up for you to handle the bill.")