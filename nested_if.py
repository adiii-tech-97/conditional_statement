print("nested_if")

attendance = (input("Enter your attendance percentage"))
fees_paid = input(" paid exam fees? (yes/no): ")

if attendance >= 75:
    if fees_paid.lower() == "yes":
        print("You are eligible for the exam.")
    else:
        print("You are not eligible your exam fees not paid.")
else:
    print("You are not eligible your attendance is under 75%.")

username = input("enter your username")
password = input("enter your password")
if username == "admin":
    if password == "9354":
        print("login succesful.")
    else:
        print("invalid pssword.")
else:
    print("invalid username.")


    marks = float(input("Enter your marks "))
    documents = input("documents verified? (yes/no)")
    if marks >= 60:
        if documents.lower() == "yes":
            print("Your admission is confirmed.")
        else:
            print("document not verified.")
    else:
        print("not eligible for admission your percentage is under 60%.")


product_available = input("product available? (yes/no): ")
payment_status = input("payment successful? (yes/no): ")

if product_available.lower() == "yes":
    if payment_status.lower() == "yes":
        print("Your order placed successfully.")
    else:
        print("Your order not placed payment failed.")
else:
    print("product is out of stock.")


    patient_registered = input("patient registered? (yes/no): ")
doctor_available = input("doctor available? (yes/no): ")

if patient_registered.lower() == "yes":
    if doctor_available.lower() == "yes":
        print("Appointment confirmed.visit hospital your scheduled time.")
    else:
        print("doctor not available.")
else:
    print("register the patient booking an appointment.")


attendance = 80
fees_paid = "yes"

if attendance >= 75:
    if fees_paid == "yes":
        print("Eligible for Exam")


username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")