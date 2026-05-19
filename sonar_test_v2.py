import os
import sys # Unused import

# Hardcoded password - Security Vulnerability
DB_PASSWORD = "super_secret_password_123"

def calculate_area(radius):
    # Print instead of logging
    print(f"Calculating area for radius: {radius}")
    pi = 3.14159
    return pi * (radius ** 2)

def calculate_volume(radius, height):
    # Duplicate logic or similar pattern
    print(f"Calculating volume for radius: {radius} and height: {height}")
    pi = 3.14159
    area = pi * (radius ** 2)
    return area * height

def function_with_too_many_arguments(a, b, c, d, e, f, g, h):
    # Sonar usually flags functions with too many parameters
    return a + b + c + d + e + f + g + h

def main():
    # Unused variable
    result = calculate_area(5)
    
    # Hardcoded sensitive data usage
    print(f"Connecting to DB with password: {DB_PASSWORD}")

    if True: # Always true condition
        print("This always runs")

if __name__ == "__main__":
    main()
