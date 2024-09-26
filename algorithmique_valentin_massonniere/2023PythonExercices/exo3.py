import math

def calcul():
    for x in range(-3, 3):
        try:
            result = math.sin(x)/x
            print(result)
        except ZeroDivisionError:
            print("Cannot divide by 0: sin(0)/0 is 1.")
        
calcul()
