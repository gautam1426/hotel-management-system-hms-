# *************** Govt Model Senior Secondary School **********************
# ##*************** HOTEL MANAGEMENT SYSTEM **************************
# ################## HOTEL GAUTAM #############################

import mysql.connector

# GLOBAL VARIABLES DECLARATION
myConnection = ""
cursor = ""
userName = "root"
password = "14261426"
roomrent = 0
restaurentbill = 0
gamingbill = 0
fashionbill = 0
totalAmount = 0
cid = ""

# MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck():
    global myConnection, userName, password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME: ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD: ")
    myConnection = mysql.connector.connect(
        host="localhost", user=userName, passwd=password, auth_plugin='mysql_native_password'
    )
    if myConnection:
        print("\n CONGRATULATIONS! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED!")
        cursor = myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD!")

# MODULE TO ESTABLISH MYSQL CONNECTION
def MYSQLconnection():
    global userName, password, myConnection, cid
    myConnection = mysql.connector.connect(
        host="localhost", user=userName, passwd=password, database="HMS", auth_plugin='mysql_native_password'
    )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION!")
        myConnection.close()

def userEntry():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        createTable = """CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20), C_NAME VARCHAR(30), 
                         C_ADDRESS VARCHAR(30), C_AGE VARCHAR(30), C_COUNTRY VARCHAR(30), 
                         P_NO VARCHAR(30), C_EMAIL VARCHAR(30))"""
        cursor.execute(createTable)
        cid = input("Enter Customer Identification Number : ")
        name = input("Enter Customer Name : ")
        address = input("Enter Customer Address : ")
        age = input("Enter Customer Age : ")
        nationality = input("Enter Customer Country : ")
        phoneno = input("Enter Customer Contact Number : ")
        email = input("Enter Customer Email : ")
        sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (cid, name, address, age, nationality, phoneno, email)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        print("\nNew Customer Entered In The System Successfully !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def searchCustomer():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        cid = input("ENTER CUSTOMER ID : ")
        sql = "SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql, (cid,))
        data = cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print("Record Not Found Try Again !")
            return False
        cursor.close()
    else:
        print("\nSomething Went Wrong, Please Try Again !")

def bookingRecord():
    global cid
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = "CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20), CHECK_IN DATE, CHECK_OUT DATE)"
            cursor.execute(createTable)
            checkin = input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
            checkout = input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
            sql = "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
            values = (cid, checkin, checkout)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("\nCHECK-IN AND CHECK-OUT ENTRY MADE SUCCESSFULLY !")
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def roomRent():
    global cid, roomrent
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20), ROOM_CHOICE INT, 
                             NO_OF_DAYS INT, ROOMNO INT, ROOMRENT INT)"""
            cursor.execute(createTable)
            print("\n ##### We have The Following Rooms For You #####")
            print(" 1. Ultra Royal ----> 10000 Rs.")
            print(" 2. Royal ----> 5000 Rs. ")
            print(" 3. Elite ----> 3500 Rs. ")
            print(" 4. Budget ----> 2500 Rs. ")
            roomchoice = int(input("Enter Your Option : "))
            roomno = int(input("Enter Customer Room No : "))
            noofdays = int(input("Enter No. Of Days : "))
            if roomchoice == 1:
                roomrent = noofdays * 10000
            elif roomchoice == 2:
                roomrent = noofdays * 5000
            elif roomchoice == 3:
                roomrent = noofdays * 3500
            elif roomchoice == 4:
                roomrent = noofdays * 2500
            else:
                print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql = "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
            values = (cid, roomchoice, noofdays, roomno, roomrent)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("Thank You, Your Room Has Been Booked For : ", noofdays, "Days")
            print("Your Total Room Rent is : Rs. ", roomrent)
            cursor.close()

def Restaurent():
    global cid, restaurentbill
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS RESTAURENT(CID VARCHAR(20), CUISINE VARCHAR(30), 
                             QUANTITY VARCHAR(30), BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("1. Vegetarian Combo -----> 300 Rs.")
            print("2. Non-Vegetarian Combo -----> 500 Rs.")
            print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
            choice_dish = int(input("Enter Your Cuisine : "))
            quantity = int(input("Enter Quantity : "))
            if choice_dish == 1:
                restaurentbill = quantity * 300
            elif choice_dish == 2:
                restaurentbill = quantity * 500
            elif choice_dish == 3:
                restaurentbill = quantity * 750
            else:
                print("Wrong Input, Please Try Again !!!")
                return
            sql = "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s)"
            values = (cid, choice_dish, quantity, restaurentbill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("Your Total Bill Amount Is : Rs. ", restaurentbill)
            cursor.close()

def Gaming():
    global cid, gamingbill
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20), GAMES VARCHAR(30), 
                             HOURS VARCHAR(30), GAMING_BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("1. Table Tennis (150/hr)\n2. Bowling (100/hr)\n3. Snooker (250/hr)\n4. VR World (400/hr)\n5. Video Games (300/hr)\n6. Swimming (350/hr)")
            game = int(input("Enter Game Choice : "))
            hour = int(input("Enter Hours : "))
            rates = {1: 150, 2: 100, 3: 250, 4: 400, 5: 300, 6: 350}
            if game in rates:
                gamingbill = hour * rates[game]
            else:
                return
            sql = "INSERT INTO GAMING VALUES(%s,%s,%s,%s)"
            values = (cid, game, hour, gamingbill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("Total Gaming Bill: Rs. ", gamingbill)
            cursor.close()

def Fashion():
    global cid, fashionbill
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS FASHION(CID VARCHAR(20), DRESS VARCHAR(30), 
                             AMOUNT VARCHAR(30), BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("1. Shirts (1500)\n2. T-Shirts (300)\n3. Pants (2000)\n4. Jeans (4000)...")
            dress = int(input("Enter Choice : "))
            quantity = int(input("Quantity : "))
            # Logic for prices (1500, 300, 2000, 4000, 500, 3000, 3000, 400, 200, 30)
            prices = {1:1500, 2:300, 3:2000, 4:4000, 5:500, 6:3000, 7:3000, 8:400, 9:200, 10:30}
            fashionbill = quantity * prices.get(dress, 0)
            sql = "INSERT INTO FASHION VALUES(%s,%s,%s,%s)"
            values = (cid, dress, quantity, fashionbill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("Total Fashion Bill: ", fashionbill)
            cursor.close()

def totalAmount():
    global cid, roomrent, restaurentbill, fashionbill, gamingbill
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20), C_NAME VARCHAR(30), 
                             ROOMRENT INT, RESTAURENTBILL INT, GAMINGBILL INT, FASHIONBILL INT, TOTALAMOUNT INT)"""
            cursor.execute(createTable)
            name = input("Enter Customer Name : ")
            grandTotal = roomrent + restaurentbill + fashionbill + gamingbill
            values = (cid, name, roomrent, restaurentbill, gamingbill, fashionbill, grandTotal)
            cursor.execute("INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)", values)
            cursor.execute("COMMIT")
            print("\n **** TOTAL AMOUNT : Rs. ", grandTotal)
            cursor.close()

def searchOldBill():
    global cid
    customer = searchCustomer()
    if customer and myConnection:
        cursor = myConnection.cursor()
        cursor.execute("SELECT * FROM TOTAL WHERE CID= %s", (cid,))
        data = cursor.fetchall()
        print(data if data else "Record Not Found !")
        cursor.close()

# MAIN PROGRAM FLOW
myConnection = MYSQLconnectionCheck()
if myConnection:
    MYSQLconnection()
    while True:
        print("\n1. Customer Details  2. Booking Record  3. Room Rent  4. Restaurant  5. Gaming  6. Fashion  7. Search  8. Total Bill  9. Old Bill  10. EXIT")
        choice = int(input("Enter Choice: "))
        if choice == 1: userEntry()
        elif choice == 2: bookingRecord()
        elif choice == 3: roomRent()
        elif choice == 4: Restaurent()
        elif choice == 5: Gaming()
        elif choice == 6: Fashion()
        elif choice == 7: searchCustomer()
        elif choice == 8: totalAmount()
        elif choice == 9: searchOldBill()
        elif choice == 10: break