from PIL import Image       # Image.CUBIC is deprecated (replaced by Image.BICUBIC)
Image.CUBIC = Image.BICUBIC # https://stackoverflow.com/a/76717474

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import threading
import time
import re


re_input = "" #erstelle Variable re_input
input = "" #   erstelle Variable input (notwendig da globale Variable)

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
    
    meter = ttk.Meter(
        metersize=180,
        padding=5,
        amountused=25,
        metertype="semi",
        subtext="Abstand Endpositionen",
        interactive=True,
        )
    meter.pack()

    meter.configure(amountused = 50) #abstand_endpositione

    while True:
        input = st.get("1.0",END) # get the text from the text field
        re_input = re.sub('[^A-Za-zäöüÄÖÜßẞ]', '', input) # remove all non-letter characters
        app.update() # update the GUI


def check_hopsi(Startposition):
    not_finished = True #setze Variiable not_finished auf True
    Stelle = Startposition

    while not_finished == True:
        lt_re_input = list(re_input.lower()) # Wandelt ipnut in Liste um und wandelt alle Buchstaben in Kleinbuchstaben um
        print(lt_re_input)
        #print(sprungweite(lt_re_input[Stelle]))
            
        if sprungweite(lt_re_input[Stelle]) + Stelle < len(lt_re_input):
            Stelle = Stelle + sprungweite(lt_re_input[Stelle])
        else:
            print("Ende erreicht")
            not_finished = False
            print(Stelle, lt_re_input[Stelle])

    return Stelle

def berechne_differenz(Wert1, Wert2): #Funktion zur Berechnung der Differenz von zwei positiven Werten
    if Wert1 > Wert2:
        Wert_diff = Wert1 - Wert2
    else:
        Wert_diff = Wert2 - Wert1
    return Wert_diff


def check_all():
    while True:
        time.sleep(0.5)
        check_hopsi(0)
        check_hopsi(1)
        abstand_endpositionen = berechne_differenz(check_hopsi(0), check_hopsi(1))
        # print(berechne_differenz(check_hopsi(0), check_hopsi(1)))








t1 = threading.Thread(target=GUI) 
#t2 = threading.Thread(target=Test)
t3 = threading.Thread(target=check_all)
t1.start()
#t2.start()
t3.start()


