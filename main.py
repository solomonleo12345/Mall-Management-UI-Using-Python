from tkinter import *
from tkinter import ttk

# ***************************** INITIATE WINDOW **********************************************************

'''
This section will create the Window for the Mall
'''

root = Tk()
root.title("MALL Management")
root.geometry("1400x750+0+0")
root.minsize(1400, 750)
root.maxsize(1400, 750)
root.config(bg="black")


# ***************************** INITIATE TABS **********************************************************

# NOTEBOOK used here will help to create different tabs for different uses
'''
Two tabs are used here,
1. Shopping tab - 
    In this tab shopping will be done
2. Gaming tab - 
    In this tab, games can be played
'''

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# This is tab 1
shopping = Frame(my_notebook, width=1400, height=750, bg="black")
shopping.pack(fill="both", expand=1)
my_notebook.add(shopping, text="Shopping")

# This is tab 2
gaming = Frame(my_notebook, width=1400, height=750, bg="black")
gaming.pack(fill="both", expand=1)
my_notebook.add(gaming, text="Gaming")

# @@@@@@@@@@@@@@@@@@@@@@@@ SHOPPING AREA @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# ********************************************************************************************************************

''' 
We will declare "Balance" as a global variable to be able to 
call it anywhere we need
'''

global balance

# ***************************** INITIATE GLOBAL VARIABLES **********************************************************

# List to store the items added to cart in current scope
item_list = []

# Dictionary to store the Rates of all the items of a particular shop
item_rates = {} 


# total_amount = 0

# ***************************************************************************************

# We will add all the item rates respectively to their item slots in that particular Shop

item_rates['NIKE'] = [1143, 3695, 1362, 3037, 2397, 621, 5396, 1499, 2252, 345]
item_rates['MCD'] = [58, 51, 51, 132, 150, 164, 169, 200, 211, 55]
item_rates['CHROMA'] = [69990, 21490, 37999, 62900, 36900, 36200, 48240, 52990, 29190, 150990]
item_rates['CROSSWORDS'] = [999, 799, 449, 250, 146, 499, 399, 269, 499, 599]
item_rates['TITAN'] = [2995, 2595, 2395, 1495, 2245, 1595, 1795, 1795, 1795, 1895]
item_rates['UNDERARMOUR'] = [4393, 6500, 6998, 329, 6590, 2196, 2300, 1171, 3500, 1400]
item_rates['SUBWAY'] = [180, 125, 200, 150, 30, 50, 35, 20, 140, 40]
item_rates['APPLE'] = [39990, 40900, 20900, 71000, 34900, 92900, 199900, 59900, 15900, 1550]
item_rates['RAYMOND'] = [4502, 2553, 6299, 8099, 4049, 2211, 5289, 4599, 2943, 3149]

# ***************************************************************************************

# ADDING ITEMS TO EVERY SHOP TO DISPLAY
shop1_items = ["1,143/-   Men’s slippers", "3,695/-   Revolution 5 shoes",
               "1,362/-   Heritage backpack", "3,037/-   Phantom studs", "2,397/-   Men’s sneakers",
               "621/-       Women’s T-Shirt", "5,396/-   Women’s sneakers ", "1,499/-   Women’s Tights",
               "2,252/-   Women Explore Shoes", "345/-       Ankle size socks"]

shop2_items = ["58/-    McAloo Tikki Burger", "51/-    McVeggie Burger",
               "51/-    Grilled Chatpata Aloo", "132/-  Salad Wrap", "150/-  Filet-o-Fish Burger",
               "164/-  McSpicy Paneer Burger", "169/-  McSpicy Chicken Burger", "200/-  Veg Maharaja Mac",
               "211/-  Chicken Maharaja Mac", "55/-    McEgg Burger"]

shop3_items = ["69,990/-    Vivo X60 Pro Plus", "21,490/-    Oppo F19 Pro",
               "37,999/-    Samsung Galaxy A72", "62,900/-    Apple iPhone 12 Mini",
               "36,900/-    Daikin 1.5 ton AC", "36,200/-    LG 1 Ton 5 star AC",
               "48,240/-    HP 14 Core i5 laptop", "52,990/-    Acer Aspire 5 laptop",
               "29,190/-    Apple iPad 8th Gen Tablet", "150,990/-  Asus ROG Strix Laptop"]

