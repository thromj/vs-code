#test
from fizzbuzz_lib import fizzbuzz
Count = 0                                           #Zählervariable für Anzahl der durchgeführten Eingaben
failcount = 0                                       #Zähler für falsche Eingaben
regeln = "Geben Sie eine ganze (natürliche) Zahl ein. Wenn diese Zahl durch drei teilbar ist erscheint 'Fizz!', \nsollte die Zahl durch fünf teilbar sein, erscheint 'Buzz!'. Trifft beides zu erscheint 'FizzBuzz!'."

print("FizzBuzz!")                                  #Spielüberschrift
while Count <=10 :                                  #Erstellung eines Loops für die Anzahl der erlaubten Eingaben
    if Count < 1 :
        f = input("Geben Sie eine Zahl ein oder schreiben Sie Spiel um das Spiel erklärt zu bekommen:")           #Aufforderung zur Eingabe einer Spielzahl oder Aufruf der Erklärung
    else :                                          
        f = input("Geben Sie eine Zahl ein:")       #Aufforderung nach dem ersten Spielzug
    Count = Count +1                                #Zähler für Anzahl der Eingaben
    if f == "Imran Ghory" :                         #Cheatcode setzt Terminator, Eingabe und Fehlerzähler auf null.
        Count = 1
        f = 0
        failcount = 0
    if f == "" :                                    #Reaktion auf leere Eingaben
        print("Sie müssen eine natürliche Zahl eingeben um FizzBuzz zu spielen: z.B. 15 dann passiert das hier:")
        f = 15
        Count = 0
        failcount = failcount +1                    #Fehlerzähler wird um eins erhöht
    if f == "Spiel" :                               #Gibt die Regeln aus
        print(regeln, "\nViel Spaß beim ausprobieren:")
        f = input("Geben Sie jetzt ihre Zahl ein:")
        failcount = 0
    fizzbuzz(int(f))                                #Ausführung des FizzBuzz spiels anhand der Eingabe
    if failcount >= 5 :                             #Fehlerzähler zu hoch Ruft regel auf
        print("Sie sollten sich die Spielregel nocheinmal genau durchlesen:\n")
        print(regeln)
        failcount = 3
    if Count == 10:                                 #Zähler erreicht Maximum 
        break                                       #Terminierung des Programm
print("\nGenug für jetzt, schreib lieber eine Kurzbiografie!")        
input("\nSchließen mit Enter...")