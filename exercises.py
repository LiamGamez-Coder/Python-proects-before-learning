# NAME CHECKER


name = input("Enter a Name ")

if len(name) < 3:
    print("Name must be atleast 3 characters long")
elif len(name) > 50:
    print("Name can only be a maximum of 50 characters")
else:
    print("Name looks good!")


# WEIGHT CONVERTER


unit = input("Enter your unit of weight (abbreviation) ")
mg = float(input("Enter your weight in your unit "))

if unit == "kg":
    print("mg in pounds = ", (mg)*(2.5))
elif unit == "lb":
    print("mg in kilograms = ", (mg)/(2.5))
elif unit == "LT":
    print("mg in pounds", mg*2240)
elif unit == "tn":
    print("mg in pounds", mg*2000)
elif unit == "MT":
    print("mg in kilograms = ", mg*1000)
elif unit == "st":
    print("mg in pounds", mg*14)
else:
    print("Your weight has no unit, Your weight is", mg)


# CAR GAME


print("CAR GAME V1")
i = 0
while i == 0:

    command = input(">")

    if command.lower() == "help":
        print("start - to start the car"+"\n" +
              "stop - to stop the car"+"\n"+"quit - to exit")
    elif command.lower() == "start":
        print("Car started.... Ready to go!")
    elif command.lower() == "stop":
        print("Car stopped")
    elif command.lower() == "quit":
        break
    else:
        print("command unrecognised")
