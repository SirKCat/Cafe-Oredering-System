import datetime
from prettytable import PrettyTable
import os


# Receipt printing component
class Receipt:
    total = 0
    date = (datetime.datetime.now()).strftime("%d %B %I:%M %p")

    # Printing Receipt on The terminal
    @staticmethod
    def printReceipt(_customerOrderList, total):
        table = PrettyTable(['       ID        ', '     Item     ', '     Count     ',
                             '      Price      '])
        print(""" ******************************** CAFE RECEIPT ******************************** """)
        print(Receipt.date)
        for item, count in _customerOrderList:
            table.add_row([item.ID, item.name, count, item.price])
        table.add_row(["", 'TOTAL', "", total])
        #Receipt.printReceipt2(table)
        print(table)

    # Printing Receipt on the default printer
    @staticmethod
    def printReceipt2(receipt):
        with open("receipt.txt", "w+") as f:
            f.write(str(receipt))
        # sleep(1)
        os.startfile("receipt.txt", "print")

    # Calculate the of order list
    @staticmethod
    def calculateTotal(customerOrderList):
        # print("customerOrderList:", customerOrderList)
        for item, count in customerOrderList:
            # print(item, count)
            Receipt.total = Receipt.total + item.price * count
        Receipt.printReceipt(customerOrderList, Receipt.total)
        Receipt.total = 0
