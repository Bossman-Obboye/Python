# Exercise: Write a program that converts a temperature given in Celsius
# to Fahrenheit. The formula for conversion is:
# Fahrenheit=Celsius×5/9​+32

tempInCelsius = input("Enter temperature in Celsius: ")
tempInFehrenheit = int(tempInCelsius) * (5 / 9) + 32
print(f"Temperature in Fehrenheit is: {tempInFehrenheit}")