shop4_items = ["999/-  Becoming  Michelle Obama", "799/-  Crescent City: House",
               "449/-  Home Body", "250/-  The Girl who got Labelled", "146/-  Young Storytellers 52 ",
               "499/-  Ikigai", "399/-  Tharoorosaurus", "269/-  By Heart: My Heart", "449/-  Milk and Honey",
               "599/-  The Victory Project"]

shop5_items = ["2,995/-  Lagan - White Dial", "2,595/-  Lagan - Blue Dial",
               "2,395/-  Lagan - Black Dial", "1,495/-  Silver Dial Analog", "2,245/-  Rose Dial Analog",
               "1,595/-  Black Dial Analog", "1,795/-  Workwear Black Dial", "1,795/-  Workwear Blue Dial",
               "1,795/-  Workwear Silver Dial", "1,895/-  Workwear White Dial"]

shop6_items = ["4393/-  Men's UA Breeze Run Short Sleeve",
               "6500/-  Men's UA HOVR™ Machina 2 Running Shoes", "6998/-  Women’s  UA  Running  Shoes",
               "329/-   Adult Sports UA Mask", "6590/-  Men's UA RECOVER™ Crew Long Sleeve",
               "2196/-  Women's UA Tech™ Vent Short Sleeve", "2300/-  Women's HeatGear® Armour Shine Bike Shorts",
               "1171/-  Curry Flow 8 'International Women's Day' Basketball Shoes",
               "3500/-  Men's UA Spotlight Lux MC Football Cleats",
               "1400/-  Men's UA Clone Blur MC Football Cleats"]

shop7_items = ["180/-  Over Roasted Chicken Sandwich", "125/-  Veggie Delite",
               "200/-  Sweet Onion Chicken Teriyaki Wrap", "150/-  Italian B.M.T  Wrap",
               "30/-   Subway Fresh Brewed Tea", "50/-   Gatorade Energy Drink", "35/-   12 oz Coffee",
               "20/-  Chips", "140/-  Musselman’s  Apple  Sauce", "40/-   Huberts  Lemonade"]

shop8_items = ["39990/-   iPhone SE", "40900/-   Apple Watch Series 6",
               "20900/-   Apple Watch Series 3", "71000/-   iPad Pro", "34900/-   iPad Mini",
               "92900/-   MacBook Air", "199900/-  MacBook Pro 16", "59900/-   AirPods Max", "15900/-   Airpods",
               "1550/-    20W USB Power Charger"]

shop9_items = ["4502/-  Full Sleeve Dark Blue Blazer", "2553/-  Men Waistcoat",
               "6299/-  Rayon Purple Blend Suit", "8099/-  Rayon Collar Shawl Suit",
               "4049/-  Full Sleeve Mandarin Collar Shirt", "2211/-  Traditional Men Waistcoat",
               "5289/-  Synthetic Trousers", "4599/-  Poly Blend Solid Suit", "2943/-  Notch Lapel Regular Blazer",
               "3149/-  Contemporary Fit Blazer"]


# ***************************** FUNCTIONS **********************************************************

# create_window will create a pop up window to ask the user to enter his wallet balance

def create_window():
    wallet_window = Toplevel(root)  # toplevel will make this window to come on top of other apps 
    wallet_window.geometry("400x200+500+300")
    wallet_window.config(bg="cornflower blue")

    ask = Label(wallet_window, text="Enter Your Wallet Balance", font=("calibri", 12))
    ask.place(x=10, y=10, width=200, height=40)

    enter_balance = Entry(wallet_window, font=("calibri", 12), textvariable=enter_balance_number, width=20)
    enter_balance.place(x=220, y=10, width=150, height=40)

    # This function will take balance from user and store it in "balance"
    def send_balance():
        global balance

        # wal_bal_total will be used further for "cart total"
        global wal_bal_total
        balance = enter_balance.get()
        wal_bal_total = balance
        wallet_balance_label.config(text=balance)
        wallet_window.destroy()

    get_balance_button = Button(wallet_window, text="Submit", font=("calibri", 18), command=send_balance, width=10)
    get_balance_button.place(x=150, y=100, width=100, height=30)


