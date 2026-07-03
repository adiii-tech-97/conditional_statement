print("if_elif_else_statement.py")


marks = int(input("enter your marks"))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 75:
    print("Grade C")
elif marks >= 65:
    print("Grade D")
else:
    print("Fail")


age = int(input("Enter your age"))
if age <= 18:
    print("child")
elif age <= 30:
    print("teenger")
elif age >= 50:
     print("adult")
elif age >= 70:
    print("senior citizen")


signal = input("Enter traffic signal (Red/Yellow/Green): ")
if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Get Ready")
elif signal == "Green":
    print("Go")
else:
    print("Invalid Traffic Signal")


amount = float(input("Enter purchase amount: "))
if amount >= 5000:
    print("Discount: 20%")
elif amount >= 3000:
    print("Discount: 15%")
elif amount >= 1000:
    print("Discount: 10%")
else:
    print("No Discount")


temp = float(input("enter daily temp"))
if temp <= 10.5:
    print("cold")
elif temp <= 15:
    print("worm")
elif temp <= 20:
    print("hot")
elif temp >= 30:
    print("very hot")
else:
    print("temp is temp")



amount = float(input("Enter total purchase amount "))
if amount >= 50000:
    print("Membership: Platinum")
elif amount >= 25000:
    print("Membership: Gold")
elif amount >= 10000:
    print("Membership: Silver")
else:
    print("Membership: Regular")


choice = int(input("Enter your choice (1-5)"))
if choice == 1:
    print("Profile Details Displayed.")
elif choice == 2:
    print("Your Account Balance is ₹25,000.")
elif choice == 3:
    print("Money Deposited Successfully.")
elif choice == 4:
    print("Money Withdrawn Successfully.")
elif choice == 5:
    print("Thank You! Visit Again.")
else:
    print("Invalid Choice!")
