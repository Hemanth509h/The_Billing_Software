import os
from datetime import datetime
from tkinter import*
from tkinter import messagebox
import random
import pandas as pd
from fpdf import FPDF
import tkinter as tk
from tkinter.font import Font
class CustomerDetails:
    def __init__(self, root1):
        self.root = root1
        self.root.title("Customer Details")
        self.root.geometry("500x400")

        self.cus_name = StringVar()
        self.c_phone = StringVar()
        self.customer_name_entry = None
        self.customer_phone_entry = None
        self.txt = None
        self.products_window = None

        # Cosmetics
        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.sunscreens = IntVar()
        self.conditioners = IntVar()
        self.deodorants = IntVar()

        # Grocery
        self.rice = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.milk = IntVar()
        self.brown_rice = IntVar()
        self.nuts = IntVar()

        # Other products
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.nimko = IntVar()
        self.biscuits = IntVar()
        self.cookies = IntVar()
        self.candy = IntVar()
        self.dried_fruit = IntVar()

        # Total prices and tax variables
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()
        self.total_other_prices = 0
        self.total_grocery_prices = 0
        self.total_cosmetics_prices = 0
        self.total_cost = StringVar(value="Rs. 0")
        self.total_tax_en = StringVar(value="Rs. 0")
        self.bill_no = StringVar()
        self.final_total = IntVar()
        self.show_data_btn = None
        self.discount_amount = 0.0
        self.total_tax = IntVar()
        self.total_before_discount = IntVar()
        self.current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # products prices
        self.bath_soap_price = 40
        self.face_cream_price = 140
        self.face_wash_price = 240
        self.hair_spray_price = 340
        self.body_lotion_price=260
        self.sunscreens_price=600
        self.conditioners_price=350
        self.deodorants_price=200

        self.wheat_price = 100
        self.food_oil_price=180
        self.daal_price=80
        self.rice_price=80
        self.sugar_price=170
        self.milk_price=35
        self.Brown_Rice_price=90
        self.Nuts_price=100

        self.maza_price=20
        self.frooti_price = 50
        self.coke_price = 60
        self.nimko_price = 20
        self.biscuits_price = 20
        self.Cookies_price = 80
        self.Candy_price = 5
        self.Dried_Fruit_price = 200

        self.customer_details()
    def customer_details(self):
        bg_color = "#074463"
        fg_color = "white"
        font = 'inter'

        # Frame for Customer details in the first window
        customer_frame = LabelFrame(self.root, bg=bg_color, relief=GROOVE, bd=10)
        customer_frame.place(width=500, height=400)

        # Title Label
        Label(customer_frame, text="Customer Details", font=(font, 18, "bold"), fg="gold", bg=bg_color).grid(row=0,column=0,columnspan=2,pady=(50, 10))

        # Customer Name
        Label(customer_frame, text="Customer Name", bg=bg_color, fg=fg_color, font=(font, 13, "bold")).grid(row=1,column=0,padx=45,pady=(20, 5),sticky='w')
        self.customer_name_entry = Entry(customer_frame, bd=8, relief=GROOVE, textvariable=self.cus_name)
        self.customer_name_entry.grid(row=1, column=1, ipady=4, ipadx=25, pady=(20, 5), padx=(5, 0))
        self.customer_name_entry.bind("<Return>", lambda event: self.customer_phone_entry.focus())
        # Customer Phone
        Label(customer_frame, text="Phone No", bg=bg_color, fg=fg_color, font=(font, 13, "bold")).grid(row=2, column=0,padx=45,pady=(20, 5),sticky='w')
        self.customer_phone_entry = Entry(customer_frame, bd=8, relief=GROOVE, textvariable=self.c_phone)
        self.customer_phone_entry.grid(row=2, column=1, ipady=4, ipadx=25, pady=(20, 5))
        self.customer_phone_entry.bind("<Return>", lambda event:  self.open_products_window())

        # Enter Button
        enter_button = Button(customer_frame, text="Enter", font=(font, 12), bg="green", fg="white",
                              command=self.open_products_window)
        enter_button.grid(row=4, column=0, pady=10, padx=(125, 5))

        # Exit Button (placed in the next column)
        exit_button = Button(customer_frame, text="Exit", font=(font, 12), bg="green", fg="white",
                             command=self.exit_bill)
        exit_button.grid(row=4, column=1, pady=10, padx=(5, 125))

        self.show_data_btn = Button(customer_frame, text="Show Bill History", font=(font, 12), bg="green", fg="white",
                                    command=self.show_excel_data)
        self.show_data_btn.grid(row=5, column=0, columnspan=2, pady=(20, 0))
    def open_products_window(self):
        customer_name = self.customer_name_entry.get()
        customer_phone =self.customer_phone_entry.get()

        # Validate customer name (only alphabetic characters and spaces)
        if not customer_name.replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Customer name should contain only letters.")
            return False

        # Validate phone number (numeric and length check)
        if not customer_phone.isdigit() or len(customer_phone) != 10:  # Assuming 10 digits for the phone number
            messagebox.showerror("Invalid Input", "Customer phone should be a 10-digit number.")
            return False
        self.products_window = tk.Toplevel(self.root)
        self.products_window.title("Product Details")
        self.products_window.geometry("1280x675")

        # Create frames and widgets
        self.products_window1()
    def products_window1(self):
        customer_name = self.customer_name_entry.get()
        customer_phone = self.customer_phone_entry.get()
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        font = 'inter'

        Label(self.products_window, text="Billing Software", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
              font=(font, 30, "bold"), pady=3).pack(fill=X)

        f0 = LabelFrame(self.products_window, text='customer details', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 16, "bold"))
        f0.place(x=0, y=70, width=1280, height=65)  # Increased height to 85 for more space

        # Customer Name Label
        Label(f0, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Customer Name:").grid(row=0, column=0,padx=10, pady=5)  # Adjusted paddy to 5
        Label(f0, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text=customer_name).grid(row=0, column=1, padx=10,pady=5)

        # Customer Phone Label
        Label(f0, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Customer Phone:").grid(row=0, column=2,padx=10,pady=5)  # Adjusted paddy to 5
        Label(f0, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text=customer_phone).grid(row=0, column=3,padx=10, pady=5)

        # ==================Cosmetics Frame=====================#
        f1 = LabelFrame(self.products_window, text='Cosmetics', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f1.place(x=0, y=135, width=318, height=380)

        # ===========Frame Content
        # ========Bath Soap
        bath_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Bath Soap")
        bath_lbl.grid(row=0, column=0, padx=10, pady=10)
        bath_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.bath_soap, width=15)
        bath_en.grid(row=0, column=1, ipady=3, padx=(5, 20))
        bath_en.bind("<Return>", lambda event: face_en.focus())

        # =======Face Cream
        face_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Face Cream")
        face_lbl.grid(row=1, column=0, padx=10, pady=10)
        face_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.face_cream, width=15)
        face_en.grid(row=1, column=1, ipady=3, padx=(5, 20))
        face_en.bind("<Return>", lambda event: wash_en.focus())
        # ========Face Wash
        wash_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Face Wash")
        wash_lbl.grid(row=2, column=0, padx=10, pady=10)
        wash_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.face_wash, width=15)
        wash_en.grid(row=2, column=1, ipady=3, padx=(5, 20))
        wash_en.bind("<Return>", lambda event: hair_en.focus())
        # ========Hair Spray
        hair_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Hair Spray")
        hair_lbl.grid(row=3, column=0, padx=10, pady=10)
        hair_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.hair_spray, width=15)
        hair_en.grid(row=3, column=1, ipady=3, padx=(5, 20))
        hair_en.bind("<Return>", lambda event: lot_en.focus())

        # ============Body Lotion
        lot_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Body Lotion")
        lot_lbl.grid(row=4, column=0, padx=10, pady=10)
        lot_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.body_lotion, width=15)
        lot_en.grid(row=4, column=1, ipady=3, padx=(5, 20))
        lot_en.bind("<Return>", lambda event: sun_en.focus())

        # ============Sunscreens
        sun_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Sunscreens")
        sun_lbl.grid(row=5, column=0, padx=10, pady=10)
        sun_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.sunscreens, width=15)
        sun_en.grid(row=5, column=1, ipady=3, padx=(5, 20))
        sun_en.bind("<Return>", lambda event: cond_en.focus())
        # ============Conditioners
        cond_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Conditioners")
        cond_lbl.grid(row=6, column=0, padx=10, pady=10)
        cond_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.conditioners, width=15)
        cond_en.grid(row=6, column=1, ipady=3, padx=(5, 20))
        cond_en.bind("<Return>", lambda event: deod_en.focus())
        # ============Deodorants
        deod_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Deodorants")
        deod_lbl.grid(row=7, column=0, padx=10, pady=10)
        deod_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.deodorants, width=15)
        deod_en.grid(row=7, column=1, ipady=3, padx=(5, 20))
        deod_en.bind("<Return>", lambda event: rice_en.focus())

        #============= Grocery

        f1 = LabelFrame(self.products_window, text='Grocery', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f1.place(x=318, y=135, width=318, height=380)

        # ===========Frame Content
        rice_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10)
        rice_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.rice, width=15)  # Reduced width
        rice_en.grid(row=0, column=1, ipady=5, padx=(5, 20))
        rice_en.bind("<Return>", lambda event: oil_en.focus())
        # =======
        oil_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Oil")
        oil_lbl.grid(row=1, column=0, padx=10, pady=10)
        oil_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.food_oil, width=15)  # Reduced width
        oil_en.grid(row=1, column=1, ipady=5, padx=(5, 20))
        oil_en.bind("<Return>", lambda event: daal_en.focus())
        # =======
        daal_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Daal")
        daal_lbl.grid(row=2, column=0, padx=10, pady=10)
        daal_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.daal, width=15)  # Reduced width
        daal_en.grid(row=2, column=1, ipady=5, padx=(5, 20))
        daal_en.bind("<Return>", lambda event: wheat_en.focus())
        # ========
        wheat_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=10)
        wheat_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.wheat, width=15)  # Reduced width
        wheat_en.grid(row=3, column=1, ipady=5, padx=(5, 20))
        wheat_en.bind("<Return>", lambda event: sugar_en.focus())
        # ============
        sugar_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Sugar")
        sugar_lbl.grid(row=4, column=0, padx=10, pady=10)
        sugar_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.sugar, width=15)  # Reduced width
        sugar_en.grid(row=4, column=1, ipady=5, padx=(5, 20))
        sugar_en.bind("<Return>", lambda event: milk_en.focus())

        milk_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Milk")
        milk_lbl.grid(row=5, column=0, padx=10, pady=10)
        milk_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.milk, width=15)  # Reduced width
        milk_en.grid(row=5, column=1, ipady=5, padx=(5, 20))
        milk_en.bind("<Return>", lambda event: brown_rice_en.focus())
        brown_rice_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Brown Rice")
        brown_rice_lbl.grid(row=6, column=0, padx=10, pady=10)
        brown_rice_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.brown_rice, width=15)  # Reduced width
        brown_rice_en.grid(row=6, column=1, ipady=5, padx=(5, 20))
        brown_rice_en.bind("<Return>", lambda event: nuts_en.focus())
        nuts_lbl = Label(f1, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Nuts")
        nuts_lbl.grid(row=7, column=0, padx=10, pady=10)
        nuts_en = Entry(f1, bd=5, relief=GROOVE, textvariable=self.nuts, width=15)  # Reduced width
        nuts_en.grid(row=7, column=1, ipady=5, padx=(5, 20))
        nuts_en.bind("<Return>", lambda event: maza_en.focus())
        f2 = LabelFrame(self.products_window, text='Others', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f2.place(x=636, y=135, width=318, height=380)

        # ===========Frame Content
        maza_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Maza")
        maza_lbl.grid(row=0, column=0, padx=10, pady=10)
        maza_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.maza, width=15)  # Reduced width
        maza_en.grid(row=0, column=1, ipady=5, padx=(5, 20))
        maza_en.bind("<Return>", lambda event: cock_en.focus())
        # =======
        cock_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Coke")
        cock_lbl.grid(row=1, column=0, padx=10, pady=10)
        cock_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.coke, width=15)  # Reduced width
        cock_en.grid(row=1, column=1, ipady=5, padx=(5, 20))
        cock_en.bind("<Return>", lambda event: frooti_en.focus())
        # =======
        frooti_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Frooti")
        frooti_lbl.grid(row=2, column=0, padx=10, pady=10)
        frooti_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.frooti, width=15)  # Reduced width
        frooti_en.grid(row=2, column=1, ipady=5, padx=(5, 20))
        frooti_en.bind("<Return>", lambda event: cold_en.focus())

        # ========
        cold_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Nikos")
        cold_lbl.grid(row=3, column=0, padx=10, pady=10)
        cold_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.nimko, width=15)  # Reduced width
        cold_en.grid(row=3, column=1, ipady=5, padx=(5, 20))
        cold_en.bind("<Return>", lambda event: bis_en.focus())
        # ============
        bis_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Biscuits")
        bis_lbl.grid(row=4, column=0, padx=10, pady=10)
        bis_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.biscuits, width=15)  # Reduced width
        bis_en.grid(row=4, column=1, ipady=5, padx=(5, 20))
        bis_en.bind("<Return>", lambda event: cookies_en.focus())
        cookies_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Cookies")
        cookies_lbl.grid(row=5, column=0, padx=10, pady=10)
        cookies_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.cookies, width=15)  # Reduced width
        cookies_en.grid(row=5, column=1, ipady=5, padx=(5, 20))
        cookies_en.bind("<Return>", lambda event: candy_en.focus())

        candy_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Candy")
        candy_lbl.grid(row=6, column=0, padx=10, pady=10)
        candy_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.candy, width=15)  # Reduced width
        candy_en.grid(row=6, column=1, ipady=5, padx=(5, 20))
        candy_en.bind("<Return>", lambda event: dried_fruit_en.focus())

        dried_fruit_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Dried Fruit")
        dried_fruit_lbl.grid(row=7, column=0, padx=10, pady=10)
        dried_fruit_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.dried_fruit, width=15)  # Reduced width
        dried_fruit_en.grid(row=7, column=1, ipady=5, padx=(5, 20))
        dried_fruit_en.bind("<Return>", lambda event: self.total())

        # ===================Bill Area================#
        f2 = Label(self.products_window, bd=10, relief=GROOVE)
        f2.place(x=954, y=135, width=325, height=380)
        # ===========
        bill_title = Label(f2, text="Bill Area", font=(font, 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(f2, orient=VERTICAL)
        self.txt = Text(f2, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        f3 = LabelFrame(self.products_window, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f3.place(x=0, y=515, relwidth=1, height=160)

        # Configure columns to have equal weight
        for i in range(9):
            f3.columnconfigure(i, weight=1)

        # Buttons and labels as before
        cosm_lbl = Label(f3, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="TotalCosmetics")
        cosm_lbl.grid(row=0, column=0, padx=11, pady=0)
        cosm_en = Entry(f3, bd=8, relief=GROOVE, textvariable=self.total_cosmetics)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        gro_lbl = Label(f3, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Grocery")
        gro_lbl.grid(row=1, column=0, padx=11, pady=5)
        gro_en = Entry(f3, bd=8, relief=GROOVE, textvariable=self.total_grocery)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

        oth_lbl = Label(f3, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Others Total")
        oth_lbl.grid(row=2, column=0, padx=11, pady=5)
        oth_en = Entry(f3, bd=8, relief=GROOVE, textvariable=self.total_other)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

        total_cost_lbl = Label(f3, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Total cost")
        total_cost_lbl.grid(row=0, column=2, padx=30, pady=0)
        total_cost_en = Entry(f3, bd=8, relief=GROOVE, textvariable=self.total_cost)
        total_cost_en.grid(row=0, column=3, ipady=2, ipadx=5)

        total_tax_lbl = Label(f3, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Tax")
        total_tax_lbl.grid(row=2, column=2, padx=10, pady=5)
        total_tax_en = Entry(f3, bd=8, relief=GROOVE, textvariable=self.total_tax_en)
        total_tax_en.grid(row=2, column=3, ipady=2, ipadx=5)

        total_btn = Button(f3, text="Total", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.total)
        total_btn.grid(row=0, column=4, ipadx=20, padx=10, pady=1)

        gen_bill_btn = Button(f3, text="Generate Bill", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        gen_bill_btn.grid(row=0, column=5, ipadx=20, padx=10, pady=1)

        clear_btn = Button(f3, text="Clear", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=0, column=6, ipadx=20, padx=10, pady=1)

        save_btn = Button(f3, text="Save", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.save)
        save_btn.grid(row=2, column=4, ipadx=20, padx=10, pady=1)

        discount_button = Button(f3, text="Apply 5% Discount", bg=bg_color, fg=fg_color, font=("font", 12, "bold"),
                                 bd=7, relief=GROOVE, command=self.bill_area_with_discount)
        discount_button.grid(row=2, column=5, ipadx=20, padx=10, pady=1)

        new_bill = Button(f3, text="New bill", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.new_customer)
        new_bill.grid(row=2, column=6, ipadx=20, padx=10, pady=1)
    def total(self):
        # =================Total Cosmetics Prices
        self.total_cosmetics_prices = (
                (self.bath_soap.get() * self.bath_soap_price) + (self.face_cream.get() * self.face_cream_price) +
                (self.face_wash.get() * self.face_wash_price) + (self.hair_spray.get() * self.hair_spray_price) +
                (self.body_lotion.get() * self.body_lotion_price) + (self.sunscreens.get() * self.sunscreens_price) +
                (self.conditioners.get() * self.conditioners_price) + (self.deodorants.get() * self.deodorants_price)
        )
        self.total_cosmetics.set("Rs. " + str(self.total_cosmetics_prices))
        # ====================Total Grocery Prices
        self.total_grocery_prices = (
                (self.wheat.get() * self.wheat_price) + (self.food_oil.get() * self.food_oil_price) +
                (self.daal.get() * self.daal_price) + (self.rice.get() * self.rice_price) +
                (self.sugar.get() * self.sugar_price) + (self.milk.get() * self.milk_price) +
                (self.brown_rice.get() * self.Brown_Rice_price) + (self.nuts.get() * self.Nuts_price)
        )
        self.total_grocery.set("Rs. " + str(self.total_grocery_prices))
        # ======================Total Other Prices
        self.total_other_prices = (
                (self.maza.get() * self.maza_price) + (self.frooti.get() * self.frooti_price) +
                (self.coke.get() * self.coke_price) + (self.nimko.get() * self.nimko_price) +
                (self.biscuits.get() * self.biscuits_price) + (self.cookies.get() * self.Cookies_price) +
                (self.candy.get() * self.Candy_price) + (self.dried_fruit.get() * self.Dried_Fruit_price)
        )
        self.total_other.set("Rs. " + str(self.total_other_prices))
        total_before_discount = self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices
        total_tax = self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05

        # Update the Entry widget for total cost
        self.total_cost.set("Rs. " + str(total_before_discount))
        self.total_tax_en.set("Rs. " + str(total_tax))
        # Function For Text Area
    def dill_no(self):
        x = random.randint(10000, 99999)
        self.bill_no.set(str(x))
    def bill_area(self):
        self.welcome_soft()
        self.product_lists()
        self.total_in_bill_area()
    def welcome_soft(self):
        self.dill_no()
        self.txt.delete('1.0', END)
        bold_font = Font(family="Helvetica", size=14, weight="bold")
        self.txt.tag_config("bold", font=bold_font)
        bold_font1 = Font(family="Helvetica", size=11, weight="bold")
        self.txt.tag_config("bold1", font=bold_font1)
        # Insert welcome message
        self.txt.insert(END, "      Welcome To VIJETHA \n", "bold")
        self.txt.insert(END, f"\nBill No. : {str(self.bill_no.get())}")
        self.txt.insert(END, f"\nDate and Time : {str(self.current_datetime)}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")
    def add_product_to_bill(self, product_name, quantity, price_per_item):
        if quantity != 0:
            self.txt.insert(END, f"\n{product_name:<16}{quantity:<13}{quantity * price_per_item}")
    def product_lists(self):
        # Add products to the bill
        self.add_product_to_bill("Bath Soap", self.bath_soap.get(), self.bath_soap_price)
        self.add_product_to_bill("Face Cream", self.face_cream.get(), self.face_cream_price)
        self.add_product_to_bill("Face Wash", self.face_wash.get(), self.face_wash_price)
        self.add_product_to_bill("Hair Spray", self.hair_spray.get(), self.hair_spray_price)
        self.add_product_to_bill("Body Lotion", self.body_lotion.get(), self.body_lotion_price)
        self.add_product_to_bill("Sunscreens", self.sunscreens.get(), self.sunscreens_price)
        self.add_product_to_bill("Conditioners", self.conditioners.get(), self.conditioners_price)
        self.add_product_to_bill("Deodorants", self.deodorants.get(), self.deodorants_price)
        self.add_product_to_bill("Wheat", self.wheat.get(), self.wheat_price)
        self.add_product_to_bill("Food Oil", self.food_oil.get(), self.food_oil_price)
        self.add_product_to_bill("Daal", self.daal.get(), self.daal_price)
        self.add_product_to_bill("Rice", self.rice.get(), self.rice_price)
        self.add_product_to_bill("Sugar", self.sugar.get(), self.sugar_price)
        self.add_product_to_bill("Milk", self.milk.get(), self.milk_price)
        self.add_product_to_bill("Brown Rice", self.brown_rice.get(), self.Brown_Rice_price)
        self.add_product_to_bill("Nuts", self.nuts.get(), self.Nuts_price)
        self.add_product_to_bill("Maza", self.maza.get(), self.maza_price)
        self.add_product_to_bill("Frooti", self.frooti.get(), self.frooti_price)
        self.add_product_to_bill("Coke", self.coke.get(), self.coke_price)
        self.add_product_to_bill("Nimko", self.nimko.get(), self.nimko_price)
        self.add_product_to_bill("Biscuits", self.biscuits.get(), self.biscuits_price)
        self.add_product_to_bill("Cookies", self.cookies.get(), self.Cookies_price)
        self.add_product_to_bill("Candy", self.candy.get(), self.Candy_price)
        self.add_product_to_bill("Dried Fruit", self.dried_fruit.get(), self.Dried_Fruit_price)
    def total_in_bill_area(self):
        # Calculate total prices and tax
        total_price = self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices
        tax = total_price * 0.05
        total_with_tax = total_price + tax
        # Insert total amounts
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, f"\n                      Total : {total_price}")
        self.txt.insert(END, f"\n              Total With Tax: {total_with_tax}")
        self.txt.insert(END, f"\n\n                  Total: {total_with_tax}",'bold1')
    def bill_area_with_discount(self):
        # Calculate total prices and tax
        total_price = self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices
        tax = total_price * 0.05
        total_with_tax = total_price + tax
        discount_amount = (5 / 100) * total_with_tax
        final_total = total_with_tax - discount_amount
        self.txt.delete('1.0', END)
        self.welcome_soft()
        self.product_lists()
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, f"\n                      Total : {total_price}")
        self.txt.insert(END, f"\n             Total With Tax : {total_with_tax}")
        self.txt.insert(END, f"\n     Total after 5% Discount: {round(final_total, 2)}")
        self.txt.insert(END, f"\n\n               Total Rs. {round(final_total, 2)}",'bold1')
    def save(self):
        self.save_bill()
        self.save_bill_excel()
    def save_bill(self):
        bill_content = self.txt.get(1.0, END).strip()
        if not bill_content:
            messagebox.showwarning("Warning", "The Bill Area is empty! Please generate a bill before saving.")
            return
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in bill_content.split('\n'):
            pdf.cell(200, 10, line, ln=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_file = f"Bill_{timestamp}.pdf"
        pdf.output(pdf_file)
        print(f"Bill has been saved as {pdf_file}!")
    def save_bill_excel(self):
        final_total1 =(self.total_cosmetics_prices + self.total_grocery_prices +
                       self.total_other_prices + self.total_cosmetics_prices * 0.05 +
                       self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05)
        final_total2=final_total1 - self.discount_amount
        bill_number=int(self.bill_no.get())

        total_price_formatted = f"Rs. {final_total2:.2f}"

        excel_file_name = "Bill_History.xlsx"
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        customer_data = {
            "Date and Time": [current_datetime],
            "Bill no.":[bill_number],
            "Customer Name": [self.cus_name.get()],
            "Customer Phone": [self.c_phone.get()],
            "Total Price": [total_price_formatted]
        }

        # Create a DataFrame from the customer details
        df = pd.DataFrame(customer_data)

        # Check if the file already exists
        file_exists = os.path.exists(excel_file_name)

        if not file_exists:
            # Create a new Excel file with headers
            df.to_excel(excel_file_name, index=False)
        else:
            # Append to existing Excel file without headers
            with pd.ExcelWriter(excel_file_name, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)

        print(f"Bill details saved to {excel_file_name}")
    def clear(self):
        # Clear the text widget
        self.txt.delete('1.0', END)
        # Reset all Entry fields
        self.bath_soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.hair_spray.set(0)
        self.body_lotion.set(0)
        self.sunscreens.set(0)
        self.conditioners.set(0)
        self.deodorants.set(0)
        self.wheat.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.rice.set(0)
        self.sugar.set(0)
        self.milk.set(0)
        self.brown_rice.set(0)
        self.nuts.set(0)
        self.maza.set(0)
        self.frooti.set(0)
        self.coke.set(0)
        self.nimko.set(0)
        self.biscuits.set(0)
        self.cookies.set(0)
        self.candy.set(0)
        self.dried_fruit.set(0)
        # Reset all Label fields
        self.total_cosmetics.set("Rs. 0")
        self.tax_cos.set("Rs. 0")
        self.total_grocery.set("Rs. 0")
        self.tax_groc.set("Rs. 0")
        self.total_other.set("Rs. 0")
        self.tax_other.set("Rs. 0")
        self.total_cost.set("Rs. 0")
        self.total_tax_en.set("Rs. 0")
    def new_customer(self):
        self.clear()
        self.products_window.destroy()
        self.customer_details()
        self.customer_name_entry.delete(0, END)
        self.customer_phone_entry.delete(0, END)
    def show_excel_data(self):
        # File path for the Excel file
        excel_file_name = "Bill_History.xlsx"

        # Check if the file exists
        if not os.path.exists(excel_file_name):
            print("Excel file does not exist!")
            return

        # Read data from Excel file
        df = pd.read_excel(excel_file_name)

        # Create a new window to display the data
        data_window = Toplevel(self.root)
        data_window.title("Bill History")

        bg_color = "#074463"
        fg_color = "white"
        font = 'inter'

        # Frame for displaying data
        data_frame = tk.LabelFrame(data_window, text="Bill History", bg=bg_color, fg="gold", relief=GROOVE, bd=10, font=(font, 18, "bold"))
        data_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Create a Text widget to display the data
        text_widget = Text(data_frame, wrap='none', bg=bg_color, fg=fg_color, font=(font, 12))
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbars
        scroll_y = Scrollbar(data_frame, orient='vertical', command=text_widget.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.configure(yscrollcommand=scroll_y.set)

        scroll_x = Scrollbar(data_frame, orient='horizontal', command=text_widget.xview)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        text_widget.configure(xscrollcommand=scroll_x.set)

        # Insert the data into the Text widget
        data_str = df.to_string(index=False)  # Convert DataFrame to string
        text_widget.insert(tk.END, data_str)

        # Disable editing in the Text widget
        text_widget.config(state=tk.DISABLED)
    def exit_bill(self):
        self.root.destroy()

        # Close the first window when the second one is opened
        self.root.withdraw()
if __name__ == "__main__":
    root = Tk()
    app = CustomerDetails(root)
    root.mainloop()
