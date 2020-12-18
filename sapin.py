etoile="*"
nombre= input('Donne moi un chiffre bogosse: ')
nombre=int(nombre) * 2 
espace="_"
oui=nombre-2
oui=int(oui) / 2
print(oui)
if nombre>13:
    print("       /",etoile * (nombre-14),"\\")
if nombre>11:
    print("      /",etoile * (nombre-12),"\\")
    print("     /",etoile * (nombre-10),"\\")
if nombre>9:
    print("    /",etoile * (nombre-8),"\\")
if nombre>7:
    print("   /",etoile * (nombre-6),"\\")
if nombre>5:
    print("  /",etoile * (nombre-4),"\\")
if nombre>3:
    print(" /",etoile * (nombre-2),"\\")
print("/",etoile * nombre,"\\")
print(" ",espace * oui,"#")
