# --- Conversion Functions ---

def c_to_f(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def c_to_k(celsius):
    """Converts Celsius to Kelvin."""
    return celsius + 273.15

def k_to_c(kelvin):
    """Converts Kelvin to Celsius."""
    return kelvin - 273.15

# --- Main Program Loop ---

def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '5':
            print("Exiting converter. Stay cool!")
            break
            
        if choice in ['1', '2', '3', '4']:
            try:
                # Get the temperature value from the user
                temp_input = float(input("Enter the temperature to convert: "))
                
                # Perform the conversion based on choice
                if choice == '1':
                    result = c_to_f(temp_input)
                    print(f"\nResult: {temp_input}°C is {result:.2f}°F")
                    
                elif choice == '2':
                    result = f_to_c(temp_input)
                    print(f"\nResult: {temp_input}°F is {result:.2f}°C")
                    
                elif choice == '3':
                    result = c_to_k(temp_input)
                    print(f"\nResult: {temp_input}°C is {result:.2f}K")
                    
                elif choice == '4':
                    result = k_to_c(temp_input)
                    print(f"\nResult: {temp_input}K is {result:.2f}°C")
                    
            except ValueError:
                print("\nError: Please enter a valid numerical value.")
        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")

# Run the program
if __name__ == "__main__":
    main()