# buy function will activate when "buy" button will be pressed
def buy():

    # show all the items bought in show_items Label
    show_items.config(text=("Items bought\n\n\n" + "\n".join(item_list)), anchor=N)
    
    # pr_bal will calculate the cart total
    pr_bal = int(wal_bal_total)-int(balance)
    cart_total.config(text=str(pr_bal)+"/-")


# reset_window will reset the whole Window/Mall
def reset_window():
    wallet_balance_label.config(anchor="center", text="Wallet Balance")
    show_items.config(text="")
    item_list.clear()


# ********************************************************************************************************************


# ***************************** SHOW FUNCS **********************************************************

# explanation of this function is shown in show2 function below
def show1():
    for x in range(len(shop1_items)):
        if clicked1.get() == shop1_items[x]:
            global balance
            if int(balance) > item_rates['NIKE'][x]:

                item_list.append(clicked1.get())
                print(balance)
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['NIKE'][x]
                wallet_balance_label.config(text=balance)
                clicked1.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green", font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked1.set("select the ITEMS")


def show2():
    # iterate through all items of shop 2
    for x in range(len(shop2_items)):

        # check if clicked item is equal to any element in item list
        if clicked2.get() == shop2_items[x]:
            global balance
            # check if balance is greater than the rate of the item
            if int(balance) > item_rates['MCD'][x]:
                # add that clicked item to a temporary list
                item_list.append(clicked2.get())
                # show the selected item on label
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                # new balance is equal to main balance - item rate
                balance = int(balance) - item_rates['MCD'][x]
                wallet_balance_label.config(text=balance)
                clicked2.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",
                                   font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked2.set("select the ITEMS")


def show3():
    for x in range(len(shop3_items)):
        if clicked3.get() == shop3_items[x]:
            global balance
            if int(balance) > item_rates['CHROMA'][x]:

                item_list.append(clicked3.get())
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['CHROMA'][x]

                wallet_balance_label.config(text=balance)
                clicked3.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",
                                   font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked3.set("select the ITEMS")


def show4():
    for x in range(len(shop4_items)):
        if clicked4.get() == shop4_items[x]:
            global balance
            if int(balance) > item_rates['CROSSWORDS'][x]:

                item_list.append(clicked4.get())
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['CROSSWORDS'][x]

                wallet_balance_label.config(text=balance)
                clicked4.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",
                                   font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked4.set("select the ITEMS")


def show5():
    for x in range(len(shop5_items)):
        if clicked5.get() == shop5_items[x]:
            global balance
            if int(balance) > item_rates['TITAN'][x]:

                item_list.append(clicked5.get())
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['TITAN'][x]

                wallet_balance_label.config(text=balance)
                clicked5.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked5.set("select the ITEMS")


def show6():
    for x in range(len(shop6_items)):
        if clicked6.get() == shop6_items[x]:
            global balance
            if int(balance) > item_rates['UNDERARMOUR'][x]:

                item_list.append(clicked6.get())
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['UNDERARMOUR'][x]

                wallet_balance_label.config(text=balance)
                clicked6.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",
                                   font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked6.set("select the ITEMS")


def show7():
    for x in range(len(shop7_items)):
        if clicked7.get() == shop7_items[x]:
            global balance
            if int(balance) > item_rates['SUBWAY'][x]:

                item_list.append(clicked7.get())
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['SUBWAY'][x]

                wallet_balance_label.config(text=balance)
                clicked7.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked7.set("select the ITEMS")


def show8():
    for x in range(len(shop8_items)):
        if clicked8.get() == shop8_items[x]:
            global balance
            if int(balance) > item_rates['APPLE'][x]:

                item_list.append(clicked8.get())
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['APPLE'][x]

                wallet_balance_label.config(text=balance)
                clicked8.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",
                                   font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked8.set("select the ITEMS")


