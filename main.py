# Requirement C.1: Zach Hendrix Student ID:001220147

from ImportDistance import distance_table
from ImportPackage import package_hash
from ImportAddress import address_table
from Truck import Truck

truck_Alpha = Truck(0, .3, '4001 South 700 East', [])
truck_Beta = Truck(0, .3, '4001 South 700 East', [])
truck_Gamma = Truck(0, .3, '4001 South 700 East', [])
delivery_list_alpha = [1, 2, 4, 5, 6, 7, 8, 25, 28, 29, 30, 31, 32, 34, 37, 40]
delivery_list_beta = [3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 36, 38]
delivery_list_gamma = [9, 23, 24, 26, 27, 33, 35, 39]


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

    for i in delivery_list_gamma:
        truck_Gamma.cargo.append(i)


def distance_between(current, new):
    current_index = address_table.index(current)
    new_index = address_table.index(new)
    distance = distance_table[current_index][new_index]
    return distance


# Requirement A: Greedy Algorithm
#
def greedy_delivery(truck):
    delivery_end = False
    final_packages_loaded = False
    while not delivery_end:
        shortest_distance = 100
        shortest_location = ''
        shortest_id = ''
        if truck.cargo:
            for x in range(0, len(truck.get_cargo())):
                package_select = package_hash.search(str(truck.cargo[x]))
                package_destination = package_select[1]
                package_id = package_select[0]
                distance_ref = distance_between(truck.get_location(), package_destination)
                if float(shortest_distance) >= float(distance_ref):
                    shortest_distance = str(distance_ref)
                    shortest_location = package_destination
                    shortest_id = package_id

        truck.set_location(shortest_location)
        truck.add_mileage(float(shortest_distance))
        truck.remove_cargo(int(shortest_id))
        print("Package:", shortest_id, "delivered")

        if not truck.cargo:
            truck.set_location('4001 South 700 East')
            truck.add_mileage(float(distance_between(truck.location, '4001 South 700 East')))
            delivery_end = True


class Main:
    main_menu()
    user_input = input()
    while user_input != 'exit':

        if user_input == '1':
            print("One Selected")
            load_trucks()
            greedy_delivery(truck_Alpha)
            greedy_delivery(truck_Beta)

            ##Poor truck driver has to go back out, hire more drivers WGU!
            if not truck_Alpha.cargo and not truck_Beta.cargo:
                greedy_delivery(truck_Gamma)

            print("Truck Alpha Package IDs:", truck_Alpha.cargo)
            print("Truck Beta Package IDs:", truck_Beta.cargo)
            print("Truck Gamma Package IDs:", truck_Gamma.cargo)
            print("Total truck mileage",
                  float(truck_Alpha.mileage) + float(truck_Beta.mileage) + float(truck_Gamma.mileage))

        if user_input == '2':
            print("Two Selected")

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
