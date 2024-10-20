import customer
import owner
import dbase as db

db.initiate()


def menu(sm_name):
    try:
        choice1 = int(input("Choose who you are?\n1. Customer\n2. Owner\nEnter choice:"))
    except ValueError:
        print("->Invalid value. Enter the number corresponding to the option you want to choose!")
        menu(sm_name)
