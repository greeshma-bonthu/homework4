def FahToCel(f):
    return ((f-32) * (5/9))

print("Enter Temperature in Fahrenheit: ", end="")
fah = int(input())

cel = FahToCel(fah)
print("\nEquivalent Temperature in Celsius = ", cel)