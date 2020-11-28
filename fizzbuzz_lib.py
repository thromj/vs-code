def fizzbuzz(n): 
    output = ""                                     #Ausgabevariable leer vergeben
    if n % 3 == 0: output = output + "Fizz"         #Eingabeteiler 
    if n % 5 == 0: output = output + "Buzz"         #Eingabeteiler
    if output == "" : print(n)                      #Ausgabe bei irrelevanter Eingabe
    if output != "": output = output + "!"          #Ausgabevariable durch Zeichensetzung ergänzen
    print(output)                                   #Ausgabe der Variable
