import mysql.connector as CON
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return CON.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))

def login(uid,uname,pwd):
    try:
        CN=get_connection()
        CUR=CN.cursor()
        CUR.execute("select * from users where UserID={} and UserName='{}' and Password='{}'".format(uid,uname,pwd))
        user=CUR.fetchone()
        CN.commit()
        CN.close()
        return user
    except ValueError:
        print('Invalid input given.')
    except TypeError:
        print("invalid data type")


def signin(uname,pwd,work):
    try:
        CN=get_connection()
        CUR=CN.cursor()
        CUR.execute("insert into users(UserName, Password, Work) values (%s,%s,%s)",(uname,pwd,work))
        user_id = CUR.lastrowid
        CN.commit()
        CN.close()
        return user_id
    except ValueError:
        print('Invalid input given.')
    except TypeError:
        print("invalid data type")
    
    
def room_details():
    try:
        get_connection()
        CUR=CN.cursor() 
        CUR.execute('select * from rooms') 
        E=CUR.fetchall() 
        CN.close()
        return E
    except ValueError:
        print('Invalid input given.')
    except TypeError:
        print("invalid data type")

def room_booking(RoomNo, U_Id, U_Name, Address, PhoneNo, InDate, OutDate, Gender):
    try:
        CN=get_connection()
        CUR=CN.cursor()
        CUR.execute("INSERT INTO room_booking(RoomNo, U_Id, U_Name, Address, PhoneNo, InDate, OutDate, Gender)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(RoomNo, U_Id, U_Name, Address, PhoneNo, InDate, OutDate, Gender))
        B_Id=CUR.lastrowid
        CUR.execute("UPDATE rooms SET Status='{}' WHERE RoomNo={}".format('Occupied', RoomNo))
        CN.commit()
        CN.close()
        return B_Id
    except Exception as e:
        print("room_booking:", e)
        return False

def remove_room_booking(room_no):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("DELETE FROM room_booking WHERE RoomNo=%s",(room_no,))
        CUR.execute("UPDATE rooms SET Status='Available' WHERE RoomNo=%s",(room_no,))

        CN.commit()
        CN.close()

        return True

    except Exception as e:
        print("remove_room_booking:", e)
        return False
    
def table_booking_details():
    CN=get_connection()
    CUR = CN.cursor()
    CUR.execute("SELECT * FROM tables")
    result = CUR.fetchall()
    CN.close()
    return result

def remove_table_booking(table_no):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("UPDATE tables SET Status='Available' WHERE TableNo=%s",(table_no,))
        CN.commit()
        CN.close()
        return True

    except Exception as e:
        print("remove_table_booking:",e)
        return False
    
def menu():
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("SELECT * FROM menu")
        data = CUR.fetchall()
        CN.close()
        return data
    except Exception as e:
        print("menu error:", e)
        return []

def create_order(user_id):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        total=0
        CUR.execute("INSERT INTO order_info(User_ID, Total) VALUES (%s, %s)",(user_id, total))
        order_no = CUR.lastrowid
        CN.commit()
        CN.close()
        return order_no
    except Exception as e:
        print("order error:",e)
        return False

def remove_order(order_no):
    try:
        CN=get_connection()
        CUR = CN.cursor()

        CUR.execute("DELETE FROM order_details WHERE Order_No=%s",(order_no,))
        CUR.execute("DELETE FROM order_info WHERE Order_No=%s",(order_no,))
        success = CUR.rowcount > 0
        CN.commit()
        CN.close()

        return success

    except Exception as e:
        print("remove_order:", e)
        return False
def add_item(order_no, item_no, qty):
    CN=get_connection()
    CUR = CN.cursor()
    CUR.execute("SELECT Price FROM menu WHERE I_No=%s",(item_no,))
    
    price = CUR.fetchone()
    if not price:
        CN.close()
        return False
    total = price[0] * qty
    
    CUR.execute("INSERT INTO order_details(Order_No, Item_No, Qty, Total) VALUES(%s,%s,%s,%s)",(order_no, item_no, qty, total))
    CUR.execute("UPDATE order_info SET Total = Total + %s WHERE Order_No=%s",(total, order_no))

    CN.commit()
    CN.close()

    return True
    
def add_dish(iname,price,category,vorn):
    try:
        CN=get_connection()
        CUR=CN.cursor()
        CUR.execute("insert into menu(I_Name,Price,Category,VorN) values('{}',{},'{}','{}')".format(iname,price,category,vorn)) 
              
        CN.commit()
        CN.close()
        return True

    except Exception as e:
        print("add dish error:", e)
        return False 

#remove_dish 
def remove_dish(ino):
    try:
        CN=get_connection()
        CUR=CN.cursor()  
        CUR.execute("delete from menu where I_No ={}".format(ino)) 
        CN.commit()
        CN.close()
        return True

    except Exception as e:
        print("remove dish error:", e)
        return False

def update_dish(ino,iname,price,category,vorn):
    try:
        CN=get_connection()
        CUR = CN.cursor()

        CUR.execute("UPDATE menu SET I_Name=%s, Price=%s, Category=%s, VorN=%s WHERE I_No=%s",(iname, price, category, vorn, ino))

        CN.commit()
        CN.close()
        return True

    except Exception as e:
        print("update_dish error:", e)
        return False
    
def book_table(table_no):
    CN=get_connection()
    CUR = CN.cursor()

    CUR.execute("SELECT Status FROM tables WHERE TableNo=%s", (table_no,))
    status = CUR.fetchone()
    if not status[0]!= "Available":
        CN.close()
        return False

    CUR.execute("UPDATE tables SET Status='Occupied' WHERE TableNo=%s",(table_no,))

    CN.commit()
    CN.close()
    return True

def guests():
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("SELECT * FROM guests")
        data = CUR.fetchall()
        CN.close()
        return data
    except Exception as e:
        print(e)
        return []

def search_guest_id(uid):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("SELECT * FROM guests WHERE UserID=%s", (uid,))
        data = CUR.fetchall()
        CN.close()
        return data
    except Exception as e:
        print(e)
        return []

def search_guest_name(name):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("SELECT * FROM guests WHERE UserName LIKE %s", (f"%{name}%",))
        data = CUR.fetchall()
        CN.close()
        return data
    except Exception as e:
        print(e)
        return []
def remove_guest(uid):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("DELETE FROM guests WHERE UserID=%s", (uid,))
        CUR.execute("DELETE FROM users WHERE UserID=%s", (uid,))
        CN.commit()
        CN.close()
        return True
    except Exception as e:
        print(e)
        return False

def change_guest(user_id, username, phone, address, gender):
    try:
        CN=get_connection()
        CUR = CN.cursor()

        CUR.execute("UPDATE guests SET UserName=%s, PhoneNum=%s, Address=%s, Gender=%s WHERE UserID=%s",(username, phone, address, gender, user_id))
        CUR.execute("UPDATE users SET UserName=%s WHERE UserID=%s",(username, user_id))

        CN.commit()
        CN.close()
        return True

    except Exception as e:
        print("update_guest error:", e)
        return False

def add_guest(username, password, phone, address, gender):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        usertype = "Guest"

        CUR.execute("INSERT INTO users (UserName, password, Work) VALUES (%s, %s, %s)",(username, password, usertype))
        user_id = CUR.lastrowid
        CUR.execute("INSERT INTO guests (UserID, UserName, PhoneNum, Address, Gender, UserType) VALUES (%s, %s, %s, %s, %s, %s)",(user_id, username, phone, address, gender, usertype))
        CN.commit()
        CN.close()
        return user_id

    except Exception as e:
        print("create_guest error:", e)
        return None

def staff():
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("SELECT * FROM staff")
        data = CUR.fetchall()
        CN.close()
        return data
    except Exception as e:
        print(e)
        return []

def search_staff_id(uid):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("SELECT * FROM staff WHERE UserID=%s", (uid,))
        data = CUR.fetchall()
        CN.close()
        return data
    except Exception as e:
        print(e)
        return []

def search_staff_name(name):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("SELECT * FROM staff WHERE UserName LIKE %s", (f"%{name}%",))
        data = CUR.fetchall()
        CN.close()
        return data
    except Exception as e:
        print(e)
        return []
def remove_staff(uid):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        CUR.execute("DELETE FROM staff WHERE UserID=%s", (uid,))
        CUR.execute("DELETE FROM users WHERE UserID=%s", (uid,))
        CN.commit()
        CN.close()
        return True
    except Exception as e:
        print(e)
        return False

def change_staff(user_id, username, dept, phone, doj, address, gender):
    try:
        CN=get_connection()
        CUR = CN.cursor()

        CUR.execute("UPDATE staff SET UserName=%s,Dept=%s, PhoneNum=%s, DateofJoining=%s, Address=%s, Gender=%s where UserID=%s",(username, dept, phone,doj, address, gender, user_id))
        CUR.execute("UPDATE users SET UserName=%s WHERE UserID=%s",(username, user_id))

        CN.commit()
        CN.close()
        return True

    except Exception as e:
        print("update_staff error:", e)
        return False

def add_staff(username, password,dept, phone,doj, address, gender):
    try:
        CN=get_connection()
        CUR = CN.cursor()
        usertype = "Staff"

        CUR.execute("INSERT INTO users (UserName, password, Work) VALUES (%s, %s, %s)",(username, password, usertype))
        user_id = CUR.lastrowid
        CUR.execute("INSERT INTO staff (UserID, UserName,Dept, PhoneNum,DateofJoining,Address,Gender, UserType) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)",(user_id, username,dept, phone, doj, address, gender, usertype))
        CN.commit()
        CN.close()
        return user_id

    except Exception as e:
        print("create_staff error:", e)
        return None

def calculate_bill(user_id):
    try:
        CN=get_connection()
        CUR=CN.cursor()
        room_total=0
        food_total=0

        CUR.execute("SELECT SUM(r.Price) FROM room_booking rb JOIN rooms r ON rb.RoomNo=r.RoomNumWHERE rb.U_Id=%s",(user_id,))
        result=CUR.fetchone()

        if result[0]:
            room_total=result[0]

        CUR.execute("SELECT SUM(Total)FROM order_info WHERE UserID=%s",(user_id,))
        result=CUR.fetchone()
        
        if result[0]:
            food_total=result[0]
        total=room_total+food_total
        CN.close()
        return room_total,food_total,total

    except Exception as e:
        print(e)
        return 0,0,0
    
def add_feedback(username, rating, comments):
    try:
        CN=get_connection()
        CUR=CN.cursor()
        CUR.execute("INSERT INTO feedback(UserName,Rating,Comments,FeedbackDate)VALUES(%s,%s,%s,CURDATE())",(username,rating,comments))
        CN.commit()
        CN.close()
        return True
    except Exception as e:
        print(e)
        return False
    
def feedbacks():
    CN=get_connection()
    CUR=CN.cursor()
    CUR.execute("SELECT * FROM feedback ORDER BY FeedbackDate DESC")
    data=CUR.fetchall()
    CN.close()
    return data
    
