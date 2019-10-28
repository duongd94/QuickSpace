from datetime import date
import random
from copy import copy, deepcopy
import binaryTreeInsert



class WareHouse:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.items = []
        self.p = binaryTreeInsert.warehouseTree(width, height)
    
    def totalSpace(self):
        return self.width*self.height

    def usedSpace(self):
        space = 0
        for item in self.items:
            space += item.width * item.height
        return space

    def remainingSpace(self):
        return self.totalSpace() - self.usedSpace()
        


    def addItem(self, barcode, name, width,
                height, amount, price, owner_name ):
        print("trying to add item width: ", width, ", height: ", height, ", Barcode: ", barcode)
        fits = self.p.addItem(width, height, barcode)
        if not fits:
            return False
        else:
            locations = self.itemLocation(barcode)
            self.items.append(Item(barcode, name, width,
                height, amount, price, owner_name, locations))
            return True

    def itemLocation(self, barcode):
        return self.p.itemLoc(barcode)


    def displayMatrix(self):
        self.p.printWarehouseMatrix()
        # all_rects = self.p.rect_list()
        # tests = [ [ 0 for i in range(self.width) ] for j in range(self.height) ]
        # for i in all_rects:
        #     for j in range(i[3]):# width
        #         for k in range(i[4]):# height
        #             disRow = i[2]
        #             disCol = i[1]
        #             tests[disRow+k][disCol+j] = i[5]
        #             # tests[disCol+j][disRow+k] = 1
        # for i in range(self.height):
        #     for j in range(self.width):
        #         if not tests[i][j] == 0:
        #             print(tests[i][j], end=", ")
        #         else:
        #             print(" ", end=", ")
        #     print("")

    def checkoutItem(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                item.checkout()

    def checkinItem(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                item.checkin()

class Item:
    def __init__(self, barcode, name, width,
                height, amount, price, owner_name, locations):
        self.barcode = barcode
        self.name = name
        self.width = width
        self.height = height
        self.amount = amount
        self.date_in = date.today()
        self.date_out = -1
        self.price = price
        self.owner_name = owner_name
        self.item_locations = locations

    def checkout(self):
        self.date_out = date.today()
    def checkin(self):
        self.date_in = date.today()

# make a warehouse, warehousePacker(width, height)
x = WareHouse(50, 30)                    

# addItem(width, height, barcode)
# fits                                  #(barcode, item_name, width, height, amount,price , owner_name)
print("Was the item placed?: ", x.addItem('d'    , "Disc"   , 3    , 5     , 1     , 20.11, "Jonathan" ))
print("Was the item placed?: ", x.addItem( 2, "Another Disc", 3, 30, 1, 49.99, "JonathanB" ))
print("Was the item placed?: ", x.addItem(3    , "Mouse", 3, 5, 1, 29.99, "Jonathan"))
print("Was the item placed?: ", x.addItem(4    , "Keyboard", 3, 5, 1, 39.99, "Jonathan"))

# Item does not fit 
print("Was the item placed?: ", x.addItem(9, "", 30, 50,1, 99999, "people"))

# checking out item with barcode 'd'
x.checkoutItem('d')
print(x.items[0].date_out)

# checking in item with barcode 'd'
x.checkinItem('d')
print(x.items[0].date_in)

# get the totalspace, usedspace, and remaining space of warehouse
print(x.totalSpace(), x.usedSpace(), x.remainingSpace())

# get location of an item in warehouse, using barcode
print("Location of item with barcode 'd': ",x.itemLocation('d'))
print("Location of item with barcode 2: ",x.itemLocation(2))
print("Location of item with barcode 4: ",x.itemLocation(4))
print("Location of item with barcode 9: ",x.itemLocation(9))

# gives the list of all item rectangles
# print(x.p.rect_list())

# display warehouse
x.displayMatrix()


# x = binaryTreeInsert.warehouseTree(25, 50)
# x.addItem(10, 20, 1)
# x.printNodes()
# x.addItem(5, 5, 2)
# # x.addItem(5, 5, 3)
# x.addItem(5, 5, 4)
# x.addItem(20, 200, 9)
# # x.addItem(20, 30, 5)
# x.addItem(30, 5, 6)
# x.printWarehouseMatrix()