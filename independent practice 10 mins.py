def rectangle():
    length=float(input("What is the length of the rectangle?(m): "))
    width=float(input("What is the width of the rectangle?(m): "))
    area = float(length) * float(width)
    print("The area of the rectangle is",area,"m.")

def conversion():
    minutes=int(input("How many minutes are you converting?: "))
    hours = minutes // 60
    leftover = minutes % 60
    print(hours)
    print(leftover)


