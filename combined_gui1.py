# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:19:32 2019

@author: aksha
"""
import os
from pathlib import Path
import sys
import tkinter as tk
import tkinter.ttk as ttk
import items
from tkinter import Canvas
import json

def run_gui():
    app = warehouseApp()
    app.mainloop()

class warehouseApp(tk.Tk):
    # Frame change reference https://pythonprogramming.net/change-show-new-frame-tkinter/
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (welcomePage, warehouseInfo, menu, addItem, addItemSuccess, addItemFail, addItemFail1, viewWarehouse):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("welcomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def exit_app(self):
        self.destroy()


class welcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        controller.geometry("480x600+467+263")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.welcomeLabel = tk.Label(self)
        self.welcomeLabel.place(relx=0.083, rely=0.183, height=146, width=409)
        self.welcomeLabel.configure(font="-family {Segoe UI} -size 18")
        self.welcomeLabel.configure(foreground="#000000")
        self.welcomeLabel.configure(highlightbackground="#d9d9d9")
        self.welcomeLabel.configure(highlightcolor="black")
        self.welcomeLabel.configure(text='''Welcome to the Warehouse''')

        self.continueButton = tk.Button(self)
        self.continueButton.place(relx=0.396, rely=0.633, height=43, width=96)
        self.continueButton.configure(activebackground="#ececec")
        self.continueButton.configure(activeforeground="#000000")
        self.continueButton.configure(background="#d9d9d9")
        self.continueButton.configure(disabledforeground="#a3a3a3")
        self.continueButton.configure(foreground="#000000")
        self.continueButton.configure(highlightbackground="#d9d9d9")
        self.continueButton.configure(highlightcolor="black")
        self.continueButton.configure(pady="0")
        self.continueButton.configure(text='''Continue''')
        self.continueButton.configure(command=lambda: controller.show_frame("warehouseInfo"))


class warehouseInfo(tk.Frame):
    warehouse=None
    wareHeight=0
    wareWidth=0
    updateFlag = False
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        controller.geometry("480x600+858+189")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        def getitem():
            warehouseInfo.updateFlag = True
            warehouseSelected = str(variable.get())
            if warehouseSelected == 'Select Warehouse':
                height=int(float(self.lengthEntry.get()))
                width=int(float(self.widthEntry.get()))
                name=str(self.nameEntry.get())
                warehouseInfo.warehouse=items.WareHouse(height,width,name)
                warehouseInfo.warehouse.saveWarehouse()
                loadNames()
            else:
                warehouseInfo.warehouse=items.WareHouse(1,1,'name')
                warehouseInfo.warehouse.loadNewWarehouse(warehouseSelected)
            controller.show_frame("menu")
            
            

        self.infoLabel = tk.Label(self)
        self.infoLabel.place(x=20, y=90, height=36, width=455) #ORIGINAL LOCATION: y=60
        self.infoLabel.configure(font="-family {Segoe UI} -size 13")
        self.infoLabel.configure(foreground="#000000")
        self.infoLabel.configure(highlightbackground="#d9d9d9")
        self.infoLabel.configure(highlightcolor="black")
        self.infoLabel.configure(text='''Please enter dimensions and name of the warehouse:''')

        self.nameLabel = tk.Label(self)
        self.nameLabel.place(x=60, y=188, height=34, width=70) #ORIGINAL LOCATION: x=50, y=135
        self.nameLabel.configure(anchor='e')
        self.nameLabel.configure(font="-family {Segoe UI} -size 12")
        self.nameLabel.configure(foreground="#000000")
        self.nameLabel.configure(highlightbackground="#d9d9d9")
        self.nameLabel.configure(highlightcolor="black")
        self.nameLabel.configure(text='''Name:''')

        self.lengthLabel = tk.Label(self)
        self.lengthLabel.place(x=65, y=248, height=34, width=79) #ORIGINAL LOCATION: x=50, y=135
        self.lengthLabel.configure(anchor='e')
        self.lengthLabel.configure(font="-family {Segoe UI} -size 12")
        self.lengthLabel.configure(foreground="#000000")
        self.lengthLabel.configure(highlightbackground="#d9d9d9")
        self.lengthLabel.configure(highlightcolor="black")
        self.lengthLabel.configure(text='''Length (ft.):''')

        self.widthLabel = tk.Label(self)
        self.widthLabel.place(x=65, y=308, height=34, width=76) #ORIGINAL LOCATION: x=50, y=245
        self.widthLabel.configure(anchor='e')
        self.widthLabel.configure(font="-family {Segoe UI} -size 12")
        self.widthLabel.configure(foreground="#000000")
        self.widthLabel.configure(highlightbackground="#d9d9d9")
        self.widthLabel.configure(highlightcolor="black")
        self.widthLabel.configure(text='''Width (ft.):''')

        self.nameEntry = tk.Entry(self)
        self.nameEntry.place(x=150, y=195, height=24, width=270) #ORIGINAL LOCATION: x=150, y=140
        self.nameEntry.configure(background="white")
        self.nameEntry.configure(font="-family {Courier New} -size 11")
        self.nameEntry.configure(foreground="#000000")
        self.nameEntry.configure(highlightbackground="#d9d9d9")
        self.nameEntry.configure(highlightcolor="black")
        self.nameEntry.configure(insertbackground="black")
        self.nameEntry.configure(selectbackground="#c4c4c4")
        self.nameEntry.configure(selectforeground="black")

        self.lengthEntry = tk.Entry(self)
        self.lengthEntry.place(x=150, y=255, height=24, width=270) #ORIGINAL LOCATION: x=150, y=140
        self.lengthEntry.configure(background="white")
        self.lengthEntry.configure(font="-family {Courier New} -size 11")
        self.lengthEntry.configure(foreground="#000000")
        self.lengthEntry.configure(highlightbackground="#d9d9d9")
        self.lengthEntry.configure(highlightcolor="black")
        self.lengthEntry.configure(insertbackground="black")
        self.lengthEntry.configure(selectbackground="#c4c4c4")
        self.lengthEntry.configure(selectforeground="black")

        self.widthEntry = tk.Entry(self)
        self.widthEntry.place(x=150, y=315, height=24, width=270) #ORIGINAL LOCATION: x=150, y=250
        self.widthEntry.configure(background="white")
        self.widthEntry.configure(disabledforeground="#a3a3a3")
        self.widthEntry.configure(font="-family {Courier New} -size 11")
        self.widthEntry.configure(foreground="#000000")
        self.widthEntry.configure(highlightbackground="#d9d9d9")
        self.widthEntry.configure(highlightcolor="black")
        self.widthEntry.configure(insertbackground="black")
        self.widthEntry.configure(selectbackground="#c4c4c4")
        self.widthEntry.configure(selectforeground="black")

        self.submitButton = tk.Button(self)
        self.submitButton.place(x=190, y=480, height=33, width=79) #ORIGINAL LOCATION: x=200, y=420 ;; x=200, y=535
        self.submitButton.configure(activebackground="#ececec")
        self.submitButton.configure(activeforeground="#000000")
        self.submitButton.configure(background="#d9d9d9")
        self.submitButton.configure(disabledforeground="#a3a3a3")
        self.submitButton.configure(foreground="#000000")
        self.submitButton.configure(highlightbackground="#d9d9d9")
        self.submitButton.configure(highlightcolor="black")
        self.submitButton.configure(pady="0")
        self.submitButton.configure(text='''Submit''')
        self.submitButton.configure(command=getitem)
        #elf.submitButton.configure(command=lambda: controller.show_frame("menu"))

        self.orLabel = tk.Label(self)
        self.orLabel.place(x=98, y=360, height=34, width=200) #ORIGINAL LOCATION: x=50, y=245
        self.orLabel.configure(anchor='e')
        self.orLabel.configure(font="-family {Segoe UI} -size 12")
        self.orLabel.configure(foreground="#000000")
        self.orLabel.configure(highlightbackground="#d9d9d9")
        self.orLabel.configure(highlightcolor="black")
        self.orLabel.configure(text='''Or load Warehouse''')

        # get warehouseNames
        fileLoc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')
        with open(fileLoc) as json_file:
            names = [
                'Select Warehouse'
            ]
            data = json.load(json_file)
            for d in data:
                names.append(d['warehouseName'])
            variable = tk.StringVar(self)
            variable.set(names[0]) # default value
            w = tk.OptionMenu(self, variable, *names)
            w.place(x=120, y=390, height=33, width=200)
            def loadNames():
                w['menu'].add_command(label=warehouseInfo.warehouse.warehouseName, command=tk._setit(variable, warehouseInfo.warehouse.warehouseName))



class menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        controller.geometry("480x600+774+269")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")
        
        def view1():
            controller.show_frame("viewWarehouse")

        self.menuLabel = tk.Label(self)
        self.menuLabel.place(relx=0.313, rely=0.067, height=95, width=177)
        self.menuLabel.configure(font="-family {Segoe UI} -size 40")
        self.menuLabel.configure(foreground="#000000")
        self.menuLabel.configure(highlightbackground="#d9d9d9")
        self.menuLabel.configure(highlightcolor="black")
        self.menuLabel.configure(text='''Menu''')

        self.addButton = tk.Button(self)
        self.addButton.place(relx=0.354, rely=0.33, height=52, width=150)
        self.addButton.configure(activebackground="#ececec")
        self.addButton.configure(activeforeground="#000000")
        self.addButton.configure(background="#d9d9d9")
        self.addButton.configure(disabledforeground="#a3a3a3")
        self.addButton.configure(font="-family {Segoe UI} -size 11")
        self.addButton.configure(foreground="#000000")
        self.addButton.configure(highlightbackground="#d9d9d9")
        self.addButton.configure(highlightcolor="black")
        self.addButton.configure(pady="0")
        self.addButton.configure(text='''Add Item''')
        self.addButton.configure(command=lambda: controller.show_frame("addItem"))
        
        

        self.viewButton = tk.Button(self)
        self.viewButton.place(relx=0.354, rely=0.45, height=52, width=150)
        self.viewButton.configure(activebackground="#ececec")
        self.viewButton.configure(activeforeground="#000000")
        self.viewButton.configure(background="#d9d9d9")
        self.viewButton.configure(disabledforeground="#a3a3a3")
        self.viewButton.configure(font="-family {Segoe UI} -size 11")
        self.viewButton.configure(foreground="#000000")
        self.viewButton.configure(highlightbackground="#d9d9d9")
        self.viewButton.configure(highlightcolor="black")
        self.viewButton.configure(pady="0")
        self.viewButton.configure(text='''View Warehouse''')
        self.viewButton.configure(command=view1)
        #self.viewButton.configure(command=lambda: controller.show_frame("viewWarehouse"))

        self.addButton = tk.Button(self)
        self.addButton.place(relx=0.24, rely=0.69, height=52, width=250)
        self.addButton.configure(activebackground="#ececec")
        self.addButton.configure(activeforeground="#000000")
        self.addButton.configure(background="#d9d9d9")
        self.addButton.configure(disabledforeground="#a3a3a3")
        self.addButton.configure(font="-family {Segoe UI} -size 11")
        self.addButton.configure(foreground="#000000")
        self.addButton.configure(highlightbackground="#d9d9d9")
        self.addButton.configure(highlightcolor="black")
        self.addButton.configure(pady="0")
        self.addButton.configure(text='''Load another warehouse''')
        self.addButton.configure(command=lambda: controller.show_frame("warehouseInfo"))

        self.exitButton = tk.Button(self)
        self.exitButton.place(relx=0.354, rely=0.57, height=52, width=150)
        self.exitButton.configure(activebackground="#ececec")
        self.exitButton.configure(activeforeground="#000000")
        self.exitButton.configure(background="#d9d9d9")
        self.exitButton.configure(disabledforeground="#a3a3a3")
        self.exitButton.configure(font="-family {Segoe UI} -size 11")
        self.exitButton.configure(foreground="#000000")
        self.exitButton.configure(highlightbackground="#d9d9d9")
        self.exitButton.configure(highlightcolor="black")
        self.exitButton.configure(pady="0")
        self.exitButton.configure(text='''Exit''')
        self.exitButton.configure(command=lambda: controller.exit_app())


class addItem(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        controller.geometry("480x600+601+171")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")
        
        def additem1():
            
            warehouseInfo.updateFlag = True
            ilength=int(float(self.Entry1.get()))
            iwidth=int(float(self.Entry2.get()))
            iname=self.nameEntry.get()

            if warehouseInfo.warehouse.addItem(iname, iwidth, ilength):
                controller.show_frame("addItemSuccess")
            else:
                controller.show_frame("addItemFail")
            

        self.addLabel = tk.Label(self)
        self.addLabel.place(relx=0.313, rely=0.133, height=51, width=185)
        self.addLabel.configure(font="-family {Segoe UI} -size 20")
        self.addLabel.configure(foreground="#000000")
        self.addLabel.configure(highlightbackground="#d9d9d9")
        self.addLabel.configure(highlightcolor="black")
        self.addLabel.configure(text='''Adding Item''')

        self.nameLabel = tk.Label(self)
        self.nameLabel.place(x=70, rely=0.3, height=34, width=62)
        self.nameLabel.configure(font="-family {Segoe UI} -size 12")
        self.nameLabel.configure(foreground="#000000")
        self.nameLabel.configure(highlightbackground="#d9d9d9")
        self.nameLabel.configure(highlightcolor="black")
        self.nameLabel.configure(text='''Name:''')

        self.sizeLabel = tk.Label(self)
        self.sizeLabel.place(x=75, y=300, height=34, width=50)
        self.sizeLabel.configure(font="-family {Segoe UI} -size 12")
        self.sizeLabel.configure(foreground="#000000")
        self.sizeLabel.configure(highlightbackground="#d9d9d9")
        self.sizeLabel.configure(highlightcolor="black")
        self.sizeLabel.configure(text='''Size:''')

        self.xLabel = tk.Label(self)
        self.xLabel.place(x=210, y=306, height=26, width=13)
        self.xLabel.configure(font="-family {Segoe UI} -size 12")
        self.xLabel.configure(foreground="#000000")
        self.xLabel.configure(highlightbackground="#d9d9d9")
        self.xLabel.configure(highlightcolor="black")
        self.xLabel.configure(text='''x''')

        self.ftLabel = tk.Label(self)
        self.ftLabel.place(x=310, rely=0.46, height=34, width=23)
        self.ftLabel.configure(font="-family {Segoe UI} -size 12")
        self.ftLabel.configure(foreground="#000000")
        self.ftLabel.configure(highlightbackground="#d9d9d9")
        self.ftLabel.configure(highlightcolor="black")
        self.ftLabel.configure(text='''ft.''')

        self.nameEntry = tk.Entry(self)
        self.nameEntry.place(x=140, y=195, height=34, relwidth=0.529)
        self.nameEntry.configure(background="white")
        self.nameEntry.configure(disabledforeground="#a3a3a3")
        self.nameEntry.configure(font="-family {Courier New} -size 12")
        self.nameEntry.configure(foreground="#000000")
        self.nameEntry.configure(highlightbackground="#d9d9d9")
        self.nameEntry.configure(highlightcolor="black")
        self.nameEntry.configure(insertbackground="black")
        self.nameEntry.configure(selectbackground="#c4c4c4")
        self.nameEntry.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self)
        self.Entry1.place(x=140, y=300, height=34, relwidth=0.113)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 12")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = tk.Entry(self)
        self.Entry2.place(x=240, y=300, height=34, relwidth=0.113)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 12")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.addButton = tk.Button(self)
        self.addButton.place(relx=0.396, rely=0.7, height=43, width=106)
        self.addButton.configure(activebackground="#ececec")
        self.addButton.configure(activeforeground="#000000")
        self.addButton.configure(background="#d9d9d9")
        self.addButton.configure(disabledforeground="#a3a3a3")
        self.addButton.configure(font="-family {Segoe UI} -size 12")
        self.addButton.configure(foreground="#000000")
        self.addButton.configure(highlightbackground="#d9d9d9")
        self.addButton.configure(highlightcolor="black")
        self.addButton.configure(pady="0")
        self.addButton.configure(text='''Add Item''')
        self.addButton.configure(command=additem1)
        #self.addButton.configure(command=lambda: controller.show_frame("addItemSuccess"))


class addItemSuccess(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        controller.geometry("480x600+778+270")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.successLabel = tk.Label(self)
        self.successLabel.place(relx=0.042, rely=0.233, height=60, width=442)
        self.successLabel.configure(font="-family {Segoe UI} -size 24")
        self.successLabel.configure(foreground="#000000")
        self.successLabel.configure(highlightbackground="#d9d9d9")
        self.successLabel.configure(highlightcolor="black")
        self.successLabel.configure(text='''Item Successfully added!''')

        self.addMoreLabel = tk.Label(self)
        self.addMoreLabel.place(relx=0.167, rely=0.383, height=34, width=327)
        self.addMoreLabel.configure(font="-family {Segoe UI} -size 12")
        self.addMoreLabel.configure(foreground="#000000")
        self.addMoreLabel.configure(highlightbackground="#d9d9d9")
        self.addMoreLabel.configure(highlightcolor="black")
        self.addMoreLabel.configure(text='''Would you like to add another item?''')

        self.yesButton = tk.Button(self)
        self.yesButton.place(relx=0.292, rely=0.533, height=35, width=70)
        self.yesButton.configure(activebackground="#ececec")
        self.yesButton.configure(activeforeground="#000000")
        self.yesButton.configure(background="#d9d9d9")
        self.yesButton.configure(disabledforeground="#a3a3a3")
        self.yesButton.configure(font="-family {Segoe UI} -size 11")
        self.yesButton.configure(foreground="#000000")
        self.yesButton.configure(highlightbackground="#d9d9d9")
        self.yesButton.configure(highlightcolor="black")
        self.yesButton.configure(pady="0")
        self.yesButton.configure(text='''Yes''')
        self.yesButton.configure(command=lambda: controller.show_frame("addItem"))

        self.noButton = tk.Button(self)
        self.noButton.place(relx=0.583, rely=0.533, height=35, width=70)
        self.noButton.configure(activebackground="#ececec")
        self.noButton.configure(activeforeground="#000000")
        self.noButton.configure(background="#d9d9d9")
        self.noButton.configure(disabledforeground="#a3a3a3")
        self.noButton.configure(font="-family {Segoe UI} -size 11")
        self.noButton.configure(foreground="#000000")
        self.noButton.configure(highlightbackground="#d9d9d9")
        self.noButton.configure(highlightcolor="black")
        self.noButton.configure(pady="0")
        self.noButton.configure(text='''No''')
        self.noButton.configure(command=lambda: controller.show_frame("menu"))


class addItemFail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        
        controller.geometry("480x600+524+369")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.sorryLabel = tk.Label(self)
        self.sorryLabel.place(relx=0.375, rely=0.117, height=60, width=108)
        self.sorryLabel.configure(font="-family {Segoe UI} -size 24")
        self.sorryLabel.configure(foreground="#000000")
        self.sorryLabel.configure(highlightbackground="#d9d9d9")
        self.sorryLabel.configure(highlightcolor="black")
        self.sorryLabel.configure(text='''Sorry!''')

        self.remainingSpaceLabel = tk.Label(self)
        self.remainingSpaceLabel.place(relx=0.146, rely=0.25, height=51, width=319)
        self.remainingSpaceLabel.configure(font="-family {Segoe UI} -size 20")
        self.remainingSpaceLabel.configure(foreground="#000000")
        self.remainingSpaceLabel.configure(highlightbackground="#d9d9d9")
        self.remainingSpaceLabel.configure(highlightcolor="black")
        self.remainingSpaceLabel.configure(text='''There is only [x] sq. ft.''')
        

        self.leftLabel = tk.Label(self)
        self.leftLabel.place(relx=0.021, rely=0.35, height=51, width=453)
        self.leftLabel.configure(font="-family {Segoe UI} -size 20")
        self.leftLabel.configure(foreground="#000000")
        self.leftLabel.configure(highlightbackground="#d9d9d9")
        self.leftLabel.configure(highlightcolor="black")
        self.leftLabel.configure(text='''left available in the warehouse.''')


    # no longer supporting remove item
        # self.tryLabel = tk.Label(self)
        # self.tryLabel.place(relx=0.104, rely=0.45, height=51, width=384)
        # self.tryLabel.configure(font="-family {Segoe UI} -size 20")
        # self.tryLabel.configure(foreground="#000000")
        # self.tryLabel.configure(highlightbackground="#d9d9d9")
        # self.tryLabel.configure(highlightcolor="black")
        # self.tryLabel.configure(text='''Try removing an item first.''')

        self.okButton = tk.Button(self)
        self.okButton.place(relx=0.417, rely=0.65, height=52, width=80)
        self.okButton.configure(activebackground="#ececec")
        self.okButton.configure(activeforeground="#000000")
        self.okButton.configure(background="#d9d9d9")
        self.okButton.configure(disabledforeground="#a3a3a3")
        self.okButton.configure(font="-family {Segoe UI} -size 14")
        self.okButton.configure(foreground="#000000")
        self.okButton.configure(highlightbackground="#d9d9d9")
        self.okButton.configure(highlightcolor="black")
        self.okButton.configure(pady="0")
        self.okButton.configure(text='''OK''')
        self.okButton.configure(command=lambda: controller.show_frame("menu"))

class addItemFail1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        
        controller.geometry("480x600+524+369")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.sorryLabel = tk.Label(self)
        self.sorryLabel.place(relx=0.375, rely=0.117, height=60, width=108)
        self.sorryLabel.configure(font="-family {Segoe UI} -size 24")
        self.sorryLabel.configure(foreground="#000000")
        self.sorryLabel.configure(highlightbackground="#d9d9d9")
        self.sorryLabel.configure(highlightcolor="black")
        self.sorryLabel.configure(text='''Sorry!''')

        self.remainingSpaceLabel = tk.Label(self)
        self.remainingSpaceLabel.place(relx=0.146, rely=0.25, height=51, width=319)
        self.remainingSpaceLabel.configure(font="-family {Segoe UI} -size 20")
        self.remainingSpaceLabel.configure(foreground="#000000")
        self.remainingSpaceLabel.configure(highlightbackground="#d9d9d9")
        self.remainingSpaceLabel.configure(highlightcolor="black")
        self.remainingSpaceLabel.configure(text='''Name already exists!''')
        

        self.leftLabel = tk.Label(self)
        self.leftLabel.place(relx=0.021, rely=0.35, height=51, width=453)
        self.leftLabel.configure(font="-family {Segoe UI} -size 20")
        self.leftLabel.configure(foreground="#000000")
        self.leftLabel.configure(highlightbackground="#d9d9d9")
        self.leftLabel.configure(highlightcolor="black")
        self.leftLabel.configure(text='''Please choose another.''')

    # no longer supporting remove item
        # self.tryLabel = tk.Label(self)
        # self.tryLabel.place(relx=0.104, rely=0.45, height=51, width=384)
        # self.tryLabel.configure(font="-family {Segoe UI} -size 20")
        # self.tryLabel.configure(foreground="#000000")
        # self.tryLabel.configure(highlightbackground="#d9d9d9")
        # self.tryLabel.configure(highlightcolor="black")
        # self.tryLabel.configure(text='''Try removing an item first.''')

        self.okButton = tk.Button(self)
        self.okButton.place(relx=0.417, rely=0.65, height=52, width=80)
        self.okButton.configure(activebackground="#ececec")
        self.okButton.configure(activeforeground="#000000")
        self.okButton.configure(background="#d9d9d9")
        self.okButton.configure(disabledforeground="#a3a3a3")
        self.okButton.configure(font="-family {Segoe UI} -size 14")
        self.okButton.configure(foreground="#000000")
        self.okButton.configure(highlightbackground="#d9d9d9")
        self.okButton.configure(highlightcolor="black")
        self.okButton.configure(pady="0")
        self.okButton.configure(text='''OK''')
        self.okButton.configure(command=lambda: controller.show_frame("menu"))

class viewWarehouse(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        controller.geometry("480x650+667+287")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.itemsLabel = tk.Label(self)
        self.itemsLabel.place(relx=0.167, rely=0.031, height=56, width=331)
        self.itemsLabel.configure(font="-family {Segoe UI} -size 22")
        self.itemsLabel.configure(foreground="#000000")
        self.itemsLabel.configure(highlightbackground="#d9d9d9")
        self.itemsLabel.configure(highlightcolor="black")
        self.itemsLabel.configure(text='''Items in Warehouse''')

        self.spaceUsedLabel = tk.Label(self)
        self.spaceUsedLabel.place(relx=0.208, rely=0.81, height=37, width=279)
        self.spaceUsedLabel.configure(font="-family {Segoe UI} -size 14")
        self.spaceUsedLabel.configure(foreground="#000000")
        self.spaceUsedLabel.configure(highlightbackground="#d9d9d9")
        self.spaceUsedLabel.configure(highlightcolor="black")
        self.spaceUsedLabel.configure(text='''Total Space Used: [x] sq. ft.''')

        self.spaceRemainingLabel = tk.Label(self)
        self.spaceRemainingLabel.place(relx=0.146, rely=0.86, height=37, width=337)
        self.spaceRemainingLabel.configure(font="-family {Segoe UI} -size 14")
        self.spaceRemainingLabel.configure(foreground="#000000")
        self.spaceRemainingLabel.configure(highlightbackground="#d9d9d9")
        self.spaceRemainingLabel.configure(highlightcolor="black")
        self.spaceRemainingLabel.configure(text='''Total Space Remaining: [x] sq. ft.''')

        self.currentWarehouseLabel = tk.Label(self)#0.292
        self.currentWarehouseLabel.place(relx=0.292, rely=0.443, height=37, width=202)
        self.currentWarehouseLabel.configure(font="-family {Segoe UI} -size 14")
        self.currentWarehouseLabel.configure(foreground="#000000")
        self.currentWarehouseLabel.configure(highlightbackground="#d9d9d9")
        self.currentWarehouseLabel.configure(highlightcolor="black")
        self.currentWarehouseLabel.configure(text='''Current Warehouse''')

        self.okButton = tk.Button(self)
        self.okButton.place(relx=0.438, rely=0.907, height=33, width=56)
        self.okButton.configure(activebackground="#ececec")
        self.okButton.configure(activeforeground="#000000")
        self.okButton.configure(background="#d9d9d9")
        self.okButton.configure(disabledforeground="#a3a3a3")
        self.okButton.configure(foreground="#000000")
        self.okButton.configure(highlightbackground="#d9d9d9")
        self.okButton.configure(highlightcolor="black")
        self.okButton.configure(pady="0")
        self.okButton.configure(text='''OK''')
        self.okButton.configure(command=lambda: controller.show_frame("menu"))

        # Create a frame for the canvas and scrollbar(s).
        frame2 = tk.Frame(self)
        # frame2.grid(row=4, column=3, sticky=tk.NW)
        frame2.place(x=30, y=80, height=200, width=450)

        # Add a canvas in that frame.
        canvas = tk.Canvas(frame2, bg="White")
        canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(canvas, bg="#d9d9d9", bd=2)
        button = tk.Button(buttons_frame, padx=40, pady=0, relief=tk.RIDGE,
                                        text="Name")
        button.grid(row=1, column=1, sticky='news')
        button = tk.Button(buttons_frame, padx=5, pady=0, relief=tk.RIDGE,
                                        text="Length")
        button.grid(row=1, column=2, sticky='news')
        button = tk.Button(buttons_frame, padx=5, pady=0, relief=tk.RIDGE,
                                        text="Width")
        button.grid(row=1, column=3, sticky='news')
        button = tk.Button(buttons_frame, padx=15, pady=0, relief=tk.RIDGE,
                                        text="X1, Y1")
        button.grid(row=1, column=4, sticky='news')
        button = tk.Button(buttons_frame, padx=15, pady=0, relief=tk.RIDGE,
                                        text="X2, Y2")
        button.grid(row=1, column=5, sticky='news')
        button = tk.Button(buttons_frame, padx=15, pady=0, relief=tk.RIDGE,
                                        text="Barcode")
        button.grid(row=1, column=6, sticky='news')
        canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)
        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        # Define the scrollable region as entire canvas with only the desired
        dw, dh = 400, 180
        canvas.configure(scrollregion=bbox, width=dw, height=dh)
        
        
        frame=tk.Frame(self,width=400,height=180)

        frame.place(x=30, y=320)

        self.counter = 0
        # refreshed the viewWarehouse. Maybe there is a better way to do this?
        def refreshItems():
            if warehouseInfo.updateFlag:
                warehouseInfo.updateFlag = False
                # updates the space remaining and used
                spaceRemStr = "Total Space Remaining: "
                spaceRemStr += str(warehouseInfo.warehouse.remainingSpace())
                spaceRemStr += " sq. ft."
                self.spaceRemainingLabel.configure(text=spaceRemStr)
                spaceRemStr = "Total Space Used: "
                spaceRemStr += str(warehouseInfo.warehouse.usedSpace())
                spaceRemStr += " sq. ft."
                self.spaceUsedLabel.configure(text=spaceRemStr)
            
                # following updates the items
                i = 2
                # get rid of the previous items in the warehouse
                for widget1 in frame.winfo_children():
                    widget1.destroy()

                w=tk.Canvas(frame,bg='red',width=warehouseInfo.warehouse.width,height=warehouseInfo.warehouse.height,scrollregion=(0,0,warehouseInfo.warehouse.width,warehouseInfo.warehouse.height))
                hbar=tk.Scrollbar(frame,orient=tk.HORIZONTAL)
                hbar.pack(side=tk.BOTTOM,fill=tk.X)
                hbar.config(command=w.xview)
                vbar=tk.Scrollbar(frame,orient=tk.VERTICAL)
                vbar.pack(side=tk.RIGHT,fill=tk.Y)
                vbar.config(command=w.yview)

                for item in warehouseInfo.warehouse.items:
                    loc=list(warehouseInfo.warehouse.itemLocation(item.barcode))
                    w.create_rectangle(loc[0], loc[1], loc[2], loc[3], fill="blue")
                canW, canH = 400, 180
                if warehouseInfo.warehouse.width < canW:
                    canW = warehouseInfo.warehouse.width
                if warehouseInfo.warehouse.height < canH:
                    canH = warehouseInfo.warehouse.height
                
                w.config(width=canW,height=canH)
                w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
                w.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
                # rows
                for item in warehouseInfo.warehouse.items:
                    loc=list(warehouseInfo.warehouse.itemLocation(item.barcode))
                    button = tk.Button(buttons_frame, padx=0, pady=0, relief=tk.RIDGE,
                                    text=item.name)
                    button.grid(row=i, column=1, sticky='news')
                    button = tk.Button(buttons_frame, padx=0, pady=0, relief=tk.RIDGE,
                                    text=str(item.height))
                    button.grid(row=i, column=2, sticky='news')
                    button = tk.Button(buttons_frame, padx=0, pady=0, relief=tk.RIDGE,
                                    text=str(item.width))
                    button.grid(row=i, column=3, sticky='news')
                    button = tk.Button(buttons_frame, padx=0, pady=0, relief=tk.RIDGE,
                                    text="("+str(loc[0])+", "+str(loc[1])+")")
                    button.grid(row=i, column=4, sticky='news')
                    button = tk.Button(buttons_frame, padx=0, pady=0, relief=tk.RIDGE,
                                    text="("+str(loc[2])+", "+str(loc[3])+")")
                    button.grid(row=i, column=5, sticky='news')
                    button = tk.Button(buttons_frame, padx=0, pady=0, relief=tk.RIDGE,
                                    text=str(item.barcode))
                    button.grid(row=i, column=6, sticky='news')
                    i+=1
            # Create canvas window to hold the buttons_frame.
                canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)
                buttons_frame.update_idletasks()  # Needed to make bbox info available.
                bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
            # Define the scrollable region as entire canvas with only the desired
                dw, dh = 400, 180
                canvas.configure(scrollregion=bbox, width=dw, height=dh)
            clock()

        def clock():
            self.after(500, refreshItems) # run itself again after 1000 ms

        clock()

        self.addButton = tk.Button(self)#0.438
        self.addButton.place(relx=0.75, rely=0.456, height=22, width=70)
        self.addButton.configure(activebackground="#ececec")
        self.addButton.configure(activeforeground="#000000")
        self.addButton.configure(background="#d9d9d9")
        self.addButton.configure(disabledforeground="#a3a3a3")
        self.addButton.configure(font="-family {Segoe UI} -size 12")
        self.addButton.configure(foreground="#000000")
        self.addButton.configure(highlightbackground="#d9d9d9")
        self.addButton.configure(highlightcolor="black")
        self.addButton.configure(pady="0")
        self.addButton.configure(text='''Refresh''')
        self.addButton.configure(command=refreshItems)



if __name__ == '__main__':
    run_gui()