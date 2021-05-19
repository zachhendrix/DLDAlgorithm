# Requirement C.1: Zach Hendrix Student ID:001220147
import math
from ImportDistance import distance_table
from ImportPackage import *
from ImportAddress import address_table
from Truck import Truck
from Clock import Clock

# The truck objects are created and the lists are manually specified to fit rules and specifications
# Time Complexity O(1)
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
# Time Complexity O(1)
def main_menu():
    print('Welcome to the Daily Local Delivery List for WGU')
    print('Please input a command and press the "Enter" key:')
    print('1. Run Simulation')
    print('2. Search Deliveries by Content')
    print('3. Remove Specific Deliveries')
    print('4. Lookup Delivery Status at Time')
    print('5. Check Truck Status')
    print('To exit the program please input "exit"')
    print('To see this menu again please input "menu"')


# Function that displays the Search Menu and the options listed
# Time Complexity O(1)
def search_menu():
    print('Search by what component?')
    print('1. Package ID')
    print('2. Address')
    print('3. Deadline')
    print('4. Delivery City')
    print('5. Zip Code')
    print('6. Weight')
    print('7. Delivery Status')
    print('To exit the search please input "exit"')
    print('To see this menu again please input "menu"')


# Requirement F: Requirement was ill worded so I made sure that it could search by any factor just in case
# Time Complexity O(N)
def search_function():
    search_menu()
    user_input = input()
    while user_input != 'exit':
        if user_input == '1':
            print("Please input Package ID")
            package_id = input()
            print(package_hash.search(package_id))

        if user_input == '2':
            print("Please input Address")
            address = input()
            for x in range(1, len(package_hash.table)):
                package_ref = package_hash.search(str(x))
                if address in package_ref[1]:
                    print(package_ref)

        if user_input == '3':
            print("Please input Deadline e.g.'10:30 AM'")
            deadline = input()
            for x in range(1, len(package_hash.table)):
                package_ref = package_hash.search(str(x))
                if deadline in package_ref[5]:
                    print(package_ref)

        if user_input == '4':
            print("Please input City Destination")
            city = input()
            for x in range(1, len(package_hash.table)):
                package_ref = package_hash.search(str(x))
                if city in package_ref[2]:
                    print(package_ref)

        if user_input == '5':
            print("Please input Zip Code")
            zip_code = input()
            for x in range(1, len(package_hash.table)):
                package_ref = package_hash.search(str(x))
                if zip_code in package_ref[4]:
                    print(package_ref)

        if user_input == '6':
            print("Please input Weight")
            weight = input()
            for x in range(1, len(package_hash.table)):
                package_ref = package_hash.search(str(x))
                if weight in package_ref[6]:
                    print(package_ref)

        if user_input == '7':
            print("Please input Status")
            status = input()
            for x in range(1, len(package_hash.table)):
                package_ref = package_hash.search(str(x))
                if status in package_ref[7]:
                    print(package_ref)

        if user_input == 'menu':
            search_menu()
            user_input = input()

        else:
            user_input = input()

    main_menu()


# Function that resets information so that the deliveries may be checked at a certain time
# Time Complexity O(1)
def reset_sim():
    import_packages()

    # Reset truck variables
    truck_Alpha.set_mileage(0)
    truck_Alpha.set_location('4001 South 700 East')
    truck_Alpha.set_cargo([])

    truck_Beta.set_mileage(0)
    truck_Beta.set_location('4001 South 700 East')
    truck_Beta.set_cargo([])

    truck_Gamma.set_mileage(0)
    truck_Gamma.set_location('4001 South 700 East')
    truck_Gamma.set_cargo([])

    # Reset Clock variables
    clock_Alpha.set_time(9, 5, True)
    clock_Alpha.set_time(8, 0, True)
    clock_Alpha.set_time(8, 0, True)


# Functions that loads the trucks using the delivery lists, no specifications on time, assume that Truck Gamma is not
# loaded until the packages are fixed and arrive at the depot.
def load_trucks():
    # Truck loading process, included is some code that changes the delivery status of the packages to "On Truck"
    # while the user will never really see that in this iteration of the program, I included it for scalability.
    # Time Complexity O(N)
    for i in delivery_list_alpha:
        package_ref = package_hash.search(str(i))
        package_ref[7] = "On Truck"
        package_hash.insert(package_ref[0], package_ref)
        truck_Alpha.cargo.append(i)

    for i in delivery_list_beta:
        package_ref = package_hash.search(str(i))
        package_ref[7] = "On Truck"
        package_hash.insert(package_ref[0], package_ref)
        truck_Beta.cargo.append(i)


# Function that takes the current location of the truck and the destination in which the package is going and uses
# the 'distance_table' and the indexes of the 'address_table' in a 2D Array search to return the distance information.
# Time Complexity O(1)
def distance_between(current, new):
    current_index = address_table.index(current)
    new_index = address_table.index(new)
    distance = distance_table[current_index][new_index]
    return distance


