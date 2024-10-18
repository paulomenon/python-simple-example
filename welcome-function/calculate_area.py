# Define the function to calculate area of a rectangle
def calculate_area(width, height):
    area = width * height
    return area

# Now let's use this function with different values
rect1_width = 5
rect1_height = 10

rect2_width = 3
rect2_height = 8

# Calling the function for different rectangles
area1 = calculate_area(rect1_width, rect1_height)
area2 = calculate_area(rect2_width, rect2_height)

print(f"The area of the first rectangle is: {area1}")
print(f"The area of the second rectangle is: {area2}")
