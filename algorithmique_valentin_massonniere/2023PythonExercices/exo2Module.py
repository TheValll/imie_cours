from os import system

def addition(nb, max=10):
    try:
        nb = int(nb)
        max = int(max)

        print(f"Table d'addition de {nb} : ")
        for i in range(max):
            print(f"{nb} + {i} = {nb + i}")
    except ValueError:
        raise ValueError("Only integer is allowed here")
    

def multiplication(nb, max=10):
    try:
        nb = int(nb)
        max = int(max)

        print(f"Table de multiplication de {nb} : ")
        for i in range(max):
            print(f"{nb} * {i} = {nb * i}")
    except ValueError:
        raise ValueError("Only integer is allowed here")
    

if __name__ == "__main__":
    addition(1)
    multiplication(4)