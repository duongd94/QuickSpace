# TODO: 
# Remove label backgrounds
# Rearrange submit button in warehouseInfo
# Rename variables to more 'meaningful' names

import sys
import tkinter as tk
import tkinter.ttk as ttk


def run_gui():
    app = testApp()
    app.mainloop()


class testApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (welcomePage, warehouseInfo, menu, addItem, addItemSuccess, addItemFail, removeItem, removeItemSuccess, viewWarehouse):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("welcomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


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

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.083, rely=0.183, height=146, width=409)
        self.Label1.configure(font="-family {Segoe UI} -size 18")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Welcome to the Warehouse''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.396, rely=0.633, height=43, width=96)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Continue''')
        self.Button1.configure(command=lambda: controller.show_frame("warehouseInfo"))


class warehouseInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        controller.geometry("480x600+858+189")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.Label1 = tk.Label(self)
        self.Label1.place(x=20, y=60, height=36, width=455)
        self.Label1.configure(font="-family {Segoe UI} -size 13")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Please enter the dimensions of the warehouse (ft.):''')

        self.Button1 = tk.Button(self)
        self.Button1.place(x=200, y=420, height=33, width=79)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(command=lambda: controller.show_frame("menu"))

        self.Label5 = tk.Label(self)
        self.Label5.place(relx=0.021, y=465, height=34, width=462)
        self.Label5.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''-------------------------- OR --------------------------''')

        self.Label3 = tk.Label(self)
        self.Label3.place(x=50, y=360, height=34, width=64)
        self.Label3.configure(anchor='e')
        self.Label3.configure(font="-family {Segoe UI} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Width:''')

        self.Label4 = tk.Label(self)
        self.Label4.place(x=50, y=245, height=34, width=69)
        self.Label4.configure(anchor='e')
        self.Label4.configure(font="-family {Segoe UI} -size 12")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Height:''')

        self.Label2 = tk.Label(self)
        self.Label2.place(x=50, y=135, height=34, width=70)
        self.Label2.configure(anchor='e')
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Length:''')

        self.Entry1 = tk.Entry(self)
        self.Entry1.place(x=150, y=140, height=24, width=270)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="-family {Courier New} -size 11")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1_2 = tk.Entry(self)
        self.Entry1_2.place(x=150, y=250, height=24, width=270)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="-family {Courier New} -size 11")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        self.Entry1_4 = tk.Entry(self)
        self.Entry1_4.place(x=150, y=365, height=24, width=270)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(disabledforeground="#a3a3a3")
        self.Entry1_4.configure(font="-family {Courier New} -size 11")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="#c4c4c4")
        self.Entry1_4.configure(selectforeground="black")

        self.TCombobox1 = ttk.Combobox(self)
        self.TCombobox1.place(x=100, y=520, relheight=0.045, relwidth=0.573)
        self.TCombobox1['values'] = ('Warehouse A', 'Warehouse B', 'Warehouse C')
        self.TCombobox1.set('Saved Warehouses')


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

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.313, rely=0.067, height=95, width=177)
        self.Label1.configure(font="-family {Segoe UI} -size 40")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Menu''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.354, rely=0.333, height=52, width=150)
        self.Button1.configure(font="-family {Segoe UI} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Item''')
        self.Button1.configure(command=lambda: controller.show_frame("addItem"))

        self.Button1_1 = tk.Button(self)
        self.Button1_1.place(relx=0.354, rely=0.517, height=52, width=150)
        self.Button1_1.configure(font="-family {Segoe UI} -size 11")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Remove Item''')
        self.Button1_1.configure(command=lambda: controller.show_frame("removeItem"))

        self.Button1_2 = tk.Button(self)
        self.Button1_2.place(relx=0.354, rely=0.7, height=52, width=150)
        self.Button1_2.configure(font="-family {Segoe UI} -size 11")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''View Warehouse''')
        self.Button1_2.configure(command=lambda: controller.show_frame("viewWarehouse"))


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

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.313, rely=0.133, height=51, width=185)
        self.Label1.configure(font="-family {Segoe UI} -size 20")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Adding Item''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.125, rely=0.325, height=34, width=62)
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Name:''')

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.125, rely=0.5, height=34, width=50)
        self.Label3.configure(font="-family {Segoe UI} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Size:''')

        self.Label4_1 = tk.Label(self)
        self.Label4_1.place(relx=0.396, rely=0.5, height=26, width=13)
        self.Label4_1.configure(font="-family {Segoe UI} -size 12")
        self.Label4_1.configure(foreground="#000000")
        self.Label4_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1.configure(highlightcolor="black")
        self.Label4_1.configure(text='''x''')

        self.Label5 = tk.Label(self)
        self.Label5.place(relx=0.813, rely=0.5, height=34, width=23)
        self.Label5.configure(font="-family {Segoe UI} -size 12")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''ft.''')

        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.25, rely=0.5, height=34, relwidth=0.113)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 12")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.396, rely=0.7, height=43, width=106)
        self.Button1.configure(font="-family {Segoe UI} -size 12")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Item''')
        self.Button1.configure(command=lambda: controller.show_frame("addItemSuccess"))

        self.Entry1_2 = tk.Entry(self)
        self.Entry1_2.place(relx=0.458, rely=0.5, height=34, relwidth=0.113)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="-family {Courier New} -size 12")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        self.Entry1_3 = tk.Entry(self)
        self.Entry1_3.place(relx=0.667, rely=0.5, height=34, relwidth=0.113)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font="-family {Courier New} -size 12")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="#c4c4c4")
        self.Entry1_3.configure(selectforeground="black")

        self.Label4_2 = tk.Label(self)
        self.Label4_2.place(relx=0.604, rely=0.5, height=26, width=13)
        self.Label4_2.configure(font="-family {Segoe UI} -size 12")
        self.Label4_2.configure(foreground="#000000")
        self.Label4_2.configure(highlightbackground="#d9d9d9")
        self.Label4_2.configure(highlightcolor="black")
        self.Label4_2.configure(text='''x''')

        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.292, rely=0.325, height=34, relwidth=0.529)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 12")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")


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

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.042, rely=0.233, height=60, width=442)
        self.Label1.configure(font="-family {Segoe UI} -size 24")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Item Successfully added!''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.167, rely=0.383, height=34, width=327)
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Would you like to add another item?''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.292, rely=0.533, height=35, width=70)
        self.Button1.configure(font="-family {Segoe UI} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Yes''')
        self.Button1.configure(command=lambda: controller.show_frame("addItem"))

        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.583, rely=0.533, height=35, width=70)
        self.Button2.configure(font="-family {Segoe UI} -size 11")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''No''')
        self.Button2.configure(command=lambda: controller.show_frame("menu"))


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

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.375, rely=0.117, height=60, width=108)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Sorry!''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.146, rely=0.25, height=51, width=319)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 20")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''There is only [x] sq. ft.''')

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.021, rely=0.35, height=51, width=453)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 20")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''left available in the warehouse.''')

        self.Label4 = tk.Label(self)
        self.Label4.place(relx=0.104, rely=0.45, height=51, width=384)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 20")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Try removing an item first.''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.417, rely=0.65, height=52, width=80)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 14")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=lambda: controller.show_frame("menu"))


