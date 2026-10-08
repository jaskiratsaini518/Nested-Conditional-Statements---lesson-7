print("==============================")
print("   Welcome to Holiday Planner!   ")
print("==============================")
print()

print("Step 1: Pick your holiday")
print("1 - Christmas")
print("2 - Halloween")
print()

choice = int(input("Enter 1 or 2: "))
print()
if choice == 1:
    print("Step 2: Pick your Christmas activity")
    print("1 - Decorating")
    print("2 - Baking")
    print()

    christmas_activity = int(input("Enter 1 or 2: "))
    print()

    if christmas_activity == 1:
        print("You picked   : Decorating")
        print("Best time    : Evening")
        print("Best for     : Family Fun")
    else:
        print("You picked   : Baking")
        print("Best time    : Afternoon")
        print("Best for     : Making Treats")

elif choice == 2:
    print("Step 2: Pick your Halloween activity")
    print("1 - Costume Party")
    print("2 - Pumpkin Carving")
    print()

    halloween_activity = int(input("Enter 1 or 2: "))
    print()

    if halloween_activity == 1:
        print("You picked   : Costume Party")
        print("Best for     : Friends")
        print("Best time    : Evening")
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Christmas and 2 for Halloween.")

print()
print("================================")
print("   Your holiday plan is ready!   ")
print("       Enjoy the celebration!       ")
print("================================")