from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector as CON
from tkinter import messagebox, simpledialog
from datetime import datetime
from database import login,signin,room_booking,room_details,remove_room_booking,menu,book_table,create_order,remove_order,add_item,add_dish,remove_dish,update_dish,table_booking_details,remove_table_booking,guests,search_guest_id,search_guest_name,remove_guest,change_guest,add_guest,staff,search_staff_id,search_staff_name,remove_staff,change_staff,add_staff,calculate_bill,add_feedback,feedbacks

def add_logo(page):
    logo=Image.open("SRS Hotel Logo.jpg")
    logo=logo.resize((150, 100))
    page.logo_photo = ImageTk.PhotoImage(logo)

    page.logo_label=tk.Label(page,image=page.logo_photo,bg="#0B1F3A")
    page.logo_label.place(x=15, y=15)

class MainPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="#0B1F3A")

        center_frame=tk.Frame(self,bg="#0B1F3A")
        center_frame.place(relx=0.5,rely=0.5, anchor="center")

        def resize_image(path, max_width, max_height):
            img = Image.open(path)
            img.thumbnail((max_width, max_height))
            return ImageTk.PhotoImage(img)
        self.left_photo=resize_image("hotel pics/hotel1.jpg",500,1000)
        self.right_photo=resize_image("hotel pics/hotel2.jpg",500,1000)
        self.left_label = tk.Label(self, image=self.left_photo)
        self.left_label.place(x=20, y=300)
        self.right_label = tk.Label(self, image=self.right_photo)
        self.right_label.place(x=940, y=300)
        
        logo = Image.open("SRS Hotel Logo.jpg")
        logo = logo.resize((150, 100))
        self.logo_photo = ImageTk.PhotoImage(logo)

        title_frame = tk.Frame(self, bg="#0B1F3A")
        title_frame.pack(pady=20)
        tk.Label(title_frame,image=self.logo_photo,bg="#0B1F3A").pack(side="left", padx=10)
        
        self.label=tk.Label(self, text="SRS HOTEL DATABASE",font=('Garamond',64,'bold'),bg="#0B1F3A",fg="#F5E6C8")
        self.label.pack(pady=20)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        subtitle=tk.Label(center_frame,text="Luxury • Comfort • Excellence",font=("Garamond", 18, "italic"),bg="#0B1F3A",fg="#D4AF37")
        subtitle.pack(pady=10)

        self.buttonframe=tk.Frame(center_frame,bg="#0B1F3A")
        button_style={"font": ("Garamond",18,"bold"),"bg": "#F5E6C8","fg": "#0B1F3A","width": 15,"height": 2,"relief": "flat","cursor": "hand2"}

        self.btn1=tk.Button(self.buttonframe, text="Log in", font=('Garamond',18),bg='#08172B',fg="#D4AF37", command=lambda: controller.show_frame(LoginPage))
        self.btn1.grid(row=0,column=0,padx=5)

        self.btn2=tk.Button(self.buttonframe, text="Sign in", font=('Garamond',18),bg='#08172B',fg="#D4AF37", command=lambda: controller.show_frame(SignInPage))
        self.btn2.grid(row=0,column=1,padx=5)

        self.btn3=tk.Button(self.buttonframe, text="About Hotel", font=('Garamond',18),bg='#08172B',fg="#D4AF37",command=lambda: controller.show_frame(AboutPage))
        self.btn3.grid(row=0,column=2,padx=5)

        self.buttonframe.pack()

