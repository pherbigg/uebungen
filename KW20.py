'''import os, os.path

for element in os.listdir():
    if os.path.isfile(element):
        (dateiname, endung) = os.path.splitext(element)
        print(endung)'''

#Aufgabe 1: Finden Sie den am meisten vorkommenden Datei-Typ in Ihrem Verzeichnis raus und geben Sie die Anzahl der Dateien mit diesem Dateityp an die Console aus
import os, os.path
dateiendung = {}
for element in os.listdir():
    if os.path.isfile(element):
        (dateiname, endung) = os.path.splitext(element)
        if endung not in dateiendung:
            dateiendung[endung] = []

        dateiliste = dateiendung[endung]
        dateiliste.append(endung)
    #   print(dateiname)
counter = 0
maxexternsoin = None
for eintrag in dateiendung:
    if len(eintrag) > counter:
        counter = len(eintrag)
        maxexternsoin = eintrag
#print(maxexternsoin)



#Aufgabe 2: Erstellen Sie eine alphabetisch sortierte Liste aller Unterverzeichnisse des aktuellen Verzeichnisses (benutzen Sie dafür die Methode list.sort)

unterverzichnisse = os.listdir()

folders = []

for element in unterverzichnisse:
    if not os.path.isfile(element):
        folders.append(element)

folders.sort(reverse= True)

print(folders)

print(unterverzichnisse)

#Aufgabe 3: Schreiben Sie eine Funktion, die, je nach Parameter, entweder alle Dateien ODER alle Unterverzeichnisse eines durch Parameter angegebenen Verzeichnisses als alphabetisch sortierte Liste zurückgibt.

def get_sorted_list(getFiles):
    elements = os.listdir()
    sortedElements = []
    for element in elements:
        if os.path.isfile(element):
            if getFiles:
                sortedElements.append(element)
        if not os.path.isfile(element) and not getFiles:
                sortedElements.append(element)
    
    print(sortedElements)

get_sorted_list(getFiles=False)