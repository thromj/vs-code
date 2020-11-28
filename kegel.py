import math
pi = math.pi
print("Dies ist ein Volumenrechner für Kegel")
Höhe = float(input("Geben Sie die Höhe des Kegel in Centimetern ein "))
Radius = float( input("Geben Sie den Radius des Kegel in Centimetern ein "))
Vol = 1/3 * (pi * Radius ** 2) * Höhe
print("Das Volumen beträgt:", round(Vol, 2)," in Kubikcentimetern" )
input("Drücken Sie Enter um das Programm zu schließen")