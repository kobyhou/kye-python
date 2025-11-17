print("Before starting we need your patient details...")
name=str(input("What is the patient's name?: "))
age=int(input("What is your age?: "))
sex=str(input("Are you male or female?: "))
height=float(input("What is your height in (m)?: "))
weight=float(input("What is your weight in (kg)?: "))
bmi = float(weight) / (float(height) * float(height))
roundedBMI=round(bmi, 2)
print("So far, your name is",name,", you are",age,"years old, a",sex,",",height,"metres tall and weigh",weight,"kilos.")
correct=str(input("Are all these details correct (yes/no)?: "))
if correct == "Yes" or "yes":
    print("Your BMI score is",roundedBMI,)
    med=str(input("Have you taken the right amount of medicine for today?: "))
    if med == "yes" or "Yes":
        print("Perfect!")
    else:
        print("It is dangerous to not take your medicine.")
else:
    print("You will have to restart this process, something went wrong...")