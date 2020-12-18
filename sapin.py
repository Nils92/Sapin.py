etoile="*"
nombre= input('Donne moi un chiffre bogosse: ')
nombre=int(nombre) * 2 
if nombre>11:
    print("     /",etoile * (nombre-10),"I")
if nombre>9:
    print("    /",etoile * (nombre-8),"I")
if nombre>7:
    print("   /",etoile * (nombre-6),"I")
if nombre>5:
    print("  /",etoile * (nombre-4),"I")
if nombre>3:
    print(" /",etoile * (nombre-2),"I")
print("/",etoile * nombre,"I")
print()
