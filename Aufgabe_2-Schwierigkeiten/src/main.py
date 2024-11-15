

klausur_1 = ["B", "A", "D", "F"]
klausur_2= ["D", "F", "G"]
klausur_3 =["A", "E", "D", "C"]
klausur_4 = ["G", "F", "C"]
anzahl_klausuren = 4

gesamte_aufgaben = []

gewuenschte_aufgaben = ["B", "C", "D", "E", "F"]

def ordne_aufgaben():
        for i in gewuenschte_aufgaben:
             if gewuenschte_aufgaben.index(i) < len(gewuenschte_aufgaben)-1:
                if i in klausur_1:
                     for j in range(len(gewuenschte_aufgaben)-gewuenschte_aufgaben.index(i)):
                        if gewuenschte_aufgaben[gewuenschte_aufgaben.index(i)+j] in klausur_1:
                            if klausur_1.index(i) <= klausur_1.index(gewuenschte_aufgaben[gewuenschte_aufgaben.index(i)+j]):
                                print("Test")     


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    

ordne_aufgaben()


