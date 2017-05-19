def digit(value):
    if 0<= value <= 9 : 
        return chr(ord('0')+value)
    if 10<= value <=35 :
        return chr(ord('A')+(value-10))
    raise IndexError

def writeinbase(entier,base):
    if base <2 or base >36 :
        print("Erreur base hors de l'interval [2,36]")
        return None
    if entier >base :
        return writeinbase(entier//base,base)+digit(entier%base)
    else:
        return digit(entier)

