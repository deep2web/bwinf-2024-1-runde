import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import threading
import time
import re


# Event, um die Initialisierung von input zu signalisieren
input_initialized = threading.Event()


def sprungweite(buchstabe):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "ü", "ß"]
    return alphabet.index(buchstabe) + 1


print(sprungweite("ß"))




def GUI():
    global input
    global re_input

    app = ttk.Window(title="My Application", themename="superhero")

    b1 = ttk.Button(app, text="Button 1", bootstyle=SUCCESS)
    b1.pack(side=LEFT, padx=5, pady=10)

    b2 = ttk.Button(app, text="Button 2", bootstyle=(INFO, OUTLINE))
    b2.pack(side=LEFT, padx=5, pady=10)

    # scrolled text with autohide vertical scrollbar
    st = ScrolledText(app, padding=20, height=10, autohide=True)
    st.pack(fill=BOTH, expand=YES)
    input_initialized.set() # setzt Signal, dass Variable input initialisiert ist
    # add text
    st.insert(END, 'Insert your text here.')

    while True:
        input = st.get("1.0",END) # get the text from the text field
        re_input = re.sub('[^A-Za-zäöüÄÖÜßẞ]', '', input) # remove all non-letter characters
        app.update() # update the GUI

def Test():
    input_initialized.wait() # wartet bis input initialisiert ist
    print("Ready to test")
    while True:
        global input
        global re_input  # Deklariere re_input als global
        print(input)
        print("RE:------>")
        print(re_input)
        time.sleep(2)

def check_hopsi():
    input_initialized.wait() # wartet bis input initialisiert ist
    global re_input
    lt_re_input = re_input.split()
    while True:
        print(lt_re_input)
        for i in re_input:
            print(i)
            print(sprungweite(i))



t1 = threading.Thread(target=GUI) 
t2 = threading.Thread(target=Test)
t3 = threading.Thread(target=check_hopsi)
t1.start()
t2.start()
t3.start()


