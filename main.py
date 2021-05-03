# Zach Hendrix Student ID:001220147
import DistanceImport
import PackageImport

package_hash_table = PackageImport.package_hash_ref
distance_hash_table = DistanceImport.distance_hash_ref


def main_menu():
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
            print(distance_hash_table.table)
            for x in range(1, len(package_hash_table.table)):
                print(package_hash_table.search(str(x)))

        if user_input == '2':
            print("Two Selected")
            print("Please Enter Package ID to Search")
            package_id = input()
            print(package_hash_table.search(package_id))

        if user_input == '3':
            print("Two Selected")
            print("Please Enter Package ID to Delete")
            package_id = input()
            package_hash_table.remove(package_id)

        if user_input == '4':
            print("Three Selected")
            for x in range(1, len(package_hash_table.table)):
                print(package_hash_table.search(str(x)))

        if user_input == '5':
            print("Four Selected")

        elif user_input == 'menu':
            main_menu()

        elif user_input == 'exit':
            exit()

        else:
            user_input = input()
