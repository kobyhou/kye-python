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
    dosage = int(input("How many times have you given your child paracetomal today?: "))
    if dosage <= 3:
        print("Okay, remember the limit is 4!")
    elif dosage == 4:
        print("No more is recommended.")
    else:
        print("Call 111 for your child, they've had too much.")