class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(bg="#0B1F3A")
        self.controller=controller

        add_logo(self)
        tk.Label(self, text="LOGIN PAGE",font=('Garamond',32,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()

        login_frame = tk.Frame(self,bg="#0B1F3A",bd=4,relief="ridge")
        login_frame.pack(pady=30)
        
        tk.Label(login_frame, text="User ID",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        self.useri_entry=tk.Entry(login_frame)
        self.useri_entry.pack(pady=10)
        
        tk.Label(login_frame, text="Username",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        self.usern_entry=tk.Entry(login_frame)
        self.usern_entry.pack(pady=10)

        tk.Label(login_frame, text="Password",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        self.pass_entry=tk.Entry(login_frame, show="*")
        self.pass_entry.pack(pady=10)
        
        tk.Button(login_frame, text="Login",font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.login).pack(pady=10)
        tk.Button(login_frame, text='Back',font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=lambda:self.controller.show_frame(MainPage)).pack(pady=10)

        self.msg=tk.Label(login_frame,text="",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8")
        self.msg.pack()
        
    def login(self):
        try:
            self.msg.config(text="")
            uid = int(self.useri_entry.get())
            uname = self.usern_entry.get()
            pwd = self.pass_entry.get()

            if not uid or not uname or not pwd:
                self.msg.config(text="Wrong credentials", fg="red")
                return
            
            result= login(uid,uname,pwd)
            if result:
                self.controller.current_user = result
                print("Logged in:",self.controller.current_user)
                self.useri_entry.delete(0, tk.END)
                self.usern_entry.delete(0, tk.END)
                self.pass_entry.delete(0, tk.END)
                self.msg.config(text="Login Sucessful",fg="green")
                self.controller.frames[RoomDetailsPage].refresh()
                self.controller.frames[RestaurantPage].refresh()
                if result[3]=="Staff":

                     self.controller.show_frame(StaffDashboardPage)
                else:
                    self.controller.show_frame(DashboardPage)
            else:
                self.msg.config(text="Invalid User ID, Username or Password", fg="red")


        except ValueError:
            self.msg.config(text="User ID must be a number", fg="red")

        except Exception as e:
            self.msg.config(text=str(e), fg="red")
        
class SignInPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="#0B1F3A")

        self.controller=controller
        add_logo(self)

        tk.Label(self, text="SIGN-IN PAGE",font=('Garamond',32,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        signin_frame = tk.Frame(self,bg="#0B1F3A",bd=4,relief="ridge")
        signin_frame.pack(pady=30)
        tk.Label(signin_frame, text="Username",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        self.usern_entry=tk.Entry(signin_frame)
        self.usern_entry.pack(pady=10)

        tk.Label(signin_frame, text="Password",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        self.pass_entry=tk.Entry(signin_frame, show="*")
        self.pass_entry.pack(pady=10)

        tk.Label(signin_frame, text="Identity",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        self.identity_var=tk.StringVar(value="Guest")
        identity_menu=tk.OptionMenu(signin_frame,self.identity_var,"Guest","Staff")
        identity_menu.pack(pady=5)

        self.extra_frame = tk.Frame(signin_frame)
        self.extra_frame.pack(pady=10)

        self.next_btn =tk.Button(signin_frame,text="Next",font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.account)
        self.next_btn.pack(pady=10)
        tk.Button(signin_frame, text='Back',font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=lambda:self.controller.show_frame(MainPage)).pack(pady=10)
        
        self.msg=tk.Label(self,text="",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8")
        self.msg.pack()
        
    def signin(self):
        uname = self.usern_entry.get()
        pwd = self.pass_entry.get()
        Id=self.identity_var.get()

        if not uname or not pwd:
            self.msg.config(text="Fill all fields correctly", fg="red")

        try:
            if Id=="Guest":
                uid=add_guest(uname,pwd,selF.phone_entry.get().strip(),self.address_entry.get().strip(),self.gender_var.get())
                if uid:
                    self.msg.config(text=f"Account Created. Your User ID is {uid}",fg="green")
                    self.after(2000,lambda:self.controller.show_frame(LoginPage))
            else:
                uid=add_staff(uname,pwd,self.dept_entry.get().strip(),self.phone_entry.get().strip(),self.doj_entry.get().strip(),self.address_entry.get().strip(),self.gender_var.get())
                if uid:
                    self.msg.config(text=f"Account Created. Your User ID is {uid}",fg="green")
                    self.after(2000,lambda:self.controller.show_frame(LoginPage))
                
                self.msg.config(text="Fill all fields correctly", fg="red")

        except Exception as e:
            self.msg.config(text=str(e),fg="red")

    def account(self):
        uname = self.usern_entry.get().strip()
        pwd = self.pass_entry.get().strip()

        if not uname or not pwd:
            self.msg.config(text="Enter username and password first",fg="red")
            return

        for widget in self.extra_frame.winfo_children():
            widget.destroy()

        if self.identity_var.get() == "Guest":
            tk.Label(self.extra_frame,text="Phone", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=0,column=0,padx=5,pady=5)
            self.phone_entry=tk.Entry(self.extra_frame)
            self.phone_entry.grid(row=0,column=1)

            tk.Label(self.extra_frame,text="Address", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=1,column=0,padx=5,pady=5)
            self.address_entry=tk.Entry(self.extra_frame)
            self.address_entry.grid(row=1,column=1)

            tk.Label(self.extra_frame,text="Gender", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=2,column=0,padx=5,pady=5)
            self.gender_var=tk.StringVar(value="Female")
            tk.OptionMenu(self.extra_frame,self.gender_var,"Female","Male","Other").grid(row=2,column=1)

        else:

            tk.Label(self.extra_frame,text="Department", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=0,column=0,padx=5,pady=5)
            self.dept_entry=tk.Entry(self.extra_frame)
            self.dept_entry.grid(row=0,column=1)

            tk.Label(self.extra_frame,text="Phone", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=1,column=0,padx=5,pady=5)
            self.phone_entry=tk.Entry(self.extra_frame)
            self.phone_entry.grid(row=1,column=1)

            tk.Label(self.extra_frame,text="Date of Joining(YYYY/MM/DD)", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=2,column=0,padx=5,pady=5)
            self.doj_entry=tk.Entry(self.extra_frame)
            self.doj_entry.grid(row=2,column=1)

            tk.Label(self.extra_frame,text="Address", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=3,column=0,padx=5,pady=5)
            self.address_entry=tk.Entry(self.extra_frame)
            self.address_entry.grid(row=3,column=1)

            tk.Label(self.extra_frame,text="Gender", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=4,column=0,padx=5,pady=5)
            self.gender_var=tk.StringVar(value="Female")
            tk.OptionMenu(self.extra_frame,self.gender_var,"Female","Male","Other").grid(row=4,column=1)

        tk.Button(self.extra_frame,text="Create Account",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8",command=self.signin).grid(row=5,column=0,columnspan=2,pady=10)      
        
class DashboardPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="#0B1F3A")

        self.controller=controller

        tk.Label(self, text="DASHBOARD",font=('Garamond',64,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        tk.Button(self, text="Room Booking", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=lambda: controller.show_frame(RoomDetailsPage)).pack(pady=10)
        tk.Button(self, text="Restaurant", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=lambda: controller.show_frame(RestaurantPage)).pack(pady=10)
        tk.Button(self,text="Give Feedback", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",width=25,command=self.feedback).pack(pady=10)
        tk.Button(self,text="View Current Bill", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",width=25,command=self.view_bill).pack(pady=10)
        tk.Button(self, text="Log out", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.logout).pack(pady=10)
        
        self.status=tk.Label(self,text="",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8")
        self.status.pack()
    def view_bill(self):
        room, food, total = calculate_bill(self.controller.current_user[0])
        messagebox.showinfo("Current Bill",f"""----------- CURRENT BILL -----------

Room Charges        : {room}

Restaurant Charges  : {food}

------------------------------------

TOTAL               : {total}
""")

    def feedback(self):
        rating = simpledialog.askinteger("Feedback","Rating (1-5):",minvalue=1,maxvalue=5)

        if rating is None:
            return
        comment = simpledialog.askstring("Feedback","Comments:")
        if not comment:
            return
        success = add_feedback(self.controller.current_user[1],rating,comment)

        if success:
            messagebox.showinfo("Success","Thank you for your feedback!")
        
    def logout(self):
        self.controller.current_user = None
        self.controller.show_frame(MainPage)

class StaffDashboardPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="#0B1F3A")

        self.controller=controller
        add_logo(self)

        tk.Label(self, text="STAFF DASHBOARD",font=('Garamond',64,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        tk.Button(self, text="Staff Management", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=lambda: controller.show_frame(StaffManagementPage)).pack(pady=10)
        tk.Button(self, text="Guest Management", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=lambda: controller.show_frame(GuestManagementPage)).pack(pady=10)
        tk.Button(self, text="Room Management", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=lambda: controller.show_frame(RoomDetailsPage)).pack(pady=10)
        tk.Button(self, text="Restaurant Management", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=lambda: controller.show_frame(RestaurantPage)).pack(pady=10)
        tk.Button(self,text="View Feedback", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",width=25,command=self.view_feedback).pack(pady=10)
        tk.Button(self,text="Checkout / Billing", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",width=25,command=self.checkout_bill).pack(pady=10)
        tk.Button(self, text="Log out", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.logout).pack(pady=10)

        self.status=tk.Label(self,text="",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8")
        self.status.pack()

    def checkout_bill(self):
        uid = simpledialog.askinteger("Checkout","Enter Guest User ID:")
        if uid is None:
            return
        room, food, total = calculate_bill(uid)
        messagebox.showinfo("Final Bill",f"""----------- FINAL BILL -----------

Guest ID            : {uid}

Room Charges        : {room}

Restaurant Charges  : {food}

------------------------------------

TOTAL               : {total}

Collect payment before checkout.
""")

    def view_feedback(self):
        data = feedbacks()
        if not data:
            messagebox.showinfo("Feedback","No feedback available.")
            return
        text = ""

        for row in data:
            text+=(f"Guest : {row[1]}\n"
                f"Rating : {row[2]}/5\n"
                f"Comment : {row[3]}\n"
                f"Date : {row[4]}\n"
                f"{'-'*40}\n")
            messagebox.showinfo("Guest Feedback",text)
    
    def logout(self):
        self.controller.current_user = None
        self.controller.show_frame(MainPage)

class RoomDetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#0B1F3A")
        self.controller = controller
        add_logo(self)
        
        tk.Label(self, text="ROOM BOOKING",font=('Garamond',64,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        self.room_list = tk.Listbox(self, width=60, height=15)
        self.room_list.pack(pady=10)

        def resize_image(path, max_width, max_height):
            img = Image.open(path)
            img.thumbnail((max_width, max_height))
            return ImageTk.PhotoImage(img)

        self.leftup_photo=resize_image("hotel pics/room1.webp",250,500)
        self.rightup_photo=resize_image("hotel pics/room2.jpg",250,500)
        self.leftmid_photo=resize_image("hotel pics/room3.webp",250,500)
        self.rightmid_photo=resize_image("hotel pics/room4.webp",250,500)
        self.leftdown_photo=resize_image("hotel pics/bath1.png",250,500)
        self.rightdown_photo=resize_image("hotel pics/bath2.webp",250,500)

        self.left_label = tk.Label(self, image=self.leftup_photo)
        self.left_label.place(x=60, y=100)
        self.left_label = tk.Label(self, image=self.leftmid_photo)
        self.left_label.place(x=60, y=300)
        self.left_label = tk.Label(self, image=self.leftdown_photo)
        self.left_label.place(x=60, y=500)

        self.right_label = tk.Label(self, image=self.rightup_photo)
        self.right_label.place(x=1100, y=100)
        self.right_label = tk.Label(self, image=self.rightmid_photo)
        self.right_label.place(x=1100, y=300)
        self.right_label = tk.Label(self, image=self.rightdown_photo)
        self.right_label.place(x=1100, y=500)

        tk.Button(self, text="Load Rooms", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.load_rooms).pack(pady=5)
        tk.Button(self, text="Book Selected Room", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.book_room).pack(pady=5)
        self.remove_frame = tk.Frame(self)
        self.remove_frame.pack(pady=5)
        self.remove_btn=tk.Button(self.remove_frame,text="Remove Booking", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.remove_booking)

        self.back_btn=tk.Button(self, text="Back", font=('Garamond',18),bg="#08172B",fg="#F5E6C8")
        self.back_btn.pack(pady=5)
        
        self.status = tk.Label(self, text="", font=("Garamond", 15),bg="#0B1F3A",fg="#F5E6C8")
        self.status.pack(pady=5)

        self.rooms_data = []

        self.load_rooms()
    def refresh(self):
        if self.controller.current_user and self.controller.current_user[3]=="Staff":
            self.remove_btn.pack(pady=5)
            self.back_btn.config(command=lambda: self.controller.show_frame(StaffDashboardPage))
        else:
            self.remove_btn.pack_forget()
            self.back_btn.config(command=lambda: self.controller.show_frame(DashboardPage))
        
    def book_room(self):
        user= self.controller.current_user
        if user is None:
            self.controller.show_frame(LoginPage)
        else:
            selection = self.room_list.curselection()

            if not selection:
                self.status.config(text="Select a room", fg="red")
                return
            room = self.rooms_data[selection[0]]
            room_id = room[0]
            status = room[3]
            if status!= "Available":
                self.status.config(text="Room not available", fg="red")
                return
            form = self.controller.frames[BookingFormPage]
            form.set_room(room_id)

            self.controller.show_frame(BookingFormPage)

    def remove_booking(self):
        selection = self.room_list.curselection()
        if not selection:
            messagebox.showwarning("Warning","Select a booking.")
            return

        room = self.rooms_data[selection[0]]
        confirm = messagebox.askyesno("Confirm","Delete this booking?")

        if not confirm:
            return
        success = remove_room_booking(room[0])

        if success:
            messagebox.showinfo("Success","Booking removed.")
            self.load_rooms()

        else:
            messagebox.showerror("Error","Could not remove booking.")

    def load_rooms(self):
        self.room_list.delete(0, tk.END)
        self.rooms_data = room_details()

        for r in self.rooms_data:
            self.room_list.insert(tk.END,f"Room {r[0]}|{r[1]}|${r[2]}|{r[3]}|")


class BookingFormPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#0B1F3A")
        self.controller = controller
        add_logo(self)

        tk.Label(self, text="BOOKING FORM",font=('Garamond',64,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        self.room_label = tk.Label(self, text="No room selected")
        self.room_label.pack(pady=5)

        tk.Label(self, text="User ID", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack()
        self.uid_entry = tk.Entry(self)
        self.uid_entry.pack()

        tk.Label(self, text="User Name", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack()
        self.uname_entry = tk.Entry(self)
        self.uname_entry.pack()

        tk.Label(self, text="Check-in Date (YYYY-MM-DD)", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack()
        self.in_entry = tk.Entry(self)
        self.in_entry.pack()

        tk.Label(self, text="Check-out Date (YYYY-MM-DD)", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack()
        self.out_entry = tk.Entry(self)
        self.out_entry.pack()

        tk.Label(self, text="Phone Number", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack()
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()

        tk.Label(self, text="Address", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        tk.Label(self, text="Gender", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack()
        self.gender_var = tk.StringVar(value="Male")

        tk.Radiobutton(self, text="Male", variable=self.gender_var, value="Male").pack()
        tk.Radiobutton(self, text="Female", variable=self.gender_var, value="Female").pack()
        tk.Radiobutton(self, text="Other", variable=self.gender_var, value="Other").pack()

        self.status = tk.Label(self, text="")
        self.status.pack(pady=5)

        tk.Button(self, text="Confirm Booking", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.confirm_booking).pack(pady=5)
        tk.Button(self, text="Back", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=lambda: controller.show_frame(RoomDetailsPage)).pack(pady=5)

        self.room_id = None

    def set_room(self, room_id):
        self.room_id = room_id
        self.room_label.config(text=f"Room ID: {room_id}")

    def confirm_booking(self):
        user = self.controller.current_user
        if not user:
            self.controller.show_frame(LoginPage)
            return
        uid=self.uid_entry.get()
        uname=self.uname_entry.get()
        in_date = self.in_entry.get()
        out_date = self.out_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        try:
            check_in = datetime.strptime(in_date,"%Y-%m-%d")
            check_out = datetime.strptime(out_date,"%Y-%m-%d")
        except ValueError:
            self.status.config(text="Use YYYY-MM-DD format.",fg="red")
            return
        if check_out <= check_in:
            self.status.config(text="Check-out must be after check-in.",fg="red")
            return

        if not (in_date and out_date and phone and address):
            self.status.config(text="Fill all fields", fg="red")
            return
        booking_id = room_booking(RoomNo=self.room_id,U_Id=uid,U_Name=uname,Address=address,PhoneNo=phone,InDate=in_date,OutDate=out_date,Gender=self.gender_var.get())

        if booking_id:
            self.status.config(text=f"Booking successful! This is your Booking ID: {booking_id}", fg="green")
            self.uid_entry.delete(0, tk.END)
            self.uname_entry.delete(0, tk.END)
            self.in_entry.delete(0, tk.END)
            self.out_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.gender_var.set("Male")
            self.room_id = None
            self.room_label.config(text="No room selected")
            self.controller.frames[RoomDetailsPage].load_rooms()
            self.after(1500,lambda:self.controller.show_frame(RoomDetailsPage))            
        else:
            self.status.config(text="Booking failed", fg="red")
            
class RestaurantPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg="#0B1F3A")
        self.controller = controller
        add_logo(self)
        
        self.current_order=None
        canvas = tk.Canvas(self, bg="#0B1F3A", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#0B1F3A")
        scrollable_frame.configure(width=900)

        scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((500, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def resize_image(path, max_width, max_height):
            img = Image.open(path)
            img.thumbnail((max_width, max_height))
            return ImageTk.PhotoImage(img)

        self.leftup_photo=resize_image("hotel pics/rest1.jpg",250,500)
        self.rightup_photo=resize_image("hotel pics/rest2.jpg",250,500)
        self.leftmid_photo=resize_image("hotel pics/menu1.jpg",250,500)
        self.rightmid_photo=resize_image("hotel pics/menu2.jpg",250,500)
        self.leftdown_photo=resize_image("hotel pics/menu3.webp",250,500)
        self.rightdown_photo=resize_image("hotel pics/menu4.webp ",250,500)

        self.left_label = tk.Label(self, image=self.leftup_photo)
        self.left_label.place(x=60, y=100)
        self.left_label = tk.Label(self, image=self.leftmid_photo)
        self.left_label.place(x=60, y=300)
        self.left_label = tk.Label(self, image=self.leftdown_photo)
        self.left_label.place(x=60, y=500)

        self.right_label = tk.Label(self, image=self.rightup_photo)
        self.right_label.place(x=1100, y=100)
        self.right_label = tk.Label(self, image=self.rightmid_photo)
        self.right_label.place(x=1100, y=300)
        self.right_label = tk.Label(self, image=self.rightdown_photo)
        self.right_label.place(x=1100, y=500)

        tk.Label(scrollable_frame, text="RESTAURANT",font=('Garamond',64,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        tk.Label(scrollable_frame, text="TABLES", font=("Garamond", 30),bg="#0B1F3A",fg="#F5E6C8").pack(pady=5)

        self.table_list = tk.Listbox(scrollable_frame, width=60, height=15)
        self.table_list.pack(pady=10)

        tk.Button(scrollable_frame, text="Load Tables", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.show_tables).pack(pady=5)
        
        tk.Label(scrollable_frame, text="Table Number", font=("Garamond", 18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=5)
        self.table_entry=tk.Entry(scrollable_frame)
        self.table_entry.pack()
        
        tk.Button(scrollable_frame, text="Book Table", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.book_table_ui).pack(pady=5)

        self.remove_frame = tk.Frame(self)
        self.remove_frame.pack(pady=5)
        
        tk.Label(scrollable_frame, text="MENU", font=("Garamond", 30),bg="#0B1F3A",fg="#F5E6C8").pack(pady=5)
        tk.Button(scrollable_frame, text="View Menu", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.show_menu).pack(pady=5)
        self.menu_list=tk.Listbox(scrollable_frame,width=80,height=8,selectmode=tk.SINGLE,exportselection=False)
        self.menu_list.bind("<<ListboxSelect>>", self.fill_menu_form)
        self.menu_list.pack(pady=5)
        
        tk.Label(scrollable_frame, text="ORDER", font=("Garamond", 30),bg="#0B1F3A",fg="#F5E6C8").pack(pady=5)
        tk.Label(scrollable_frame, text="Item Number", font=("Garamond", 18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=5)
        self.item_entry=tk.Entry(scrollable_frame)
        self.item_entry.pack()

        tk.Label(scrollable_frame, text="Quantity", font=("Garamond", 18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=5)
        self.qty_entry=tk.Entry(scrollable_frame)
        self.qty_entry.pack()

        tk.Button(scrollable_frame, text="Place Order", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.order_ui).pack(pady=5)
        form_frame = tk.Frame(scrollable_frame)
        form_frame.pack(pady=10)

        tk.Button(scrollable_frame,text="Finish Order", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.finish_order).pack(pady=5)

        tk.Label(scrollable_frame, text="Order Number", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").pack(pady=5)

        self.order_entry = tk.Entry(scrollable_frame)
        self.order_entry.pack()
        self.remove_order_btn=tk.Button(scrollable_frame,text="Remove Order", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.delete_order)
    
        self.staff_frame = tk.Frame(scrollable_frame)
        self.staff_frame.pack(pady=10)

        tk.Label(form_frame, text="Item Number", font=('Garamond',18)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ino_entry = tk.Entry(form_frame, width=20)
        self.ino_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Item Name", font=('Garamond',18)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.iname_entry = tk.Entry(form_frame, width=20)
        self.iname_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Price", font=('Garamond',18)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.price_entry = tk.Entry(form_frame, width=20)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Category", font=('Garamond',18)).grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.category_entry = tk.Entry(form_frame, width=20)
        self.category_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Veg/Non-veg", font=('Garamond',18)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.VorN_var = tk.StringVar(value="Veg")
        tk.OptionMenu(form_frame, self.VorN_var, "Veg", "Non-Veg").grid(row=2, column=1, padx=5, pady=5)
            
        self.msg = tk.Label(scrollable_frame, text="", font=("Garamond", 15),bg="#0B1F3A",fg="#F5E6C8")
        self.msg.pack(pady=5)
            
        self.staff_buttons= tk.Frame(scrollable_frame)
        if self.controller.current_user and self.controller.current_user[3] == "Staff":
            self.staff_buttons.pack(pady=10)

        tk.Button(self.staff_buttons, text="Create Dish", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.create_dish).grid(row=0, column=0, padx=5)
        tk.Button(self.staff_buttons, text="Update Dish", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.update_dish).grid(row=0, column=1, padx=5)
        tk.Button(self.staff_buttons, text="Delete Dish", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.delete_dish).grid(row=0, column=2, padx=5)
        self.remove_btn=tk.Button(self.staff_buttons,text="Remove Table Booking", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.remove_booking)
        self.remove_btn.grid(row=0,column=3,padx=5)
        self.status = tk.Label(scrollable_frame, text="",font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8")
        self.status.pack(pady=10)

        self.back_btn=tk.Button(self, text="Back", font=('Garamond',18),bg="#08172B",fg="#F5E6C8")
        self.back_btn.pack(pady=5)

    def fill_menu_form(self, event=None):
        selection = self.menu_list.curselection()
        if not selection:
            return

        dish = self.data[selection[0]]

        self.ino_entry.delete(0, tk.END)
        self.ino_entry.insert(0, dish[0])

        self.iname_entry.delete(0, tk.END)
        self.iname_entry.insert(0, dish[1])

        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, dish[2])

        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(0, dish[3])

        self.VorN_var.set(dish[4])
        
    def refresh(self):
        if self.controller.current_user and self.controller.current_user[3] == "Staff":
            self.staff_frame.pack(pady=10)
            self.staff_buttons.pack(pady=10)
            self.remove_order_btn.pack(pady=5)
            self.back_btn.config(command=lambda: self.controller.show_frame(StaffDashboardPage))
        else:
            self.staff_frame.pack_forget()
            self.staff_buttons.pack_forget()
            self.remove_order_btn.pack_forget()
            self.back_btn.config(command=lambda: self.controller.show_frame(DashboardPage))
        self.show_menu()
        self.show_tables()
            
    def show_menu(self):
        self.menu_list.delete(0, tk.END)
        self.data=menu()

        for row in self.data:
            self.menu_list.insert(tk.END,f"Item {row[0]} | ${row[1]} | {row[2]} | {row[3]}")
    def show_tables(self):
        self.table_list.delete(0,tk.END)
        self.table_data=table_booking_details()
        for row in self.table_data:
            self.table_list.insert(tk.END,f"Item {row[0]} | {row[1]} | {row[2]} ")
    def delete_order(self):
        try:
            order_no = int(self.order_entry.get())
            confirm = messagebox.askyesno("Confirm",f"Delete Order {order_no}?")

            if not confirm:
                return
            success = remove_order(order_no)
            if success:
                messagebox.showinfo("Success","Order removed successfully.")
                self.order_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error","Order not found.")

        except ValueError:
            messagebox.showerror("Error","Enter a valid Order Number.")
        
    def remove_booking(self):
        selection=self.table_list.curselection()

        if not selection:
            return

        table=self.table_data[selection[0]]
        success=remove_table_booking(table[0])

        if success:
            messagebox.showinfo("Success","Table booking removed.")
            self.show_tables()

        else:
            messagebox.showerror("Error","Could not remove booking.")

    def book_table_ui(self):
        try:
            table_no = int(self.table_entry.get())
            success = book_table(table_no)

            if success:
                self.status.config(text="Table booked successfully!", fg="green")
            else:
                self.status.config(text="Table not available", fg="red")

        except ValueError:
            self.status.config(text="Enter a valid table number", fg="red")
    def order_ui(self):
        try:
            user=self.controller.current_user
            item_no=int(self.item_entry.get())
            qty=int(self.qty_entry.get())
            if self.current_order is None:
                self.current_order = create_order(user[0])
                print("Created order:", self.current_order)
            
            success = add_item(self.current_order, item_no, qty)

            if success:
                self.status.config(text=f"Item added to Order No. {self.current_order}",fg="green")

                self.item_entry.delete(0, tk.END)
                self.qty_entry.delete(0, tk.END)

            else:
                self.status.config(text="Could not add item.", fg="red")

        except ValueError:
            self.status.config(text="Enter a valid item number and quantity",fg="red")
    def finish_order(self):
        if self.current_order is None:
            self.status.config(text="No active order.", fg="red")
            return

        self.status.config(text=f"Order {self.current_order} completed.",fg="green")
        self.current_order = None
    
    def delete_dish(self):
        selected=self.menu_list.curselection()
        if selected:
            dish=self.data[selected[0]]
            success=remove_dish(dish[0])
            self.show_menu()
            if success:
                self.msg.config(text="Dish deleted successfully", fg="green")
                self.show_menu()
                self.clear_form()
            else:
                self.msg.config(text="Dish deletion failed", fg="red")
            
    def create_dish(self):
        iname=self.iname_entry.get().strip()
        price=self.price_entry.get().strip()
        category=self.category_entry.get().strip()
        vorn=self.VorN_var.get()

        if not iname or not price or not category or not vorn :
            self.msg.config(text="Fill all menu fields", fg="red")
            return

        new_dish=add_dish(iname,price,category,vorn)

        if new_dish:
            self.msg.config(text=f"Dish created successfully.", fg="green")
            self.clear_form()
            self.show_menu()
        else:
            self.msg.config(text="Could not create dish", fg="red")

    def update_dish(self):
        selection = self.menu_list.curselection()
        print("Selected:", selection)
        if not selection:
            self.msg.config(text="Select a dish to update", fg="red")
            return

        dish=self.data[selection[0]]
        ino=dish[0]

        iname=self.iname_entry.get().strip()
        price=self.price_entry.get().strip()
        category=self.category_entry.get().strip()
        vorn=self.VorN_var.get()

        if not iname or not price or not category:
            self.msg.config(text="Fill all fields for update", fg="red")
            return

        success=update_dish(ino,iname,price,category,vorn)

        if success:
            self.msg.config(text="Dish updated successfully", fg="green")
            self.show_menu()
        else:
            self.msg.config(text="Dish update failed", fg="red")

    def clear_form(self):
        self.iname_entry.delete(0,tk.END)
        self.price_entry.delete(0,tk.END)
        self.category_entry.delete(0,tk.END)
        self.VorN_var.set('Veg')

class GuestManagementPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="#0B1F3A")

        self.controller=controller
        self.data=[]
        add_logo(self)

        tk.Label(self,text="GUEST MANAGEMENT",font=('Garamond',60,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Guest ID", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=0, column=0, padx=5)
        self.search_id_entry = tk.Entry(search_frame, width=10)
        self.search_id_entry.grid(row=0, column=1, padx=5)

        tk.Button(search_frame, text="Search by ID", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.search_by_id).grid(row=0, column=2, padx=5)

        tk.Label(search_frame, text="Guest Name", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=0, column=3, padx=5)
        self.search_name_entry = tk.Entry(search_frame, width=10)
        self.search_name_entry.grid(row=0, column=4, padx=5)

        tk.Button(search_frame, text="Search by Name", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.search_by_name).grid(row=0, column=5, padx=5)

        tk.Button(search_frame,text="Load All", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.load_guests).grid(row=0, column=6, padx=5)
        self.guest_list=tk.Listbox(self,width=100,height=15)
        self.guest_list.pack(pady=10)
        self.guest_list.bind("<<ListboxSelect>>", self.fill_form)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="User Name", font=('Garamond',18)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = tk.Entry(form_frame, width=20)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Password", font=('Garamond',18)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(form_frame, width=20)
        self.password_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Phone Number", font=('Garamond',18)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(form_frame, width=20)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address", font=('Garamond',18)).grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(form_frame, width=20)
        self.address_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Gender", font=('Garamond',18)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.gender_var = tk.StringVar(value="Female")
        tk.OptionMenu(form_frame, self.gender_var, "Female", "Male", "Other").grid(row=2, column=1, padx=5, pady=5)
        
        self.msg = tk.Label(self, text="", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8")
        self.msg.pack(pady=5)
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Create Guest", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.create_guest).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Selected", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.update_guest).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Selected", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.delete_guest).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Back", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=lambda: controller.show_frame(StaffDashboardPage)).grid(row=0, column=3, padx=5)

        self.load_guests()

    def clear_form(self):
        self.username_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
        self.phone_entry.delete(0,tk.END)
        self.address_entry.delete(0,tk.END)
        self.gender_var.set('Female')
        
    def load_guests(self):
        self.guest_list.delete(0,tk.END)
        self.data=guests()

        for guest in self.data:
            self.guest_list.insert(tk.END,f"ID:{guest[0]} | Name:{guest[1]} | Phone:{guest[2]} | Address:{guest[3]} | Gender:{guest[4]} | Type:{guest[5]}")

    def search_by_id(self):
        uid=self.search_id_entry.get().strip()
        if not uid:
            self.msg.config(text="Enter Guest ID", fg="red")
            return
            
        self.guest_list.delete(0,tk.END)
        self.data=search_guest_id(int(uid))

        for guest in self.data:
            self.guest_list.insert(tk.END,f"ID:{guest[0]} | Name:{guest[1]} | Phone:{guest[2]} | Address:{guest[3]} | Gender:{guest[4]} | Type:{guest[5]}")

    def search_by_name(self):
        name=self.search_name_entry.get().strip()
        if not name:
            self.msg.config(text="Enter Guest Name", fg="red")
            return
            
        self.guest_list.delete(0,tk.END)
        self.data=search_guest_name(name)

        for guest in self.data:
            self.guest_list.insert(tk.END,f"ID:{guest[0]} | Name:{guest[1]} | Phone:{guest[2]} | Address:{guest[3]} | Gender:{guest[4]} | Type:{guest[5]}")

    def delete_guest(self):
        selected=self.guest_list.curselection()
        if selected:
            guest=self.data[selected[0]]
            success=remove_guest(guest[0])
            if success:
                self.msg.config(text="Guest deleted successfully", fg="green")
                self.load_guests()
                self.clear_form()
            else:
                self.msg.config(text="Guest deletion failed", fg="red")
            
    def create_guest(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        gender = self.gender_var.get()

        if not username or not password or not phone or not address:
            self.msg.config(text="Fill all guest fields", fg="red")
            return

        user_id = add_guest(username, password, phone, address, gender)

        if user_id:
            self.msg.config(text=f"Guest created successfully. User ID={user_id}", fg="green")
            self.clear_form()
            self.load_guests()
        else:
            self.msg.config(text="Could not create guest", fg="red")

    def fill_form(self, event=None):
        selection = self.guest_list.curselection()
        if not selection:
            return
        guest = self.data[selection[0]]

        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, guest[1])

        self.password_entry.delete(0, tk.END)

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, guest[2])

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, guest[3])

        self.gender_var.set(guest[4])
    def update_guest(self):
        selection = self.guest_list.curselection()
        if not selection:
            self.msg.config(text="Select a guest to update", fg="red")
            return

        guest = self.data[selection[0]]
        user_id = guest[0]

        username = self.username_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        gender = self.gender_var.get()

        if not username or not phone or not address:
            self.msg.config(text="Fill all fields for update", fg="red")
            return

        success = change_guest(user_id, username, phone, address, gender)

        if success:
            self.msg.config(text="Guest updated successfully", fg="green")
            self.load_guests()
        else:
            self.msg.config(text="Guest update failed", fg="red")

class StaffManagementPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent,bg="#0B1F3A")

        self.controller=controller
        self.data=[]
        add_logo(self)

        tk.Label(self,text="STAFF MANAGEMENT",font=('Garamond',60,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Staff ID", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=0, column=0, padx=5)
        self.search_id_entry = tk.Entry(search_frame, width=10)
        self.search_id_entry.grid(row=0, column=1, padx=5)

        tk.Button(search_frame, text="Search by ID", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.search_by_id).grid(row=0, column=2, padx=5)

        tk.Label(search_frame, text="Staff Name", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8").grid(row=0, column=3, padx=5)
        self.search_name_entry = tk.Entry(search_frame, width=10)
        self.search_name_entry.grid(row=0, column=4, padx=5)

        tk.Button(search_frame, text="Search by Name", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=self.search_by_name).grid(row=0, column=5, padx=5)

        tk.Button(search_frame,text="Load All", font=('Garamond',18),bg="#08172B",fg="#F5E6C8",command=self.load_staff).grid(row=0, column=6, padx=5)
        self.staff_list=tk.Listbox(self,width=100,height=15)
        self.staff_list.pack(pady=10)
        self.staff_list.bind("<<ListboxSelect>>", self.fill_form)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="User Name", font=('Garamond',18)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = tk.Entry(form_frame, width=20)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Password", font=('Garamond',18)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(form_frame, width=20)
        self.password_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Department", font=('Garamond',18)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.dept_entry = tk.Entry(form_frame, width=20)
        self.dept_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Phone Number", font=('Garamond',18)).grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(form_frame, width=20)
        self.phone_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Date of Joining", font=('Garamond',18)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.doj_entry = tk.Entry(form_frame, width=20)
        self.doj_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address", font=('Garamond',18)).grid(row=2, column=2, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(form_frame, width=20)
        self.address_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Gender", font=('Garamond',18)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.gender_var = tk.StringVar(value="Female")
        tk.OptionMenu(form_frame, self.gender_var, "Female", "Male", "Other").grid(row=3, column=1, padx=5, pady=5)
        
        self.msg = tk.Label(self, text="", font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8")
        self.msg.pack(pady=5)
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Create Staff", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.create_staff).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Selected", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.update_staff).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Selected", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=self.delete_staff).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Back", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", width=15, command=lambda: controller.show_frame(StaffDashboardPage)).grid(row=0, column=3, padx=5)

        self.load_staff()

    def clear_form(self):
        self.username_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
        self.dept_entry.delete(0,tk.END)
        self.phone_entry.delete(0,tk.END)
        self.doj_entry.delete(0,tk.END)
        self.address_entry.delete(0,tk.END)
        self.gender_var.set('Female')
        
    def load_staff(self):
        self.staff_list.delete(0,tk.END)
        self.data=staff() or []

        for member in self.data:
            self.staff_list.insert(tk.END,f"ID:{member[0]} | Name:{member[1]} | Dept:{member[2]} | Phone:{member[3]} | DOJ:{member[4]} | Address:{member[5]} | Gender:{member[6]} | Type:{member[7]}")

    def search_by_id(self):
        uid=self.search_id_entry.get().strip()
        if not uid:
            self.msg.config(text="Enter Staff ID", fg="red")
            return
        try:
            self.staff_list.delete(0,tk.END)
            self.data=search_staff_id(int(uid))

            for member in self.data:
                self.staff_list.insert(tk.END,f"ID:{member[0]} | Name:{member[1]} | Dept:{member[2]} | Phone:{member[3]} | DOJ:{member[4]} | Address:{member[5]} | Gender:{member[6]} | Type:{member[7]}")
        except ValueError:
            self.msg.config(text="Staff ID must be a number",fg="red")
            
    def search_by_name(self):
        name=self.search_name_entry.get().strip()
        if not name:
            self.msg.config(text="Enter Staff Name", fg="red")
            return
            
        self.staff_list.delete(0,tk.END)
        self.data=search_staff_name(name)

        for member in self.data:
            self.staff_list.insert(tk.END,f"ID:{member[0]} | Name:{member[1]} | Dept:{member[2]} | Phone:{member[3]} | DOJ:{member[4]} | Address:{member[5]} | Gender:{member[6]} | Type:{member[7]}")
    def delete_staff(self):
        selected=self.staff_list.curselection()
        if selected:
            member=self.data[selected[0]]
            success=remove_staff(member[0])
            
            if success:
                self.msg.config(text="Staff deleted successfully", fg="green")
                self.load_staff()
                self.clear_form()
            else:
                self.msg.config(text="Staff deletion failed", fg="red")
            
    def create_staff(self):
        username=self.username_entry.get().strip()
        password=self.password_entry.get().strip()
        dept=self.dept_entry.get().strip()
        phone=self.phone_entry.get().strip()
        doj=self.doj_entry.get().strip()
        address=self.address_entry.get().strip()
        gender=self.gender_var.get()

        try:
            datetime.strptime(doj,"%Y-%m-%d")
        except:
            self.msg.config(text="Date must be YYYY-MM-DD",fg="red")
            return

        if not username or not password or not dept or not phone or not doj or not address:
            self.msg.config(text="Fill all staff fields", fg="red")
            return

        user_id = add_staff(username, password,dept, phone, doj,address, gender)

        if user_id:
            self.msg.config(text=f"Staff created successfully. User ID = {user_id}", fg="green")
            self.clear_form()
            self.load_staff()
        else:
            self.msg.config(text="Could not create staff", fg="red")

    def fill_form(self, event=None):
        selection = self.staff_list.curselection()
        if not selection:
            return

        member=self.data[selection[0]]

        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, member[1])

        self.password_entry.delete(0, tk.END)

        self.dept_entry.delete(0, tk.END)
        self.dept_entry.insert(0, member[2])
        
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, member[3])

        self.doj_entry.delete(0, tk.END)
        self.doj_entry.insert(0, member[4])

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, member[5])

        self.gender_var.set(member[6])

    def update_staff(self):
        selection = self.staff_list.curselection()
        if not selection:
            self.msg.config(text="Select a staff to update", fg="red")
            return

        member=self.data[selection[0]]
        user_id=member[0]

        username = self.username_entry.get().strip()
        dept=self.dept_entry.get().strip()
        phone = self.phone_entry.get().strip()
        doj = self.doj_entry.get().strip()
        address = self.address_entry.get().strip()
        gender = self.gender_var.get()

        try:
            datetime.strptime(doj,"%Y-%m-%d")
        except:
            self.msg.config(text="Date must be YYYY-MM-DD",fg="red")
            return

        if not username or not dept or not phone or not doj or not address:
            self.msg.config(text="Fill all fields for update", fg="red")
            return

        success = change_staff(user_id, username,dept, phone,doj, address, gender)

        if success:
            self.msg.config(text="Staff updated successfully", fg="green")
            self.load_staff()
        else:
            self.msg.config(text="Staff update failed", fg="red")


class AboutPage(tk.Frame):
     def __init__(self,parent,controller):
        super().__init__(parent,bg="#0B1F3A")
        add_logo(self)

        tk.Label(self, text="ABOUT HOTEL",font=('Garamond',64,'bold'),bg="#0B1F3A",fg="#F5E6C8").pack(pady=10)
        tk.Label(self,text="✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦",font=("Garamond",18),fg="#D4AF37",bg="#0B1F3A").pack()
        info='''✨ Welcome to SRS Hotel – The Crown Jewel of Hospitality and Elegance ✨
Where grandeur meets serenity, and every moment is woven with luxury — SRS Hotel stands as an icon of high-class living and refined comfort. Situated in a location kissed by nature’s beauty and embraced by breathtaking views, SRS is more than a hotel — it is a world of its own, where every detail is designed to enchant, indulge, and inspire.
From the moment you step into our majestic lobby — with its soaring ceilings, hand-crafted chandeliers, and fragrant floral artistry — you are greeted not just as a guest, but as royalty. The architecture seamlessly blends timeless opulence with modern sophistication, setting the tone for an experience that is both rich in heritage and forward in vision.
Our lavish rooms and signature suites offer panoramic views of pristine landscapes, sparkling city lights, or crystal-clear waters — each space a sanctuary of elegance and peace, adorned with premium furnishings, smart amenities, and exquisite attention to detail.
SRS is home to award-winning fine dining restaurants, rooftop lounges, and serene garden cafés that serve global cuisines crafted by world-renowned chefs. Whether you are in the mood for a five-course culinary journey or a quiet evening with handcrafted cocktails, your tastebuds are promised an experience as luxurious as your surroundings.
Unwind in our full-service luxury spa, take a dip in the infinity pool that melts into the horizon, or explore curated activities from private yacht cruises and golf retreats to cultural showcases, cooking classes, and exclusive shopping experiences. For those seeking adventure, wellness, romance, or pure indulgence — SRS Hotel offers the finest of everything, in one unforgettable destination.
From destination weddings and grand celebrations to corporate events and intimate escapes, every experience at SRS is infused with impeccable service, unmatched comfort, and a deep dedication to excellence.
At SRS Hotel, you don’t just stay — you discover a life of magnificence.
Come, be part of a story where luxury is not just seen, but deeply felt'''

        tk.Label(self, text=info, font=('Garamond',18),bg="#0B1F3A",fg="#F5E6C8", justify="center",wraplength=1450).pack()
        tk.Button(self, text="Back", font=('Garamond',18),bg="#08172B",fg="#F5E6C8", command=lambda: controller.show_frame(MainPage)).pack(pady=10)
        

'''

            cn = CON.connect(host="localhost",user="root",password="SLC.123",database="srs_hotel")
            cur = cn.cursor()
            cur.execute("SELECT * FROM users WHERE UserID=%s AND UserName=%s AND Password=%s;"(uid, uname, pwd))

            result =
            cur.fetchall()
            cn.close()

            if result:
                self.msg.config(text="Login successful", fg="green")
                self.controller.show_frame(DashboardPage)
            else:
                self.msg.config(text="Wrong credentials", fg="red")

        except ValueError:
            self.msg.config(text="Invalid input type", fg="red")
        print('-'*40)

        try:
            print('-'*40)
            U_Id=int(input("Enter your user ID:"))
            U_Name=input("Enter user name:")
            Password=int(input("Enter your password:"))
            CN=CON.connect(host="localhost",user="root",password="SLC.123",database="srs_hotel")
            CUR=CN.cursor()
            CUR.execute("select * from users")
            A=CUR.fetchall()
            B=5
            for i in A:
                if U_Name==i[1] and Password==i[2] and U_Id==i[0]:
                        B=6
                        print("-"*40)
                        print("Login successful.")
                        
                        CUR.execute('select * from users where UserID={} and UserName="{}" and Password={}'.format(U_Id,U_Name,Password))
                        s=CUR.fetchall()
                        return s
                if B==5:
                    print("Wrong details given")
                    return None
                CN.commit()
        except ValueError:
            print('Invalid input given.')
        except TypeError:
            print("invalid data type")
        print('-'*40)

        button=tk.Button(root, text="Log in", font=('Garamond',18))
        button.pack(padx=10,pady=10)
'''
class App():
    def __init__(self):

        self.root=tk.Tk()
        self.root.state("zoomed")
        self.root.title("My First GUI")
        self.current_user = None

        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames={}
        self.current_user=None

        for Page in (MainPage, LoginPage, SignInPage, DashboardPage, StaffDashboardPage, RoomDetailsPage, BookingFormPage, RestaurantPage, AboutPage, GuestManagementPage, StaffManagementPage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, page):
        frame = self.frames[page]

        if hasattr(frame, "refresh"):
            frame.refresh()

        frame.tkraise()
app=App()
app.root.mainloop()
