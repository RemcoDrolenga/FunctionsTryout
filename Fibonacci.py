nummer1=0
nummer2=1
def Fibonacci(Getal1,Getal2):
    doorgaan = "doorgaan"
    while doorgaan == "doorgaan":
        Getal2 = Getal1 + Getal2
        Getal1 = Getal1 + Getal2
        print(Getal2)
        print(Getal1)
        if Getal1 >= 1000000:
            doorgaan = "stop"
Fibonacci(nummer1,nummer2)
