def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def get_float_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == 'exit':
                return 'exit'
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")

def main_loop():
    print("Welcome to the Temperature Converter!")

    while True:
        print("\n-------------------------------------------")
        print("Choose a conversion option or type 'exit' to quit:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("-------------------------------------------")

        choice_input = input("Enter your choice (1-6, or 'exit'): ")

        if choice_input.lower() == 'exit':
            print("Thank you for using the Temperature Converter. Goodbye!")
            break

        try:
            choice = int(choice_input)
            
            if choice == 1:
                temp_c = get_float_input("Enter temperature in Celsius (or 'exit'): ")
                if temp_c == 'exit':
                    continue
                temp_f = celsius_to_fahrenheit(temp_c)
                print(f"{temp_c}°C is equal to {temp_f:.2f}°F")
            
            elif choice == 2:
                temp_f = get_float_input("Enter temperature in Fahrenheit (or 'exit'): ")
                if temp_f == 'exit':
                    continue
                temp_c = fahrenheit_to_celsius(temp_f)
                print(f"{temp_f}°F is equal to {temp_c:.2f}°C")
            
            elif choice == 3:
                temp_c = get_float_input("Enter temperature in Celsius (or 'exit'): ")
                if temp_c == 'exit':
                    continue
                temp_k = celsius_to_kelvin(temp_c)
                print(f"{temp_c}°C is equal to {temp_k:.2f}K")
            
            elif choice == 4:
                temp_k = get_float_input("Enter temperature in Kelvin (or 'exit'): ")
                if temp_k == 'exit':
                    continue
                temp_c = kelvin_to_celsius(temp_k)
                print(f"{temp_k}K is equal to {temp_c:.2f}°C")
            
            elif choice == 5:
                temp_f = get_float_input("Enter temperature in Fahrenheit (or 'exit'): ")
                if temp_f == 'exit':
                    continue
                temp_k = fahrenheit_to_kelvin(temp_f)
                print(f"{temp_f}°F is equal to {temp_k:.2f}K")
            
            elif choice == 6:
                temp_k = get_float_input("Enter temperature in Kelvin (or 'exit'): ")
                if temp_k == 'exit':
                    continue
                temp_f = kelvin_to_fahrenheit(temp_k)
                print(f"{temp_k}K is equal to {temp_f:.2f}°F")
            
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

        except ValueError:
            print("Invalid input. Please enter a number corresponding to a menu option.")

if __name__ == '__main__':
    main_loop()