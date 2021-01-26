print('Binary To Decimal Converter')

while True:
  # exits the program
    print("Enter 'x' for exit.")
    binary = input("Enter number in Binary Format: ")
    if binary == 'x':
        break
    else:
        # converts binary to decimals
    decimal = int(binary, 2)
    print(binary, "in Decimal =", decimal, "\n")
