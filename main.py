# Zach Hendrix Student ID:001220147
import CSVImport
import HashTable

csvTable = CSVImport.csvHashRef

def main_menu():
    print('')
    print('Welcome to the Daily Local Delivery List for WGU')
    print('Please input a command and press the "Enter" key:')
    print('1. Display Deliveries')
    print('2. Lookup Specific Deliveries')
    print('3. Lookup Delivery Status')
    print('4. Lookup Truck Status')


class Main:
    main_menu()
    user_input = input()
    while user_input != 'end':
        if user_input == 1:
            print("One Selected")
            pass

        elif user_input == 'end':
            exit()


    



