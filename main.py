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
    print('To exit the program please input "exit"')
    print('To see this menu again please input "menu"')


class Main:
    main_menu()
    user_input = input()
    while user_input != 'exit':

        if user_input == '1':
            print("One Selected")
            print(csvTable.table)
            user_input = input()

        if user_input == '2':
            print("Two Selected")
            user_input = input()

        if user_input == '3':
            print("Three Selected")
            user_input = input()

        if user_input == '4':
            print("Four Selected")
            user_input = input()

        elif user_input == 'exit':
            exit()

        else:
            user_input = input()



    



