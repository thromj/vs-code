#jt231 Jonathan Throm
#ob83 Ole Brehm
#rf119 Raphael Franzke

Sp1 = ""
Sp2 = ""
Sp = ""
mde = 0

def höhle() :
    print("\n<Stehen vor einer Spalte im Fels> \n\nWilli: Diese kalte Luft die immer aus diesen Höhlen kommt...")
    if  input("\nWilli: Kannst du mir sagen wie die Höhle heist?(****** Cave(8 Buchstaben))") == "Colossal" :
        print("\nWilli: Ohh wenn du das weist, weist du bestimmt auch wer ich wirklich bin. \nWilli: Ich hoffe es ist okay das ich dir Don's und mein Hobby verschwiegen hab")
    else :
        print("\nWilli: Hmm ich glaub das war es nicht.. Na egal ")

def gewinnen() :
    print("\nWilli: Nachdem sich die Wege wiedervereinigt haben findet sich dort eine Tür, wir öffnen die Tür und finden dort Don wie er Colossal Cave spielt.")
    if bool(Sp1) == False :
        print("\n\n<GRATULATION",Sp, ", du hast es geschafft!>")
    else :
        print("\n\n<GRATULATION, ihr habt es geschafft!>")

def ende() :
    input("Drücke Enter um das Spiel zu beenden...")

print("Jumantipython")
print("\nDas ultimative Adventuregame egal ob alleine oder zu zweit")
if input("\nSpielst du alleine?(Ja/Nein) ") == "Nein":
    Sp1 = input("\nGebe den Name des ersten Spielers ein:")
    Sp2 = input("\nGebe den Name des zweiten Spielers ein:")
else :
    Sp = input("\nGebe deinen Namen ein:")
mde = input("\nWähle als nächstes den Schwierigkeitsgrad:(1/2/3) ")
if int(mde) < 3 :
    print("\nPahh... hast du etwa Angst vor der Herausforderung? Ich denk mit schwer liegst du ganz gut.")
else :
    print("\nSehr gut! Ich freue mich auf ein neues Abenteur mit dir. Nicht jeder hat den Mut direkt schwer zu wählen.")
print("\nOh jetzt hätte ich fast vergessen mich vorzustellen...\nMein Name ist William Crowther, aber meine Freunde und hoffentlich auch Du nennen mich einfach Willi.")
if input("\nWilli: Hab ich dir bereits erzählt weshalb ich deine Hilfe brauche?(Ja/Nein) ") == "Nein":
    print("\nWilli: Okay gut dann will ich dir das kurz erzählen.\nWilli: Mein guter Freud Don Woods ist verschwunden und ich hoffe du kannst mir helfen ihn zu finden.")
else :
    print("\nWilli: Dann lass uns losgehen!")
if input("\nWilli: Don ist meistens im Wald oder in den höhlen am Berg was meinst du wo sollen wir als erstes nachschauen?(Wald/Höhle)") == "Wald":
    print("\nWilli: Ich bin ja echt nicht gerne im Wald, ich kann Don nicht verstehen wie man sich gerne hier aufhält...\n <Knacksnedes Geräusch> \nWilli: Was war das?" )
    if input("\nWilli: Hast du das auch gehört?(Ja/Nein) ") == "Ja":
        if input("\nWilli: Sollten wir nicht besser wieder zurück?(Ja/Quatsch) ") == "Quatsch" :
            print("\nWilli: ",Sp,"wenn du dir so sicher bist fühl ich mich schon viel wohler.")
            print("\nWilli: Ich glaube wir haben den ganzen Wald durchsucht, wir müssen also doch in der höhle nachschauen.")
            höhle()
        else:
            höhle()
    else :
        print("\nWilli: Ah okay dann war das wohl nur Einbildung.\nWilli: Ich glaube wir haben den ganzen Wald durchsucht, wir müssen also doch in der Höhle nachschauen.")
        höhle()
else :
    höhle()
print("\nWilli: Lass uns in die Höhle gehen vielleicht finden wir Don ja dort.")
print("\n<Wir stehen vor einer Weggabelung>\n\n")
if bool(Sp1) == False :
    if input("Möchtest du links oder rechts gehen ?(Links/Rechts)") == "Links" :
        print("\n Willi: Okay dann lass uns links gehen.")
        print("\n Willi: Nach hundert Metern führen die Wege wieder zusammen.")
    else :
        print("\n Willi: Okay dann lass uns rechts gehen")
        print("\n Willi: Nach hundertfünfzig Metern führen die Wege wieder zusammen.")
    gewinnen()
else:
    resp = input("Willi: Möchtet ihr nach links, rechts oder euch aufteilen?(Links/Rechts/Aufteilen)")
    if  resp == "Links":
        print("\n Willi: Okay dann lass uns links gehen.")
        print("\n Willi: Nach hundert Metern führen die Wege wieder zusammen.")
        gewinnen()
    elif resp == "Rechts" :
        print("\n<Es tut mir leid der folgende Kontent ist nur für Premiumnutzer verfügbar.>")
    else :
        print("\n<",Sp1," geht nach links, ",Sp2," geht nach rechts>")
        print("\nWilli: Ich gehe mit ",Sp1," .")
        if input("\Willi: Da vorne kommt etwas, wollen wir weiter gehen oder zurück ?(Weiter/Zurück)") == "Weiter":
            print("\n<Wir treffen auf ",Sp2,">")
            gewinnen()
        else :
            print("\n Willi: Wir haben Don leider nicht gefunden versuchen wir es ein ander mal. ")
            print("\n\n Das Spiel ist beendet")
ende()            