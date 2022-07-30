# Register function
# Booking function- book and pay
# Delete account function

import pymysql.cursors

import dbconnection
def registervehicle():
    try:
        nameofowner = input("What is your Name?")
        idnumber = input("What is your ID Number?")
        phonenumber = input("What is your Phone Number +254?")
        residence = input("What is your residence?")
        cartype = input("What is your Car Type?")
        numberplate =input("What is your car numberplate?")
        modelname = input("What is your car modelname?")

        # sql
        sql = "insert into vehicle(nameofowner, idnumber, phonenumber, residence, cartype, numberplate, modelname) values (%s,%s,%s,%s,%s,%s,%s)"
        # Execute/run above sql.
        import pymysql
        connection = pymysql.connect(host="localhost", user="root", password="",
                                     database="tollbooth_db")
        cursor = connection.cursor()
        # execute sql using above cursor
        try:
           cursor.execute(sql, (nameofowner, idnumber, phonenumber, residence, cartype, numberplate, modelname))
           connection.commit()
           print("Saved Successfully")
           dbconnection.send_sms(phonenumber, "Thank you For Joining. Welcome")
        except:
           connection.rollback()
           print("Failed to Save")

    except Exception as error:
        print("oops! apologies try again later", error)

#registervehicle()

def booking():
    try:
        nameofcarowner = input("What is your Name?")
        numberplate = input("What is your car's numberplate?")
        phonenumber = input("What is your Phone Number +254?")
        distancefrom = input("Distance from?")
        destinationto = input("Destination to?")
        amount =input("Enter amount?")


        # sql
        sql = "insert into booking(nameofcarowner, numberplate, phonenumber, distancefrom, destinationto, amount) values (%s,%s,%s,%s,%s,%s)"
        # Execute/run above sql.
        import pymysql
        connection = pymysql.connect(host="localhost", user="root", password="",
                                     database="tollbooth_db")
        cursor = connection.cursor()
        # execute sql using above cursor
        try:
           cursor.execute(sql, (nameofcarowner, numberplate, phonenumber, distancefrom, destinationto, amount))
           connection.commit()
           print("Saved Successfully")
           dbconnection.send_sms(phonenumber, "Thank you For Joining. Welcome")
        except:
           connection.rollback()
           print("Failed to Save")

    except Exception as error:
        print("oops! apologies try again later", error)

#booking()


def deletevehicle(numberplate):
    sql = "delete from booking where numberplate = %s"
    connection = pymysql.connect(host="localhost", user="root", password="",
                                 database="tollbooth_db")
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
       cursor.execute(sql, (numberplate))
       connection.commit()
       print("Deleted Successfully")
    except:
       print("Not Deleted")


#deletevehicle('numberplate')
