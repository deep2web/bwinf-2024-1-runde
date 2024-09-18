from PIL import Image       # Image.CUBIC is deprecated (replaced by Image.BICUBIC)
Image.CUBIC = Image.BICUBIC # https://stackoverflow.com/a/76717474

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import threading
import time
import re


re_input = "" #erstelle Variable re_input
input = ""  #erstelle Variable input (notwendig da globale Variable)
abstand_endpositionen = 0 #erstelle Variable abstand_endpositionen



# Event, um die Initialisierung von input zu signalisieren
input_initialized = threading.Event()


def sprungweite(buchstabe):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "ü", "ß"]
    return alphabet.index(buchstabe) + 1





def GUI():
    global input
    global re_input

    app = ttk.Window(title="Hopsi-Checker", themename="united")

    # scrolled text with autohide vertical scrollbar
    st = ScrolledText(app, padding=20, height=10, autohide=True)
    st.pack(fill=BOTH, expand=YES)
    # input_initialized.set() # setzt Signal, dass Variable input initialisiert ist
    st.insert(END, 'Insert your text here.') # Default Text
  
    
    
    meter = ttk.Meter(
        metersize=260,
        padding=5,
        amountused=25,
        amounttotal=30,
        meterthickness=20,
        metertype="semi",
        subtext="Abstand Endpositionen",
        interactive=False,
        bootstyle="info",
        )
    meter.pack()

    #t2_check_hopsi.start() # rufe, nachdem die GUI initialisiert wurde, die Funktion zur Überprüfung des Hopsitextes auf
    while True:
        input = st.get("1.0",END) # get the text from the text field
        re_input = re.sub('[^A-Za-zäöüÄÖÜßẞ]', '', input) # remove all non-letter characters
        meter.configure(amountused = abstand_endpositionen) # Nutze Wert aus der Variable von abstand_endpositionen
        if abstand_endpositionen <= 5:
            meter.configure(bootstyle="danger")
        if abstand_endpositionen > 15:
            meter.configure(bootstyle="success")
        else:
            meter.configure(bootstyle="info")
        app.update() # update the GUI
        


def check_hopsi(Startposition):
    global abstand_endpositionen
    not_finished = True #setze Variiable not_finished auf True
    Stelle = Startposition

    while not_finished == True:
        lt_re_input = list(re_input.lower()) # Wandelt ipnut in Liste um und wandelt alle Buchstaben in Kleinbuchstaben um
        if len(lt_re_input) <= 1:
            abstand_endpositionen = 0
            time.sleep(0.5)
        else:
            if sprungweite(lt_re_input[Stelle]) + Stelle < len(lt_re_input):
                Stelle = Stelle + sprungweite(lt_re_input[Stelle])
            else:
                not_finished = False
        # #print(Stelle, lt_re_input[Stelle])

    return Stelle

def berechne_differenz(Wert1, Wert2): #Funktion zur Berechnung der Differenz von zwei positiven Werten
    if Wert1 > Wert2:
        Wert_diff = Wert1 - Wert2
    else:
        Wert_diff = Wert2 - Wert1
    return Wert_diff


def check_all():
    time.sleep(0.5)
    global abstand_endpositionen
    while True:
        time.sleep(0.1)
        check_hopsi(0)
        check_hopsi(1)
        abstand_endpositionen = berechne_differenz(check_hopsi(0), check_hopsi(1))

        # print(berechne_differenz(check_hopsi(0), check_hopsi(1)))








t1_GUI = threading.Thread(target=GUI) 
t2_check_hopsi = threading.Thread(target=check_all)
t1_GUI.start()
t2_check_hopsi.start()


