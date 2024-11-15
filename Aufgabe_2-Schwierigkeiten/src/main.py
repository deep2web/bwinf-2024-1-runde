

klausur_1 = ["B", "A", "D", "F"]
klausur_2= ["D", "F", "G"]
klausur_3 =["A", "E", "D", "C"]
klausur_4 = ["G", "F", "C"]
anzahl_klausuren = 4

gesamte_aufgaben = []

gewuenschte_aufgaben = ["B", "C", "D", "E", "F"]

def ordne_aufgaben():#
    global gesamte_aufgaben # definiert gesamte_aufgaben als global
    for i in gewuenschte_aufgaben:
        if gewuenschte_aufgaben.index(i) < len(gewuenschte_aufgaben)-1: #überprüfe ob es nachfolgende Buchstaben gibt
            if i in klausur_1: #überprüfe ob der zu prüfende Buchstabe in klausur_1 enthalten ist
                for j in range(len(gewuenschte_aufgaben)-gewuenschte_aufgaben.index(i)): #wiederholt die Schleife für jeden nachfolgenden Buchstaben
                    if gewuenschte_aufgaben[gewuenschte_aufgaben.index(i)+j] in klausur_1: # überprüft ob der nachfolgende Buchstabe (nach dem zu prüfenden) in klausur_1 enthalten ist
                        if klausur_1.index(i) <= klausur_1.index(gewuenschte_aufgaben[gewuenschte_aufgaben.index(i)+j]): # überprüft ob der nachfolgende (nachdem zum ursprünglich prüfenden Buchstaben i) in klausur_1 schwerer war 
                            print("Test")
                        if not gesamte_aufgaben:
                            gesamte_aufgaben = [i]
                        else:
                            print(i)
    print(gesamte_aufgaben)

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    

ordne_aufgaben()