class removeItem(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        controller.geometry("480x600+650+150")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.146, rely=0.117, height=53, width=344)
        self.Label1.configure(font="-family {Segoe UI} -size 21")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Select item to remove''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.354, rely=0.783, height=45, width=150)
        self.Button1.configure(font="-family {Segoe UI} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Remove Selected''')
        self.Button1.configure(command=lambda: controller.show_frame("removeItemSuccess"))

        self.ListBox2 = tk.Listbox(self)
        self.Scrollbar2 = tk.Scrollbar(self.ListBox2, orient="vertical")
        self.Scrollbar2.pack(side="right", fill="y")
        self.ListBox2.config(yscrollcommand=self.Scrollbar2.set)
        self.ListBox2.place(x=110, y=160, height=260, width=275)
        self.Scrollbar2.config(command=self.ListBox2.yview)

        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")
        self.ListBox2.insert("end", "item a")


class removeItemSuccess(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        controller.geometry("480x600+650+150")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.042, rely=0.233, height=60, width=442)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 22")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Item Successfully removed!''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.125, rely=0.383, height=34, width=367)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Would you like to remove another item?''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.292, rely=0.533, height=35, width=70)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Yes''')
        self.Button1.configure(command=lambda: controller.show_frame("removeItem"))

        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.583, rely=0.533, height=35, width=70)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 11")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''No''')
        self.Button2.configure(command=lambda: controller.show_frame("menu"))


class viewWarehouse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        controller.geometry("480x600+667+287")
        controller.title("Quick-Space")
        controller.configure(background="#d9d9d9")
        controller.configure(highlightbackground="#d9d9d9")
        controller.configure(highlightcolor="black")

        self.Label1_1 = tk.Label(self)
        self.Label1_1.place(relx=0.167, rely=0.033, height=56, width=331)
        self.Label1_1.configure(font="-family {Segoe UI} -size 22")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Items in Warehouse''')

        self.Label2_2 = tk.Label(self)
        self.Label2_2.place(relx=0.208, rely=0.383, height=37, width=279)
        self.Label2_2.configure(font="-family {Segoe UI} -size 14")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Total Space Used: [x] sq. ft.''')

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.146, rely=0.45, height=37, width=337)
        self.Label3.configure(font="-family {Segoe UI} -size 14")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Total Space Remaining: [x] sq. ft.''')

        self.Label4 = tk.Label(self)
        self.Label4.place(relx=0.292, rely=0.517, height=37, width=202)
        self.Label4.configure(font="-family {Segoe UI} -size 14")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Current Warehouse''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.438, rely=0.917, height=33, width=56)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=lambda: controller.show_frame("menu"))

        # Might need to be edited in order to include 'headers' like "Name" "Size (l x w x h)" "Location (x,y)"

        self.ListBox2 = tk.Listbox(self)
        self.Scrollbar2 = tk.Scrollbar(self.ListBox2, orient="vertical")
        self.Scrollbar2.pack(side="right", fill="y")
        self.ListBox2.config(yscrollcommand=self.Scrollbar2.set)
        self.ListBox2.place(x=60, y=90, height=124, width=365)
        self.Scrollbar2.config(command=self.ListBox2.yview)

        # Draw warehouse diagram here


if __name__ == '__main__':
    run_gui()
