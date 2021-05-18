# Requirement C.1: Zach Hendrix Student ID:001220147
import math
from ImportDistance import distance_table
from ImportPackage import package_hash
from ImportAddress import address_table
from Truck import Truck
from Clock import Clock

# The truck objects are created and the lists are manually specified to fit rules and specifications
truck_Alpha = Truck(0, .3, '4001 South 700 East', [])
truck_Beta = Truck(0, .3, '4001 South 700 East', [])
truck_Gamma = Truck(0, .3, '4001 South 700 East', [])
clock_Alpha = Clock(9, 5, True)
clock_Beta = Clock(8, 0, True)
clock_Gamma = Clock(8, 0, True)
delivery_list_alpha = [6, 25, 28, 29, 30, 31, 32, 40]
delivery_list_beta = [1, 3, 13, 14, 15, 16, 18, 19, 20, 21, 33, 34, 36, 37, 38, 39]
delivery_list_gamma = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 26, 27, 35]


# Function that displays the Main Menu and the options listed
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


# Functions that loads the trucks using the delivery lists, no specifications on time, assume that Truck Gamma is not
# loaded until the packages are fixed and arrive at the depot.
def load_trucks():
    # Truck loading process, included is some code that changes the delivery status of the packages to "On Truck"
    # while the user will never really see that in this iteration of the program, I included it for scalability.
    for i in delivery_list_alpha:
        package_ref = package_hash.search(str(i))
        package_ref[7] = "On Truck"
        package_hash.insert(package_ref[0],package_ref)
        truck_Alpha.cargo.append(i)

    for i in delivery_list_beta:
        package_ref = package_hash.search(str(i))
        package_ref[7] = "On Truck"
        package_hash.insert(package_ref[0], package_ref)
        truck_Beta.cargo.append(i)

    for i in delivery_list_gamma:
        package_ref = package_hash.search(str(i))
        package_ref[7] = "On Truck"
        package_hash.insert(package_ref[0], package_ref)
        truck_Gamma.cargo.append(i)


# Function that takes the current location of the truck and the destination in which the package is going and uses
# the 'distance_table' and the indexes of the 'address_table' in a 2D Array search to return the distance information.
def distance_between(current, new):
    current_index = address_table.index(current)
    new_index = address_table.index(new)
    distance = distance_table[current_index][new_index]
    return distance


# Requirement A: Greedy Algorithm
# Function that uses a greedy algorithm to determine the quickest route to deliver the packages loaded.
def greedy_delivery(truck, clock):
    delivery_end = False
    while not delivery_end:
        # I suppose the shortest_distance could cause errors if over 100, but at that point use UPS or something
        shortest_distance = 100
        shortest_location = ''
        shortest_id = ''

        if truck.cargo:
            # Iterates through the trucks cargo one by one.
            for x in range(0, len(truck.get_cargo())):
                package_select = package_hash.search(str(truck.cargo[x]))
                package_destination = package_select[1]
                package_id = package_select[0]
                distance_ref = float(distance_between(truck.get_location(), package_destination))

                # Determines if the package is the closest and holds the associated useful data for the shortest
                if float(shortest_distance) >= float(distance_ref):
                    shortest_distance = distance_ref
                    shortest_location = package_destination
                    shortest_id = package_id
                    shortest_package = package_select

        # The truck moves to the location, the mileage is added to the truck and the cargo is delivered
        # The "package_hash" is also replaced with the same package data except the delivery status has changed
        # Minutes are then added to clock using "time = distance / velocity" formula.
        truck.set_location(shortest_location)
        truck.add_mileage(float(shortest_distance))
        truck.remove_cargo(int(shortest_id))
        clock.add_minute(float(shortest_distance / truck.miles_per_min))
        shortest_package[7] = "Delivered at " + clock.get_time()
        package_hash.insert(shortest_id, shortest_package)
        print("Package:", shortest_id, "delivered at:", clock.get_time())

        # The truck continues the process until the cargo is empty in which it returns to the depot
        if not truck.cargo:
            truck.add_mileage(math.ceil(float(distance_between(truck.location, '4001 South 700 East'))))
            truck.set_location('4001 South 700 East')
            delivery_end = True


class Main:
    main_menu()
    user_input = input()
    # Process runs until exit is entered in the command line
    while user_input != 'exit':
        
        # The first selection runs the simulation the trucks are loaded using the "load_trucks" function and then the
        # created trucks and their associated clocks are passed into the "greedy_delivery" function. For user visuals
        # the printing of the trucks empty cargo is included as well as the sum of the total truck mileage.
        if user_input == '1':
            print("One Selected")
            load_trucks()
            greedy_delivery(truck_Alpha, clock_Alpha)
            greedy_delivery(truck_Beta, clock_Beta)

            # Poor truck driver has to go back out, hire more drivers WGU!
            if not truck_Alpha.cargo or not truck_Beta.cargo:
                clock_Gamma = clock_Alpha
                greedy_delivery(truck_Gamma, clock_Gamma)

            print("Truck Alpha Package IDs:", truck_Alpha.cargo)
            print("Truck Beta Package IDs:", truck_Beta.cargo)
            print("Truck Gamma Package IDs:", truck_Gamma.cargo)
            print("Total truck mileage",
                  float(truck_Alpha.mileage) +
                  float(truck_Beta.mileage) +
                  float(truck_Gamma.mileage))

        # Function that displays all deliveries, useful for seeing the difference in before the "greedy_algorithm" was
        # run and after.
        if user_input == '2':
            print("Two Selected")

            for x in range(1, len(package_hash.table)):
                print(package_hash.search(str(x)))

        # Package search by entering number
        if user_input == '3':
            print("Three Selected")
            print("Please Enter Package ID to Search")
            package_id = input()
            print(package_hash.search(package_id))

        # Package deletion by entering number
        if user_input == '4':
            print("Four Selected")
            print("Please Enter Package ID to Delete")
            package_id = input()
            package_hash.remove(package_id)

        # Essentially the same as two, would be more useful if the simulation was in real time.
        if user_input == '5':
            print("Five Selected")
            for x in range(1, len(package_hash.table)):
                package_str = package_hash.search(str(x))
                print(package_str[0],": ", package_str[7])

        # Would be more useful if was run in real time, however you can see the difference before and after deliveries
        if user_input == '6':
            print("Six Selected")
            print("Truck Alpha Location:", truck_Alpha.get_location())
            print("Truck Alpha Mileage:", truck_Alpha.get_mileage())
            print("Truck Beta Location:", truck_Beta.get_location())
            print("Truck Beta Mileage:", truck_Beta.get_mileage())
            print("Truck Gamma Location:", truck_Gamma.get_location())
            print("Truck Gamma Mileage:", truck_Gamma.get_mileage())

        # Displays menu again
        if user_input == 'menu':
            main_menu()

        # Exits program
        if user_input == 'exit':
            exit()

        else:
            user_input = input()
