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
    print('3. Remove Specific Deliveries')
    print('4. Lookup Delivery Status')
    print('5. Lookup Truck Status')
    print('To exit the program please input "exit"')
    print('To see this menu again please input "menu"')


class Main:
    main_menu()
    user_input = input()
    while user_input != 'exit':

        if user_input == '1':
            print("One Selected")
            for x in csvTable.table:
                print(csvTable.search(x))

        if user_input == '2':
            print("Two Selected")
            print("Please Enter Package ID")
            package_id = input()
            print(csvTable.search(package_id))

        if user_input == '3':
            print("Two Selected")
            print("Please Enter Package ID")
            package_id = input()
            csvTable.remove(package_id)

        if user_input == '4':
            print("Three Selected")

        if user_input == '5':
            print("Four Selected")

        elif user_input == 'menu':
            main_menu()

        elif user_input == 'exit':
            exit()

        else:
            user_input = input()
