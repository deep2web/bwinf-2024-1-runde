def read_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    n, m, k = map(int, lines[0].split())
    alle_klausuren = []
    for i in range(1, n+1):
        klausur = lines[i].replace(' ', '').split('<')
        alle_klausuren.append(klausur)
    gewuenschte_aufgaben = lines[n+1].split()
    return alle_klausuren, gewuenschte_aufgaben

def ordne_aufgaben():
    alle_klausuren, gewuenschte_aufgaben = read_data('schwierigkeiten0.txt')
    relations = []
    for klausur in alle_klausuren:
        for i in range(len(klausur)-1):
            leichter = klausur[i]
            schwerer = klausur[i+1]
            if leichter in gewuenschte_aufgaben and schwerer in gewuenschte_aufgaben:
                relations.append((leichter, schwerer))
    # Erstelle Listen für Vorgänger und Nachfolger
    vorgaenger = {aufgabe: [] for aufgabe in gewuenschte_aufgaben}
    nachfolger = {aufgabe: [] for aufgabe in gewuenschte_aufgaben}
    for leichter, schwerer in relations:
        vorgaenger[schwerer].append(leichter)
        nachfolger[leichter].append(schwerer)
    # Finde eine gute Anordnung durch topologisches Sortieren
    sortierte_aufgaben = []
    while True:
        freie_aufgaben = [aufgabe for aufgabe in gewuenschte_aufgaben if aufgabe not in sortierte_aufgaben and not vorgaenger[aufgabe]]
        if not freie_aufgaben:
            break
        for aufgabe in freie_aufgaben:
            sortierte_aufgaben.append(aufgabe)
            for nachf in nachfolger[aufgabe]:
                vorgaenger[nachf].remove(aufgabe)
    if len(sortierte_aufgaben) == len(gewuenschte_aufgaben):
        print(' '.join(sortierte_aufgaben))
    else:
        print("Keine gute Anordnung möglich.")

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    

ordne_aufgaben()

