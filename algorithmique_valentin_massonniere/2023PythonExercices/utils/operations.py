from os import system

def soustractions(nb, max=10):
    try:
        nb = int(nb)
        max = int(max)

        print(f"Table de soustraction de {nb} : ")
        for i in range(max):
            print(f"{nb} - {i} = {nb - i}")
    except ValueError:
        raise ValueError("Only integer is allowed here")
    

def division(nb, max=10):
    try:
        nb = int(nb)
        max = int(max)

        print(f"Table de division de {nb} : ")
        for i in range(max):
            if i == 0:
                print(f"{nb} / {i} = impossible")
                continue
            print(f"{nb} / {i} = {nb / i}")
    except ValueError:
        raise ValueError("Only integer is allowed here")
    

if __name__ == "__main__":
    soustractions(1)
    division(4)