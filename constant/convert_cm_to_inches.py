# Define the constant conversion factor (1 inch = 2.54 centimeters)
CM_TO_INCHES = 0.393701

# Function to convert centimeters to inches
def convert_cm_to_inches(cm):
    return cm * CM_TO_INCHES

# Test the function with an example
cm_value = float(input('Please type a value em centimeters (cm): '))  # Example value in centimeters
inches_value = convert_cm_to_inches(cm_value)

print(f"{cm_value} cm is equal to {inches_value:.2f} inches.")
