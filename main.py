# Lohnberechner

#Er soll den User abfragen, welche Eingabe er haben will.

Auswahl=input("Mit welchem Wert möchten Sie rechnen? Geben Sie eine der folgenden Zahlen ein für: 1: Stundenlohn. 2: Tageslohn. 3: Wochenlohn. 4: Monatslohn. 5: Jahreslohn\n")

# print(type (Auswahl)) Zahlen in Auswahl sind string, da die Zahlen in der input Frage ebenfalls ein string sind

if(Auswahl=="1"):
    stundenlohn = input("Wie Geld verdienen Sie pro Stunde ")
    tageslohn = float(stundenlohn) *8
    wochenlohn = tageslohn * 5
    monatslohn = wochenlohn * 4
    jahreslohn = monatslohn * 12
    print("Sie verdienen " + str(tageslohn) + " am Tag")
    print("Sie verdienen " + str(wochenlohn) + " in der Woche")
    print("Sie verdienen " + str(monatslohn) + " im Monat")
    print("Sie verdienen " + str(jahreslohn) + " im Jahr")

elif (Auswahl=="2"):
    tageslohn = input("Wie viel Geld verdienen Sie am Tag? ")
    stundenlohn = float (tageslohn) / 8
    wochenlohn = float (tageslohn) * 5
    monatslohn = wochenlohn * 4
    jahreslohn = monatslohn * 12
    print("Sie verdienen " + str(stundenlohn) + " in der Stunde")
    print("Sie verdienen " + str(wochenlohn) + " in der Woche")
    print("Sie verdienen " + str(monatslohn) + " im Monat")
    print("Sie verdienen " + str(jahreslohn) + " im Jahr")

elif (Auswahl=="3"):
    wochenlohn = input ("Wie viel Geld verdienen Sie in der Woche? ")
    tageslohn = float (wochenlohn) / 5
    stundenlohn = tageslohn / 8
    monatslohn = float (wochenlohn) * 4
    jahreslohn = monatslohn * 12
    print("Sie verdienen " + str(stundenlohn) + " in der Stunde")
    print("Sie verdienen " + str(tageslohn) + " am Tag")
    print("Sie verdienen " + str(monatslohn) + " im Monat")
    print("Sie verdienen " + str(jahreslohn) + " im Jahr")

elif (Auswahl=="4"):
    monatslohn = input ("Wie viel Geld verdienen Sie im Monat? ")
    wochenlohn = float (monatslohn) / 4
    tageslohn = wochenlohn / 5
    stundenlohn = tageslohn / 8
    jahreslohn = float (monatslohn) * 12
    print("Sie verdienen " + str(stundenlohn) + " in der Stunde")
    print("Sie verdienen " + str(tageslohn) + " am Tag")
    print("Sie verdienen " + str(wochenlohn) + " in der Woche")
    print("Sie verdienen " + str(jahreslohn) + " im Jahr")

elif (Auswahl=="5"):
    jahreslohn = input("Wie viel Geld verdienen Sie im Jahr? ")
    monatslohn = float (jahreslohn) / 12
    wochenlohn = monatslohn / 4
    tageslohn = wochenlohn / 5
    stundenlohn = tageslohn / 8
    print("Sie verdienen " + str(stundenlohn) + " in der Stunde")
    print("Sie verdienen " + str(tageslohn) + " am Tag")
    print("Sie verdienen " + str(wochenlohn) + " in der Woche")
    print("Sie verdienen " + str(monatslohn) + " im Monat")

else:
    print ("Ungültige Eingabe. Bitte nur die Zahlen 1 bis 5 benutzen.")




