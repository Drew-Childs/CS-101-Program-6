#Drew Childs, Program 6, 11/20/2019
import datetime

class invoice:
    store_address = "4563 Pleasant Hill Road;Newark, Deleware;19713"
    store_name = "Tough Stuff Hardware"
    def __init__(self, item_name : str, item_description : str, item_quantity : int, date, item_price : float):
        self.item_name = item_name
        self.item_description = item_description
        self.item_quantity = item_quantity
        self.date = date
        self.item_price = item_price

    def getInvoiceAmount(self):
        pass

    def __str__(self):
        pass

    def __add__(self):
        pass

Items = { "Screw":["a type of fastener",8.35] \
        ,"Hammer":["a weighted head fixed to a long handle",19.40] \
        ,"pocket knife":[" a foldable knife with one or more blades",8.35] \
        ,"Saw":["a tool consisting of a tough blade",9.99] \
        ,"Ladder":["an inclined set of steps",49.98] \
        ,"Rake":["a broom for outside use",31.99] \
        ,"Gloves":["a garment covering the whole hand"3.62] \
        ,"screwdriver":["screwing and unscrewing screws",9.68] \
        ,"Wrench":["tool used to provide grip",38.35] \
        ,"Allen key":["tool to drive screws with hexagonal sockets",12.53]}

print("Welcome to Tough Stuff Hardware")
while True:
    print("1 - View the items")
    print("2 - Shop")
    print("3 - Check out")
    print("4 - Exit")
    choice = str(input("Please make a choice: "))

    if choice == "1":
        pass

    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        break

    else:
        print("Invalid input, please try again...")