def show9():
    for x in range(len(shop9_items)):
        if clicked9.get() == shop9_items[x]:
            global balance
            if int(balance) > item_rates['RAYMOND'][x]:

                item_list.append(clicked9.get())
                show_items.config(text="No. of items selected\n" + str(len(item_list)))
                balance = int(balance) - item_rates['RAYMOND'][x]

                wallet_balance_label.config(text=balance)
                clicked9.set("select the ITEMS")
                break
            else:

                error_show = Label(shopping, text="NO BALANCE OR BALANCE IS LOW", bg="black", fg="lawn green",
                                   font=("calibri", 14))
                error_show.place(x=1050, y=80)
                clicked9.set("select the ITEMS")


# -------------------------------- WIDGETS ----------------------------------------------------------------


# show_items will display all the added and bought items 
show_items = Label(shopping, bg="black", font=("Calibri", 14), relief="groove", bd=2,
                   fg="white")
show_items.place(x=1020, y=120, width=330, height=470)

# reset button
reset_button = Button(shopping, text="RESET", relief="groove", font=("Calibri", 20), bd=4, fg="white", bg="black",
                      activebackground="grey25", command=reset_window)
reset_button.place(x=10, y=30, width=100, height=50)

# mall_name displays the Mall name on top of the window
mall_name = Label(root, text="HAVOK", bg="lightblue", fg="black", font=("century", 28), bd=10, relief="sunken")
mall_name.place(x=570, y=30, width=200, height=70)

# wallet balance frame
wallet_balance_label = Label(root, text="Wallet Balance", bg="black", fg="white", font=("calibri", 20), bd=4,
                             relief="groove")
wallet_balance_label.place(x=1200, y=40, width=190, height=50)

# SHOPS FRAME ***************************************************************************************

# Frame which contains all the shop names
shops_frame = Frame(shopping, bg="black")
shops_frame.place(x=20, y=110, width=300, height=500)

