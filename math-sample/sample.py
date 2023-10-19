import math

# Test Scenario: Validate a Right Triangle

# Given the lengths of two sides of a right triangle
side_a = 3
side_b = 4

# Calculate the hypotenuse using Pythagoras' theorem
hypotenuse = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))

# Calculate the angles in radians
angle_a = math.atan(side_a / side_b)
angle_b = math.atan(side_b / side_a)

# Convert the angles to degrees for better readability
angle_a_degrees = math.degrees(angle_a)
angle_b_degrees = math.degrees(angle_b)

# Print the results
print(f"Given side lengths: a = {side_a}, b = {side_b}")
print(f"The calculated hypotenuse is approximately: {hypotenuse}")
print(f"Angle A is approximately: {angle_a_degrees} degrees")
print(f"Angle B is approximately: {angle_b_degrees} degrees")

# Additional Calculations
# (These could be relevant for specific test cases in certain contexts)

# Calculate the cosine of Angle A
cosine_angle_a = math.cos(angle_a)
print(f"The cosine of Angle A is approximately: {cosine_angle_a}")

# Calculate the tangent of Angle B
tangent_angle_b = math.tan(angle_b)
print(f"The tangent of Angle B is approximately: {tangent_angle_b}")
