a = int(input("Entrez le nombre a (plus grand): "))
b = int(input("Entrez le nombre b (plus petit): "))

quotient = a // b
reste = a % b

print("Le quotient de la division de", a, "par", b, "est:", quotient)
print("Le reste de la division de", a, "par", b, "est:", reste)
