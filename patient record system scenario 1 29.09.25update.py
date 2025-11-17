def function(record):
    name=str(input("What is the patient's name?: "))
    age=int(input("How old is the patient?: "))
    height=float(input("How tall is the patient? (m): "))
    print("-----------------")
    print("-PATIENT DETAILS-")
    print("Name -", name)
    print("Age -", age)
    print("Height -", height,"m")
    print("-----------------")

def function(EHR):

    kilo=float(input("What is your weight in kg?: "))
    height=float(input("What is your height in m?: "))
    sqr = float(height * height)
    rank = float(kilo / sqr)
    uw = rank <= 18.4
    nw = rank >= 18.5
    ow = rank >= 25
    o = rank >= 30
    eo = rank >= 35
    if rank <= 18.4:
        print("You are classed as underweight.")
    elif rank >= 18.5:
        print("You are normal weight.")
    elif rank >= 25:
        print("You are classed as overweight.")
    elif rank >= 30:
        print("You are classed as obese.")
    elif rank >= 35:
        print("You are extremely obese.")
    else:
        print("Could not calculate...")

def function(child):
    amount = int(input("At what amount in 'mg', are you giving your child each time?: "))
    dosage = int(input("How many times have you given your child paracetomal today?: "))
    if dosage <= 3:
        print("Okay, remember the limit is 4!")
    elif dosage == 4:
        print("No more is recommended.")
    else:
        print("Call 111 for your child, they've had too much.")

days = int(input("How many days did you stay?: "))
room = str(input("Did the patient stay in a luxury or ordinary room?: "))
priceL = (days * 500)
priceO = (days * 275)
treatment = str(input("Did you receive basic or urgent treatment within your stay?: "))
if treatment == "Urgent" or "urgent":
    treat1 = 150 * days 
elif treatment == "Basic" or "basic":
    treat2 = 100 * days
else:
    print("Please input 'Urgent' or 'Basic'.")
consult = str(input("Did you receive a consultation during your stay?: "))
if consult == "Yes" or "yes":
    last1 = 200
elif consult == "No" or "no":
    last2 = 0
else:
    print("Please input 'Yes' or 'No'.")
luxuryurgcons = priceL + treat1 + last1
luxurybascons = priceL + treat2 + last1
luxuryurgnocons = priceL + treat1 + last2
luxurybasnocons = priceL + treat2 + last2
ordinarybascons = priceO + treat2 + last1
ordinaryurgcons = priceO + treat1 + last1
ordinaryurgnocons = priceO + treat1 + last2
ordinarybasnocons = priceO + treat2 + last2
if room == "Luxury" or "luxury" and treatment == "Urgent" or "urgent" and consult == "Yes" or "yes":
    print("Your total without VAT is", luxuryurgcons,"pounds.")
if room == "Luxury" or "luxury" and treatment == "basic" or "Basic" and consult == "Yes" or "yes":
    print("Your total without VAT is", luxurybascons,"pounds.")    
if room == "Luxury" or "luxury" and treatment == "Urgent" or "urgent" and consult == "No" or "no":
    print("Your total without VAT is", luxuryurgnocons,"pounds.")
if room == "Luxury" or "luxury" and treatment == "Basic" or "basic" and consult == "no" or "No":
    print("Your total without VAT is", luxurybasnocons,"pounds.")
if room == "Ordinary" or "ordinary" and treatment == "Urgent" or "urgent" and consult == "Yes" or "yes":
    print("Your total without VAT is", ordinaryurgcons,"pounds.")
if room == "ordinary" or "Ordinary" and treatment == "Urgent" or "urgent" and consult == "No" or "no":
    print("Your total without VAT is", ordinaryurgnocons,"pounds.")
if room == "ordinary" or "Ordinary" and treatment == "Basic" or "basic" and consult == "No" or "no":
    print("Your total without VAT is", ordinarybasnocons,"pounds.")
if room == "ordinary" or "Ordinary" and treatment == "Basic" or "basic" and consult == "Yes" or "yes":
    print("Your total without VAT is", ordinarybascons,"pounds.")