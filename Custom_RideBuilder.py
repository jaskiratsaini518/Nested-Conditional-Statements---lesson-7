print("==============================")
print("   Welcome to Ride Builder!   ")
print("==============================")
print()

print("Step 1: Pick your vehicle")
print("1 - Bike")
print("2 - Car")
print()

choice = int(input("Enter 1 or 2: "))
print()
if choice == 1:
    print("Step 2: Pick your bike type")
    print("1 - Scooty")
    print("2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked   : Scooty")
        print("Top speed    : 80km/h")
        print("Best for     : City Roads")
    else:
        print("You picked   : Mountain Bike")
        print("Top speed    : 40km/h")
        print("Best for     : Off-Roading")

elif choice == 2:
    print("Step 2: Pick your car type")
    print("1 - Sedan")
    print("2 - SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("You picked   : Sedan")
        print("Seats        : 7 passengers")
        print("Best for     : Off-Road adventures")
else:
    print("That was not a valid choice.")
    print("Please enter 1 for bike and 2 for car.")

print()
print("================================")
print("   Your custom ride is ready!   ")
print("       Enjoy the journey!       ")
print("================================")