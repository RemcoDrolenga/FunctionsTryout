def Game():
    antwoord = input("Je ziet een eiland, vaar je naar het eiland toe? ja/nee ")
    match antwoord:
        case "ja":
                antwoord2 = input("Je ziet op het eiland een lang strand en een dicht begroeid bos. Ga je het bos in? ja/nee ")
                match antwoord2:
                    case "ja":
                        antwoord3 = input("Je gaat het bos in, hier kom je fel rode besjes tegen, je hebt verschrikkelijke trek. Eet je de besjes of loop je door? ja/nee ")
                        match antwoord3:
                            case "ja":
                                print("De besjes bleken giftige besjes te zijn. Je sterft door het eten van de besjes.")
                            case "nee":
                                antwoord4 = input("Je bent langs de besjes gelopen, een kleine 10 minuten later kom je een klein huisje tegen. Ga je bij het huisje naar binnen? ja/nee ")
                                match antwoord4:
                                    case "ja":
                                        antwoord5 = input("Je probeert het huisje open te maken, hij zit alleen op slot. Ga je opzoek naar de sleutel? ja/nee ")
                                        match antwoord5:
                                            case "ja":
                                                antwoord6 = input("Je kijkt bij het huisje en vind uiteindelijk geen sleutel. Je zou de deur in kunnen trappen. ja/nee ")
                                                match antwoord6:
                                                    case "ja":
                                                        print("Je trapt de deur in, dit maakt een behoorlijk lawaai. Waardoor je de aandacht trekt van een aantal inboorlingen die iets verderop in de bosjes wonen. De aanval van hun overleef je helaas niet.")
                                                    case "nee":
                                                        print("Je zoekt nog even verder en het valt je opeens op dat er een klein raampje ergens open staat, je kruipt daardoor naar binnen en komt een kaart tegen met een route naar een ander huisje verderop waar een bootje naast lijkt te liggen. Je volgt de route en je vaart je vrijheid te gemoed.")
                                            case "nee":
                                                antwoord7 = input("je vind het niet de moeite waard en loopt verder, opzoek naar een slaapplaats. je vind na een tijdje een grot. Ga je hier de nacht doorbrengen? ja/nee ")
                                                match antwoord7:
                                                    case "ja":
                                                        print("Je hebt er voor gekozen om de grot in te lopen. Hier kom je midden in de nacht een grote beer tegen..")
                                                    case "nee":
                                                        print("Je bent doorgelopen op zoek naar een andere slaapplaats, alleen kun je niks beters vinden dan een hoge boom. Je klimt in de boom en gaat liggen en zit dan oog in oog met een giftige slang.")
                                    case "nee":
                                        antwoord8 = input("Je loopt verder, en iets verderop hoor je wat geritsel in de bosjes rechts van je, ga je kijken wat er in de bosjes zit? ja/nee ")
                                        match antwoord8:
                                            case "ja":
                                                print("je gaat kijken bij het bosje, alleen in het bosje blijkt een grote tijger te zitten te zitten die je bespringt en opeet.")
                                            case "nee":
                                                antwoord9 = input("Je loopt dieper en dieper het bos in, totdat je bij een berg en een strandje. Ga je de berg omhoog? ja/nee ")
                                                match antwoord9:
                                                    case "ja":
                                                        print("Je loopt de berg op, om er vervolgens achter te komen dat er niks te zoeken is, en op je weg terug naar beneden rolt er een steen onder je voet weg en val je naar beneden.")
                                                    case "nee":
                                                        print("je komt een strandje tegen, bij het strandje staat er een huisje met een klein bootje ernaast, je loopt het huisje in om te zoeken naar wat eten en brandstof. Dit kun je allebei vinden. Je vaart weg van het eiland in het bootje.")
                    case "nee":
                        antwoord10 = input("je hebt nu al uren gelopen maar nog steeds niks eetbaars gevonden op het strand, ga je toch het bos in? ja/nee ")
                        match antwoord10:
                            case "ja":
                                antwoord11 = input("Je gaat toch maar het bos in. Hier kom je vervolgens een huisje tegen. Ga je op onderzoek uit bij het huisje? ja/nee ")
                                match antwoord11:
                                    case "ja":
                                        antwoord12 = input("Je loopt naar het huisje toe, om er vervolgens achter te komen dat de deur op slot zit, ga je rondkijken bij het huisje voor een sleutel? ja/nee ")
                                        match antwoord12:
                                            case "ja":
                                                print("Je kan geen sleutel vinden, ook is de deur te sterk om hem geforceerd te openen. Je ziet wel een hele stapel dikke stokken ernaast liggen. Je maakt hiermee een goed vlot en vaart daarmee de zee op.")
                                            case "nee":
                                                print("Je kiest ervoor om het huisje niet te inspecteren voor een sleutel. Dus je loopt verder een heuvel op. Waar je een klein vuurtorentje in de verte ziet staan. Je loopt er naar toe en daar vind je bovenin een kratje met vuurpijlen en een slaapzak. De volgende ochtend zie je een vrachtschip de horizon voorbij varen, je steekt een vuurpijl af en na een uurtje word je opgehaald met een reddingsbootje.")
                                    case "nee":
                                            antwoord13 = input("Je loopt weg van het huisje, het word al laat dus je besluit om een eigen slaapplek te maken. Gebruik je hier takken voor? ja/nee ")
                                            match antwoord13:
                                                case "ja":
                                                    print("Je zet alle takken op de goede manier neer, alleen midden in de nacht word je wakker door een gekraak. Het houd was rot en je word bedolven onder het gewicht van alle takken.")
                                                case "nee":
                                                    print("Je vertrouwt de takken niet en besluit om een ander materiaal te gebruiken voor je slaapplek, er licht veel schors van een omgevallen boom op de grond. Dus je besluit om op het eiland een huisje te gaan maken en er zelf te gaan wonen.")
                            case "nee":
                                print("Je blijft verder en verder lopen op het strand totdat je een hutje tegenkomt. Je gaat naar binnen en je ziet een kaart liggen met de locatie van een bootje en brandstof. Ook is er fruit te vinden in het huisje, dit neem je mee op je reis terug naar het vaste land.")
        case "nee":
            print("Je overlijd aan een tekort aan voedsel en water.")

Game()