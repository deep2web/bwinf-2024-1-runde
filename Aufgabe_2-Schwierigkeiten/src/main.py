import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def GUI():
    app = ttk.Window(title="Hopsi-Checker", themename="united")

    en_klausur = ttk.Entry(app, bootstyle="warning")

    en_klausur.pack(side=RIGHT, padx=5, pady=10)


    sw_klausur = ttk.Entry(app, bootstyle="warning")

    sw_klausur.pack(side=RIGHT, padx=5, pady=10)


    b1 = ttk.Button(app, text="+", bootstyle=SUCCESS)
    b1.pack(side=LEFT, padx=5, pady=10)
    

    app.mainloop()



GUI()