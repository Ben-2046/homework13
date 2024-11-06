def quadraticFormula1(a,b,c):
    delta = b**2 - 4*a*c
    root = (-b+delta**0.5)/(2*a)
    return(root)

def quadraticFormula2(a,b,c):
    delta = b**2 - 4*a*c
    root = (-b-delta**0.5)/(2*a)
    return(root)

a = int(input("a=?"))
b = int(input("b=?"))
c = int(input("c=?"))

print("Root 1 is",quadraticFormula1(a,b,c))
print("Root 2 is",quadraticFormula2(a,b,c))

quit()