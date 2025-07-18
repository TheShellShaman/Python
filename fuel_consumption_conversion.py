#liters to mpg
def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    mile = 100 * .621371
    mpg = mile / gallons
    return f"{mpg:.2f} miles per gallon"


#mpg to liters
def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 /1000 /100
    litres = 3.785411784
    return litres / km100


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