shop1 = Label(shops_frame, text="NIKE", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop1.pack(pady=10)

shop2 = Label(shops_frame, text="McDONALD'S", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop2.pack(pady=10)

shop3 = Label(shops_frame, text="CHROMA", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop3.pack(pady=10)

shop4 = Label(shops_frame, text="CROSSWORDS", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop4.pack(pady=10)

shop5 = Label(shops_frame, text="TITAN", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop5.pack(pady=10)

shop6 = Label(shops_frame, text="UNDERARMOUR", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop6.pack(pady=10)

shop7 = Label(shops_frame, text="SUBWAY", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop7.pack(pady=10)

shop8 = Label(shops_frame, text="APPLE", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop8.pack(pady=10)

shop9 = Label(shops_frame, text="RAYMOND", bg="black", fg="white", font=("calibri", 18), bd=2, relief="groove",
              width=280)
shop9.pack(pady=10)

# ITEMS FRAME ***************************************************************************************

# clicked1 will the store the value (item) selected from the dropdown list of the shops
clicked1 = StringVar()
clicked1.set("select the ITEMS")

clicked2 = StringVar()
clicked2.set("select the ITEMS")

clicked3 = StringVar()
clicked3.set("select the ITEMS")

clicked4 = StringVar()
clicked4.set("select the ITEMS")

clicked5 = StringVar()
clicked5.set("select the ITEMS")

clicked6 = StringVar()
clicked6.set("select the ITEMS")

clicked7 = StringVar()
clicked7.set("select the ITEMS")

clicked8 = StringVar()
clicked8.set("select the ITEMS")

clicked9 = StringVar()
clicked9.set("select the ITEMS")

# items_frame is the frame which contains the items dropdown lists
items_frame = Frame(shopping, bg="black")
items_frame.place(x=350, y=110, width=300, height=500)

# OptionMenu will make a dropdown list of given elements
item1 = OptionMenu(items_frame, clicked1, "1,143/-   Men’s slippers", "3,695/-   Revolution 5 shoes",
                   "1,362/-   Heritage backpack", "3,037/-   Phantom studs", "2,397/-   Men’s sneakers",
                   "621/-       Women’s T-Shirt", "5,396/-   Women’s sneakers ", "1,499/-   Women’s Tights",
                   "2,252/-   Women Explore Shoes", "345/-       Ankle size socks")
item1.place(x=10, y=10, width=280, height=35)
item1.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')

menu1 = shopping.nametowidget(item1.menuname)
menu1.config(font=('calibri', 14), bg="darkorange1")
# item1['width'] = 280

item2 = OptionMenu(items_frame, clicked2, "58/-    McAloo Tikki Burger", "51/-    McVeggie Burger",
                   "51/-    Grilled Chatpata Aloo", "132/-  Salad Wrap", "150/-  Filet-o-Fish Burger",
                   "164/-  McSpicy Paneer Burger", "169/-  McSpicy Chicken Burger", "200/-  Veg Maharaja Mac",
                   "211/-  Chicken Maharaja Mac", "55/-    McEgg Burger")
item2.place(x=10, y=65, width=280, height=35)
item2.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu2 = shopping.nametowidget(item2.menuname)
menu2.config(font=('calibri', 14), bg="gold")

item3 = OptionMenu(items_frame, clicked3, "69,990/-    Vivo X60 Pro Plus", "21,490/-    Oppo F19 Pro",
                   "37,999/-    Samsung Galaxy A72", "62,900/-    Apple iPhone 12 Mini",
                   "36,900/-    Daikin 1.5 ton AC", "36,200/-    LG 1 Ton 5 star AC",
                   "48,240/-    HP 14 Core i5 laptop", "52,990/-    Acer Aspire 5 laptop",
                   "29,190/-    Apple iPad 8th Gen Tablet", "150,990/-  Asus ROG Strix Laptop")
item3.place(x=10, y=120, width=280, height=35)
item3.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu3 = shopping.nametowidget(item3.menuname)
menu3.config(font=('calibri', 14), bg="turquoise")

item4 = OptionMenu(items_frame, clicked4, "999/-  Becoming  Michelle Obama", "799/-  Crescent City: House",
                   "449/-  Home Body", "250/-  The Girl who got Labelled", "146/-  Young Storytellers 52 ",
                   "499/-  Ikigai", "399/-  Tharoorosaurus", "269/-  By Heart: My Heart", "449/-  Milk and Honey",
                   "599/-  The Victory Project")
item4.place(x=10, y=175, width=280, height=35)
item4.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu4 = shopping.nametowidget(item4.menuname)
menu4.config(font=('calibri', 14), bg="gold2")

item5 = OptionMenu(items_frame, clicked5, "2,995/-  Lagan - White Dial", "2,595/-  Lagan - Blue Dial",
                   "2,395/-  Lagan - Black Dial", "1,495/-  Silver Dial Analog", "2,245/-  Rose Dial Analog",
                   "1,595/-  Black Dial Analog", "1,795/-  Workwear Black Dial", "1,795/-  Workwear Blue Dial",
                   "1,795/-  Workwear Silver Dial", "1,895/-  Workwear White Dial")
item5.place(x=10, y=230, width=280, height=35)
item5.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu5 = shopping.nametowidget(item5.menuname)
menu5.config(font=('calibri', 14), bg="grey70")

item6 = OptionMenu(items_frame, clicked6, "4393/-  Men's UA Breeze Run Short Sleeve",
                   "6500/-  Men's UA HOVR™ Machina 2 Running Shoes", "6998/-  Women’s  UA  Running  Shoes",
                   "329/-   Adult Sports UA Mask", "6590/-  Men's UA RECOVER™ Crew Long Sleeve",
                   "2196/-  Women's UA Tech™ Vent Short Sleeve", "2300/-  Women's HeatGear® Armour Shine Bike Shorts",
                   "1171/-  Curry Flow 8 'International Women's Day' Basketball Shoes",
                   "3500/-  Men's UA Spotlight Lux MC Football Cleats",
                   "1400/-  Men's UA Clone Blur MC Football Cleats")
item6.place(x=10, y=285, width=280, height=35)
item6.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu6 = shopping.nametowidget(item6.menuname)
menu6.config(font=('calibri', 14), bg="cyan")

item7 = OptionMenu(items_frame, clicked7, "180/-  Over Roasted Chicken Sandwich", "125/-  Veggie Delite",
                   "200/-  Sweet Onion Chicken Teriyaki Wrap", "150/-  Italian B.M.T  Wrap",
                   "30/-   Subway Fresh Brewed Tea", "50/-   Gatorade Energy Drink", "35/-   12 oz Coffee",
                   "20/-  Chips", "140/-  Musselman’s  Apple  Sauce", "40/-   Huberts  Lemonade")
item7.place(x=10, y=340, width=280, height=35)
item7.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu7 = shopping.nametowidget(item7.menuname)
menu7.config(font=('calibri', 14), bg="springgreen2")

item8 = OptionMenu(items_frame, clicked8, "39990/-   iPhone SE", "40900/-   Apple Watch Series 6",
                   "20900/-   Apple Watch Series 3", "71000/-   iPad Pro", "34900/-   iPad Mini",
                   "92900/-   MacBook Air", "199900/-  MacBook Pro 16", "59900/-   AirPods Max", "15900/-   Airpods",
                   "1550/-    20W USB Power Charger")
item8.place(x=10, y=395, width=280, height=35)
item8.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu8 = shopping.nametowidget(item8.menuname)
menu8.config(font=('calibri', 14), bg="grey75")

item9 = OptionMenu(items_frame, clicked9, "4502/-  Full Sleeve Dark Blue Blazer", "2553/-  Men Waistcoat",
                   "6299/-  Rayon Purple Blend Suit", "8099/-  Rayon Collar Shawl Suit",
                   "4049/-  Full Sleeve Mandarin Collar Shirt", "2211/-  Traditional Men Waistcoat",
                   "5289/-  Synthetic Trousers", "4599/-  Poly Blend Solid Suit", "2943/-  Notch Lapel Regular Blazer",
                   "3149/-  Contemporary Fit Blazer")
item9.place(x=10, y=450, width=280, height=35)
item9.config(bg="black", fg="WHITE", font=("calibri", 18), activebackground='grey65')
menu9 = shopping.nametowidget(item9.menuname)
menu9.config(font=('calibri', 14), bg="brown1")

# AMOUNT FRAME ***************************************************************************************

# amount_frame stores all the "ADD TO CART" buttons in one frame
amount_frame = Frame(shopping, bg="black")
amount_frame.place(x=680, y=110, width=150, height=500)


# these are the buttons to ask the user to add the items to the cart
select1 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white",
                 activebackground="grey55",
                 bd=2, relief="groove", command=show1)
select1.place(x=10, y=10, width=130, height=35)

select2 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show2)
select2.place(x=10, y=65, width=130, height=35)

select3 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show3)
select3.place(x=10, y=120, width=130, height=35)

select4 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show4)
select4.place(x=10, y=175, width=130, height=35)

select5 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show5)
select5.place(x=10, y=230, width=130, height=35)

select6 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show6)
select6.place(x=10, y=285, width=130, height=35)

select7 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show7)
select7.place(x=10, y=340, width=130, height=35)

select8 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show8)
select8.place(x=10, y=395, width=130, height=35)

