# Zach Hendrix Student ID:001220147
from DistanceImport import distance_table
from PackageImport import package_hash


def main_menu():
    print('Welcome to the Daily Local Delivery List for WGU')
    print('Please input a command and press the "Enter" key:')
    print('1. Run Simulation')
    print('2. Display Deliveries')
    print('3. Lookup Specific Deliveries')
    print('4. Remove Specific Deliveries')
    print('5. Lookup Delivery Status')
    print('6. Lookup Truck Status')
    print('To exit the program please input "exit"')
    print('To see this menu again please input "menu"')


class Main:
    main_menu()
    user_input = input()
    while user_input != 'exit':

        if user_input == '1':
            print("One Selected")

        if user_input == '2':
            print("Two Selected")

            for x in range(1, len(distance_table)):
                print(distance_table[x])
            for x in range(1, len(package_hash.table)):
                print(package_hash.search(str(x)))

        if user_input == '3':
            print("Three Selected")
            print("Please Enter Package ID to Search")
            package_id = input()
            print(package_hash.search(package_id))

        if user_input == '4':
            print("Four Selected")
            print("Please Enter Package ID to Delete")
            package_id = input()
            package_hash.remove(package_id)

        if user_input == '5':
            print("Five Selected")
            for x in range(1, len(package_hash.table)):
                print(package_hash.search(str(x)))

        if user_input == '6':
            print("Six Selected")

        elif user_input == 'menu':
            main_menu()

        elif user_input == 'exit':
            exit()

        else:
            user_input = input()
