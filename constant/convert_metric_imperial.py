# Define the constant conversion factors
CM_TO_INCHES = 0.393701  # 1 cm = 0.393701 inches
INCHES_TO_CM = 2.54      # 1 inch = 2.54 cm

# Function to convert centimeters to inches
def convert_cm_to_inches(cm):
    return cm * CM_TO_INCHES

# Function to convert inches to centimeters
def convert_inches_to_cm(inches):
    return inches * INCHES_TO_CM

# Main program
def main():
    print("Choose a conversion option:")
    print("1. Centimeters to Inches")
    print("2. Inches to Centimeters")
    
    # Get the user's choice and convert it to an integer
    choice = int(input("Enter 1 or 2: "))
    
    # Perform the conversion based on the user's choice
    if choice == 1:
        cm_value = float(input("Enter the value in centimeters: "))  # Convert input to float to allow decimal values
        inches_value = convert_cm_to_inches(cm_value)
        print(f"{cm_value} cm is equal to {inches_value:.2f} inches.")
        
    elif choice == 2:
        inches_value = float(input("Enter the value in inches: "))  # Convert input to float to allow decimal values
        cm_value = convert_inches_to_cm(inches_value)
        print(f"{inches_value} inches is equal to {cm_value:.2f} cm.")
        
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
main()
