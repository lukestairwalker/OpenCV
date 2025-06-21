
# src/hilfsfunktionen.py

def gruss_nachricht(name):
    return f"Hallo, {name}! Willkommen in meinem Colab-Projekt."

def addiere_zahlen(a, b):
    return a + b

if __name__ == "__main__":
    print(gruss_nachricht("Welt"))
    ergebnis = addiere_zahlen(5, 3)
    print(f"5 + 3 = {ergebnis}")
