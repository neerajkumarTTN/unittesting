#fahrenheit to celcius
def convert_far_to_cel(F):
    return round((F - 32) * 5/9,2)
F=float(input("Enter a temperature in degrees F:"))
result=convert_far_to_cel(F)
print(f"{F} degrees C = {result:.2f} degrees C")

#celcius to fahrenheit
def convert_cel_to_far(C):
    return C * 9/5 + 32
C=int(input("Enter a temperature in degrees C:"))
result=convert_cel_to_far(C)
print(f"{C} degree C={result:.2f} degrees F")