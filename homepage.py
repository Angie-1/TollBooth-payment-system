print("E-TICKETING TOLL BOOTH SYSTEM")
def menu():
    text = "welcome to system \n " \
           "Please select a choice \n " \
           "1. Register your vehicle \n " \
           "2. Booking \n " \
           "3. Delete vehicle \n " \
           "4. Exit \n"

    print(text)

from functions import *
from dbconnection import *
def input_menu():
    while True:
        menu()
        str = input("enter your choice: ")
        if str == "1":
            registervehicle()
        elif str == "2":
            booking()
            mpesa_payment(input("Amount to pay"), input("Your tel 2547xxxxxxx"))
            print("Please check your phone and complete payment...")

        elif str == "3":
            deletevehicle(input('Enter your numberplate to delete: '))

        elif str == "4":
            print("Ended, Thank you")

        else:
            print("invalid Choice")



input_menu()