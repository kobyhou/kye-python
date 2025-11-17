def hospital():
    name=str(input("What is your name?: "))
    age=int(input("What is your age?: "))
    height=float(input("What is your height in (m)?: "))
    weight=float(input("What is your weight in (kg)?: "))
    bmi = float(weight) / (float(height) * float(height))
    if bmi > 30:
        print("You are overweight.")
    else:
        print("You are normal weight.")
    if age > 65:
        print("Old person discount applied.")
    print("The patient", name,"has a BMI of", bmi)
hospital()