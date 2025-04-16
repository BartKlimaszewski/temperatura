def convert_temp(x, y):
    if y == 'C':
        return float((x*1.8)+32), "F"
    elif y == 'F':
        return float((x-32)/(9/5)), "C"
    else:
        return None, "Invalid"

def print_converted(a, b):
    converted, unit = convert_temp(a, b)
    if converted is not None:
        print(f"{converted:.2f}{unit}")
    else:
        print("Invalid input, only C or F accepted.")
    
try:
    temp = float(input('Enter the temperature: '))
    format = input('C or F? ').strip().upper()
    print_converted(temp, format)
except ValueError:
    print("Enter valid number")