# Requirement A: Greedy Algorithm
# Function that uses a greedy algorithm to determine the quickest route to deliver the packages loaded.
# Time Complexity O(N)
def greedy_delivery(truck, clock, end_time):
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
        clock.add_minutes(float(shortest_distance / truck.miles_per_min))
        shortest_package[7] = "Delivered at " + clock.get_time()
        package_hash.insert(shortest_id, shortest_package)
        print("Package:", shortest_id, "delivered at:", clock.get_time())

        # Implemented as an afterthought for requirement G
        if clock.get_time() >= end_time:
            delivery_end = True

        # The truck continues the process until the cargo is empty in which it returns to the depot
        if not truck.cargo:
            truck.add_mileage(math.ceil(float(distance_between(truck.location, '4001 South 700 East'))))
            truck.set_location('4001 South 700 East')
            delivery_end = True


class Main:
    import_packages()
    main_menu()
    user_input = input()

    # Process runs until exit is entered in the command line
    while user_input != 'exit':

        # The first selection runs the simulation the trucks are loaded using the "load_trucks" function and then the
        # created trucks and their associated clocks are passed into the "greedy_delivery" function. For user visuals
        # the printing of the trucks empty cargo is included as well as the sum of the total truck mileage.
        # Time Complexity O(N)
        if user_input == '1':
            print("One Selected")
            load_trucks()
            greedy_delivery(truck_Alpha, clock_Alpha, '5:00 PM')
            greedy_delivery(truck_Beta, clock_Beta, '5:00 PM')

            # Poor truck driver has to go back out, hire more drivers WGU!
            if not truck_Alpha.cargo or not truck_Beta.cargo:
                clock_Gamma = clock_Alpha

                # Moved from the "load_trucks" function for accuracy sake
                for i in delivery_list_gamma:
                    package_ref = package_hash.search(str(i))
                    package_ref[7] = "On Truck"
                    package_hash.insert(package_ref[0], package_ref)
                    truck_Gamma.cargo.append(i)

                greedy_delivery(truck_Gamma, clock_Gamma, '5:00 PM')

            print("Truck Alpha Package IDs:", truck_Alpha.cargo)
            print("Truck Beta Package IDs:", truck_Beta.cargo)
            print("Truck Gamma Package IDs:", truck_Gamma.cargo)
            print("Total truck mileage",
                  float(truck_Alpha.mileage) +
                  float(truck_Beta.mileage) +
                  float(truck_Gamma.mileage))

        # Function that displays all deliveries, useful for seeing the difference in before the "greedy_algorithm" was
        #
        # Time Complexity O(N)
        if user_input == '2':
            print("Two Selected")
            search_function()

        # Package deletion by entering number
        # Time Complexity O(N)
        if user_input == '3':
            print("Three Selected")
            print("Please Enter Package ID to Delete")
            package_id = input()
            package_hash.remove(package_id)

        # Takes a string in time format and uses the string as a stopping point for the deliveries.
        # Could be refined, but the string NEEDS to be in HH:MM AM/PM format or else it wont work.
        # Time Complexity O(N)
        if user_input == '4':
            print("Four Selected")
            print("Please Enter a Time in 'HH:MM AM/PM' Format (i.e 10:30 AM)")

            time_string = input()

            load_trucks()
            greedy_delivery(truck_Alpha, clock_Alpha, time_string)
            greedy_delivery(truck_Beta, clock_Beta, time_string)

            if not truck_Alpha.cargo or not truck_Beta.cargo:
                clock_Gamma = clock_Alpha

                for i in delivery_list_gamma:
                    package_ref = package_hash.search(str(i))
                    package_ref[7] = "On Truck"
                    package_hash.insert(package_ref[0], package_ref)
                    truck_Gamma.cargo.append(i)

                greedy_delivery(truck_Gamma, clock_Gamma, time_string)

            print("Truck Alpha Package IDs:", truck_Alpha.cargo)
            print("Truck Beta Package IDs:", truck_Beta.cargo)
            print("Truck Gamma Package IDs:", truck_Gamma.cargo)
            print("Total truck mileage",
                  float(truck_Alpha.mileage) +
                  float(truck_Beta.mileage) +
                  float(truck_Gamma.mileage))

            for x in range(1, len(package_hash.table)):
                print(package_hash.search(str(x)))

            print("Truck Alpha Location:", truck_Alpha.get_location())
            print("Truck Alpha Mileage:", truck_Alpha.get_mileage())
            print("Truck Beta Location:", truck_Beta.get_location())
            print("Truck Beta Mileage:", truck_Beta.get_mileage())
            print("Truck Gamma Location:", truck_Gamma.get_location())
            print("Truck Gamma Mileage:", truck_Gamma.get_mileage())

            reset_sim()

        # Time Complexity O(1)
        if user_input == '5':
            print("Five Selected")
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