select9 = Button(amount_frame, text="ADD TO CART", font=("calibri", 16), bg="black", fg="white", bd=2, relief="groove",
                 width=130, command=show9)
select9.place(x=10, y=450, width=130, height=35)

# BUY BUTTONS ***************************************************************************************


# buy button, which will call the buy function
buy1 = Button(shopping, text="BUY", font=("calibri", 18), bg="black", fg="white", bd=2, relief="groove", width=130,
              command=buy)
buy1.place(x=850, y=120, width=150, height=35)


# this label will display the cart total
cart_total = Label(shopping, text="Cart Total", font=("calibri", 18), bg="black", fg="white", relief="groove", bd=2)
cart_total.place(x=1020, y=600, width=180, height=50)

# we will create a string variable, which can change whenever user changes balance
enter_balance_number = StringVar()

# ask_wallet_balance button will call the create_window function, which will ask the user to fill the wallet balance
ask_wallet_balance = Button(root, text="Enter Wallet Balance", font=("calibri", 14), bg="black", fg="white",
                            command=create_window)
ask_wallet_balance.place(x=1000, y=50, width=190, height=40)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @@@@@@@@@@@@@@@@@@@@@@@@ GAMING AREA @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# single_player_frame contains all the games to be played
single_player_frame = Frame(gaming, bg="black", relief="groove", bd=2)
single_player_frame.place(x=140, y=100, width=500, height=500)

