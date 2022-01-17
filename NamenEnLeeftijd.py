Opnieuw = "Doorgaan"
while Opnieuw == "Doorgaan":
    Naam = input("Wat is uw naam? ")
    Leeftijd = input("Wat is uw leeftijd? ")
    if Naam == "stop":
        Opnieuw = "stop"
    elif Leeftijd == "stop":
        Opnieuw = "stop"
    else:
        def VolledigeNaam(Naam, Leeftijd):
            print("Hallo",Naam,"Je leeftijd is",Leeftijd,"jaar oud.")

        VolledigeNaam(Naam, Leeftijd)