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
        for F in (welcomePage, warehouseInfo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("welcomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        print("CHANGING")
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
        self.Button1.configure(command=lambda: controller.show_frame("welcomePage"))

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


if __name__ == '__main__':
    run_gui()
