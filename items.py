# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:46:59 2019

@author: aksha
"""
import os
from pathlib import Path
from datetime import date
import random
import binaryTreeInsert
import json

(300, 300, "warehouse")
class WareHouse:
    """initialize warehouse"""
    def __init__(self, height, width, name):
        self.width = width
        self.height = height
        self.items = []
        self.p = binaryTreeInsert.warehouseTree(width, height)
        self.warehouseName = name

    def totalSpace(self):
        """return total space"""
        return self.width*self.height

    def usedSpace(self):
        """reutrn total used space"""
        space = 0
        for item in self.items:
            space += item.width * item.height
        return space

    def remainingSpace(self):
        """return remaining space"""
        return self.totalSpace() - self.usedSpace()

    def addItem(self, name, width, height, amount="", price="", owner_name="", barcode=""):
        """add item to warehouse"""
        if barcode == "":
            barcode = random.randint(100000000, 999999999)
            while self.barExists(barcode):
                barcode = random.randint(100000000, 999999999)
        print("trying to add item width: ", width, ", height: ", height, ", Barcode: ", barcode)
        fits = self.p.addItem((width), (height), barcode)
        if not fits:
            return False
        else:
            locations = self.itemLocation(barcode)
            self.items.append(Item(barcode, name, width, height, amount,
                                   price, owner_name, locations))
            self.saveWarehouse()
            return True

    def itemLocation(self, barcode):
        return self.p.itemLoc(barcode)

    def barExists(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                return True
        return False

    # def warehouseNames(self):

    def saveWarehouse(self):
        fileLoc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')

        items = []
        for i in self.items:
            items.append({
                'name': i.name,
                'barcode': i.barcode,
                'width': i.width,
                'height': i.height
            })
        warehouseData = {
            'warehouseName': self.warehouseName,
            'width': self.width,
            'height': self.height,
            'items': items
        }
        loc = -1
        with open(fileLoc) as json_file:
            data = json.load(json_file)
            iter = -1
            for ware in data:
                iter += 1
                if ware['warehouseName'] == warehouseData['warehouseName']:
                    loc = iter
            if loc >= 0:
                data[loc] = warehouseData
            else:
                data.append(warehouseData)
            with open(fileLoc, 'w') as outfile:
                json.dump(data, outfile)

    # will set the warehouse to the new width and height. Then load the items into the warehouse
    def loadNewWarehouse(self, warehouseId):
        fileLoc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')
        with open(fileLoc) as json_file:
            data = json.load(json_file)
            # print(data)
            warehouseData = {}
            for p in data:
                if p['warehouseName'] == warehouseId:
                    warehouseData = p
            if warehouseData:
                self.p.loadNewWarehouse(warehouseData['width'], warehouseData['height'])
                self.width = warehouseData['width']
                self.height = warehouseData['height']
                self.items = []
                self.warehouseName = warehouseId
                for items in warehouseData['items']:
                    self.addItem(items['name'], items['width'],
                                 items['height'], barcode=items['barcode'])


    def displayMatrix(self):
        self.p.printWarehouseMatrix()

    def checkoutItem(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                item.checkout()

    def checkinItem(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                item.checkin()

class Item:
    def __init__(self, barcode, name, width, height, amount, price, owner_name, locations):

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


B = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')
print(B)
# make a warehouse, warehousePacker(width, height)

# x = WareHouse(50, 30, 'warehouse121')
# x.addItem('paper', 4, 5)
# x.displayMatrix()

# x.saveWarehouse()
# x.loadNewWarehouse('warehouse11')
# x.displayMatrix()