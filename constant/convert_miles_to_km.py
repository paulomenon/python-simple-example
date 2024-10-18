# Define the constant conversion factor (1 mile = 1.60934 kilometers)
MILES_TO_KILOMETERS = 1.60934

# Function to convert miles to kilometers
def convert_miles_to_km(miles):
    return miles * MILES_TO_KILOMETERS

# Test the function with an example
miles_value = 5  # Example value in miles
kilometers_value = convert_miles_to_km(miles_value)

print(f"{miles_value} miles is equal to {kilometers_value:.2f} kilometers.")
