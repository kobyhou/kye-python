def task1():
    test=str(input("What type of test is this? (e.g., glucose, cholesterol...): "))
    val=float(input("What is the current value?: "))
    unit=str(input("What unit is the value stored? (e.g., mg/dL, mmol/L...): "))
    if unit == "mg/dL":
        mmol = val / 18
        print("Your converted value is", mmol,"mmol/L.")
    elif unit == "mmol/L":
        mgdl = val * 18
        print("Your converted value is", mgdl,"mg/dL.")
    else:
        print("Went wrong somewhere.")

def task2():
    read1=float(input("What is the first temperature reading? (C): "))
    read2=float(input("What is the second temperature reading? (C): "))
    read3=float(input("What is the third temperature reading? (C): "))
    add = read1 + read2 + read3
    average = add / 3
    if average > 38:
        print("Your average temperature reading is over the threshold for a fever.")
    else:
        print("Couldn't calculate it.")
    rounding=average(round, 2)
    print("Your average temperature is", rounding,"celcius.")

def task3():
    age=int(input("What is your age?: "))
    resthr=int(input("What is your resting heart rate?: "))
    MAXIMUM = 220
    safehr = MAXIMUM - age
    if resthr > MAXIMUM:
        print("Having a resting heart rate anywhere near 220 is dangerous.")
    safe = resthr >= 60 and resthr <= 100
    if resthr <= 59:
        print("Your resting heart rate is too low.")
    elif resthr >= 101:
        print("Your resting heart rate is too high.")
    else:
        print("Your resting heart rate is safe.")
    print("Your heart rate should only ever go up to",safehr,"bpm.")
