# Zach Hendrix Student ID:001220147
import datetime
from DistanceImport import distance_table
from PackageImport import package_hash
import Truck

truck_Alpha = Truck.Truck(0, .3, "At Hub", [])
truck_Beta = Truck.Truck(0, .3, "At Hub", [])
delivery_list_alpha = [1, 2, 4, 5, 6, 7, 8, 25, 28, 29, 30, 31, 32, 34, 37, 40]
delivery_list_beta = [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 36, 38]
delivery_list_gamma = [9, 23, 24, 26, 27, 33, 35]


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


def load_trucks():
    # Truck loading process
    for i in delivery_list_alpha:
        truck_Alpha.cargo.append(i)
    for i in delivery_list_beta:
        truck_Beta.cargo.append(i)


def greedy_delivery(truck):
    shortest_distance = 0
    for x in range(1, len(truck.cargo)):
        package_select = package_hash.search(str(x))
        print(package_select)



class Main:
    main_menu()
    user_input = input()
    while user_input != 'exit':

        if user_input == '1':
            print("One Selected")
            load_trucks()
            greedy_delivery(truck_Alpha)
            greedy_delivery(truck_Beta)
            print("Truck Alpha Package IDs:", truck_Alpha.cargo)
            print("Truck Beta Package IDs:", truck_Beta.cargo)


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
            print("Truck Alpha Location:", truck_Alpha.location)
            print("Truck Beta Location:", truck_Beta.location)

        if user_input == 'menu':
            main_menu()

        if user_input == 'exit':
            exit()

        else:
            user_input = input()
