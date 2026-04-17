# Convert temperatures between Celsius, Fahrenheit, and Kelvin

print("Temperature Converter")
print("-" * 30)
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("\nChoose a conversion (1/2/3/4): ")
temp = float(input("Enter the temperature: "))

if choice == "1":
    # Formula: F = (C * 9/5) + 32
    result = (temp * 9 / 5) + 32
    print(f"\n{temp:.2f} °C = {result:.2f} °F")

elif choice == "2":
    # Formula: C = (F - 32) * 5/9
    result = (temp - 32) * 5 / 9
    print(f"\n{temp:.2f} °F = {result:.2f} °C")

elif choice == "3":
    # Formula: K = C + 273.15
    result = temp + 273.15
    print(f"\n{temp:.2f} °C = {result:.2f} K")

elif choice == "4":
    # Formula: C = K - 273.15
    result = temp - 273.15
    print(f"\n{temp:.2f} K = {result:.2f} °C")

else:
    print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