# info_frame will display the info of selected game and will ask the player to click the play button
info_frame = Frame(gaming, bg="black", relief="groove", bd=2)
info_frame.place(x=700, y=100, width=500, height=500)
# ************************ FUNCTIONS ************************************************


# this label will display the information of the game
info_label = Label(info_frame, bg="black", fg="white", font=("calibri", 14), relief="groove", bd=4,
                   wraplength=380)
info_label.place(x=50, y=50, width=400, height=300)


# this play_button will start the game
play_button = Button(info_frame, text="Start Game", bg="black", fg="white", font=("calibri", 14))
play_button.place(x=200, y=400, width=100, height=50)


def play_game_1():
    
    # when the play button is pressed this function will be activated
    def play():
        import pong

    # .config() will replace whatever there was previously in info_label to this current information of the game
    info_label.config(
        text="Pong is one of the earliest arcade video games, first released in 1972 by Atari. It is a two-player game based on table tennis. The game features simple 2D graphics. It consists of two paddles used to return a bouncing ball back and forth across the screen. The score is kept by the numbers at the top of the screen.",
        bg="black", fg="white", font=("calibri", 14), relief="groove", bd=4, wraplength=380)
   

    play_button.config(text="Start Game", bg="black", fg="white", font=("calibri", 14), command=play)



def play_game_2():
    def play():
        import space

    info_label.config(
        text="Space Invaders is a 2D fixed shooter game in which the player controls a ship with lasers by moving it horizontally across the bottom of the screen and firing at descending aliens. The aim is to destroy those aliens. The aliens attempt to destroy the ship by firing at it while they approach the bottom of the screen. If they reach the bottom, the alien invasion is successful and the game ends.",
        bg="black", fg="white", font=("calibri", 14), relief="groove", bd=4, wraplength=380)

    play_button.config(text="Start Game", bg="black", fg="white", font=("calibri", 14), command=play)


def play_game_3():
    def play():
        import snakeoriginal

    info_label.config(text="Snake Game is a 2D legendary game, it was first introduced in small cellphones and as users liked it, it became the most liked game for couple of years, in snake game, A snake goes in search of food to grow bigger and bigger, but if it touches itself(body) then it dies. That is the logic behind this game.", bg="black", fg="white",
                      font=("calibri", 14), relief="groove", bd=4, wraplength=380)

    play_button.config(text="Start Game", bg="black", fg="white", font=("calibri", 14), command=play)


def play_game_4():
    def play():
        import connect_four

    info_label.config(text="Connect Four \n(also known as Four Up, Plot Four, Find Four, Captain's Mistress, "
                           "Four in a Row, Drop Four, and Gravitrips in the Soviet Union) is a "
                           "two-player connection board game, in which the players choose a color and then "
                           "take turns dropping colored discs into a seven-column, six-row vertically "
                           "suspended grid. The pieces fall straight down, occupying the lowest available "
                           "space within the column. The objective of the game is to be the first to form a "
                           "horizontal, vertical, or diagonal line of four of one's own discs. ", bg="black",
                      fg="white", font=("calibri", 14), relief="groove", bd=4, wraplength=380)

    play_button.config(text="Start Game", bg="black", fg="white", font=("calibri", 14), command=play)


# ************************ WIDGETS ************************************************

# FRAMES


# BUTTONS

game1 = Button(single_player_frame, text="PONG", bg="black", fg="white", font=("calibri", 14), relief="groove",
               bd=2, width=400, command=play_game_1)
game1.pack(padx=20, pady=20)

game4 = Button(single_player_frame, text="SPACE INVADERS", bg="black", fg="white", font=("calibri", 14),
               relief="groove",
               bd=2, width=400, command=play_game_2)
game4.pack(padx=20, pady=20)

game3 = Button(single_player_frame, text="SNAKE GAME", bg="black", fg="white", font=("calibri", 14), relief="groove",
               bd=2, width=400, command=play_game_3)
game3.pack(padx=20, pady=20)

game2 = Button(single_player_frame, text="CONNECT 4", bg="black", fg="white", font=("calibri", 14), relief="groove",
               bd=2, width=400, command=play_game_4)
game2.pack(padx=20, pady=20)

# ************************************************************************************************
root.mainloop()

