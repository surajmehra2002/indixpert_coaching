def practice1():
    while True:
        square_numbers = []

        for num in range(1, 11):
            square_numbers.append(num*num)

        print("First 10 square numbers:")
        print(square_numbers)

        square_numbers[2] = 50
        print("\nReplacing the third element with 50:")
        print(square_numbers)

        square_numbers.insert(4, 25)
        print("\nInserting 25 at the fifth position:")
        print(square_numbers)

        square_numbers.pop()
        print("\nRemoving the last element from the list and the final list:")
        print(square_numbers)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice2():
    while True:
        natural_numbers = []

        for num in range(1, 21):
            natural_numbers.append(num)

        print("List of first 20 natural numbers:")
        print(natural_numbers)

        first_10_numbers = natural_numbers[0:10]
        print("\nFirst 10 element slice:")
        print(first_10_numbers)

        last_5_numbers = natural_numbers[-5:]
        print("\nLast 5 element slice:")
        print(last_5_numbers)

        print("\nBoth Slices:")
        print(first_10_numbers)
        print(last_5_numbers)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice3():
    while True:
        odd_numbers = [2*num - 1 for num in range(1, 11)]

        print("List of the first 10 odd numbers:")
        print(odd_numbers)

        square_odd_numbers = [num**2 for num in odd_numbers]
        print("\nList of squares of the first 10 odd numbers:")
        print(square_odd_numbers)

        print("\nPrinting both lists:")
        print(odd_numbers)
        print(square_odd_numbers)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice4():
    while True:
        continents = ("Europe", "Africa", "Asia", "Australia", "Americas")

        print("Tuple of continents:")
        print(continents)

        print("\nThird continent in the tuple")
        print(continents[2])

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice5():
    while True:
        newtuple = ("This is Gaurav", 25, 3.14)

        print("Tuple with string, integer, and float:")
        print(newtuple)

        gaurav, number, decimal = newtuple
        print("\ntuple into 3 variables and printing said variable:")
        print(gaurav)
        print(number)
        print(decimal)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice6():
    while True:
        nested_tuple = ((365, 2.56, "Hello"), ('ABCD', 57, 7.89))
        print(nested_tuple)

        second_element = nested_tuple[0][1]
        print("\nSecond element of first tuple")
        print(second_element)

        first_element = nested_tuple[1][0]
        print("\nFirst element of second tuple")
        print(first_element)

        print("\nPrinting Both elements")
        print(second_element)
        print(first_element)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice7():
    while True:
        odd_numbers = {1, 3, 5, 7, 9}
        print("Odd Numbers:", odd_numbers)
        even_numbers = {2, 4, 6, 8, 10}
        print("\nEven Numbers:", even_numbers)

        union = odd_numbers.union(even_numbers)
        print("\nUnion of numbers:", union)

        intersection = odd_numbers.intersection(even_numbers)
        print("\nIntersection of numbers:", intersection)

        print("\nUnion of the sets:", union)
        print("\nIntersection of the sets:", intersection)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice8():
    while True:
        primenum = {2, 3, 5, 7, 11}
        print("First 5 prime numbers: ", primenum)

        primenum.add(11)
        print("\nAdding 11 to the set: ", primenum)

        primenum.remove(2)
        print("\nRemoving number 2 from set: ", primenum)

        is_seven_in_set = 7 in primenum
        print("\nChecking if 7 is in set: ", is_seven_in_set)  # True or False, Boolean value.

        print("\nFinal set: ", primenum)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice9():
    while True:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        print("Set of vowels: ", vowels)

        check_e = 'e' in vowels
        print("\nChecking if 'e' is in set: ", check_e)

        check_x = 'x' in vowels
        print("\nChecking if 'x' is in set: ", check_x)

        print("\nIs 'e' in the set? ", check_e)
        print("\nIs 'x' in the set? ", check_x)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice10():
    while True:
        student = {
            'name': 'Gaurav', 'age': 23, 'grades': [70, 80, 82]
        }
        print(student)

        student['age'] = 24
        print("\nUpdating age: ", student)

        student['favorite_subject'] = 'English'
        print("\nAdding a key and value pair for favorite subject: ", student)

        print("\nFinal Dictionary: ", student)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice11():
    while True:
        cities = {
            'Delhi': '3.3 crore', 'Mumbai': '2.1 crore', 'Kolkata': '1.5 crore', 'Bengaluru': '1.4 crore', 'Chennai': '1.2 crore'
        }
        print(cities)

        population_of_Mumbai = cities.get('Mumbai')
        print("\nUsing the get method to access the population of a specific city: ", population_of_Mumbai)

        remove_city = cities.pop('Chennai')
        print("\nUsing the pop method to remove a city from the dictionary: ", 'Chennai')

        print("\nFinal dictionary: ", cities)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


def practice12():
    while True:
        countries = {
            'USA': {'capital': 'Washington D.C.', 'population': 331449281},
            'India': {'capital': 'New Delhi', 'population': 1380004385},
            'Australia': {'capital': 'Canberra', 'population': 27297500}
        }
        print("Initial Dictionary: ", countries)

        capital_of_India = countries['India']['capital']
        print("\nPrinting the capital of one country: ")
        print("Capital of India: ", capital_of_India)

        countries['USA']['population'] = 551456891
        print("\nFinal dictionary: ", countries)

        choice = input("\nEnter 'm' to return to main menu: ")
        if choice.lower() == 'm':
            break


while True:
    print("\nChoose a task:")
    print("1. Practice one")
    print("2. Practice two")
    print("3. Practice three")
    print("4. Practice four")
    print("5. Practice five")
    print("6. Practice six")
    print("7. Practice seven")
    print("8. Practice eight")
    print("9. Practice nine")
    print("10. Practice ten")
    print("11. Practice eleven")
    print("12. Practice twelve")
    print("0. Exit")

    choice = input("\nEnter your choice (0-12): ")

    if choice == '1':
        practice1()
    elif choice == '2':
        practice2()
    elif choice == '3':
        practice3()
    elif choice == '4':
        practice4()
    elif choice == '5':
        practice5()
    elif choice == '6':
        practice6()
    elif choice == '7':
        practice7()
    elif choice == '8':
        practice8()
    elif choice == '9':
        practice9()
    elif choice == '10':
        practice10()
    elif choice == '11':
        practice11()
    elif choice == '12':
        practice12()
    elif choice == '0':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 0 to 12.")


# # print("Create a list of the first 10 square numbers")
# if not(2==3):

# set1 = {1,2,3,4}
# set2 = {"one","two","three","four"}

# set1.update([2,30])
# set2.add("suraj")

# print(set1)
# print(set2)

