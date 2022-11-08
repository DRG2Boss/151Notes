# "def" is shorthand for "define", and is used when defining a function.
def load_data():
    file = open("W7-nationsPop.txt", 'r')
    file_lines = file.readlines()
    country_data = []
    for line in file_lines:
        split_line_list = line.split(',')
        country = {
            "name": split_line_list[0],
            "pop": int(split_line_list[1]),
            "change": float(split_line_list[2]),
        }
        country_data.insert(0, country)
    return country_data


def main():
    main_country_data = load_data()
    while True:
        print_menu()
        answer = input("Please enter choice 1-4:")
        process_user_choice(answer, main_country_data)


def find_smallest(pop_data):
    smallest_so_far = pop_data[0]
    for country in pop_data:
        if country["pop"] < smallest_so_far["pop"]:
            smallest_so_far = country
    print(f"{smallest_so_far['name']} is the smallest country.")


def find_largest(country_data):
    largest_so_far = country_data[0]
    for nation in country_data:
        if nation["pop"] > largest_so_far["pop"]:
            largest_so_far = nation
    print(f"{largest_so_far['name']} is the largest country.")


def process_user_choice(user_choice, country_data):
    if user_choice == "1":
        find_largest(country_data)
    elif user_choice == "2":
        find_smallest(country_data)
    elif user_choice == "3":
        add_country(country_data)
    elif user_choice == "4":
        exit(0)
    else:
        print("Invalid selection, please select again")


def add_country(nations_pop_data):
    country_name = input("Please enter new country name:")
    country_pop = int(input(f"please enter population for {country_name}:"))
    pop_change = float(input(f"Please enter the population change 2021-2022:"))
    country = {
        'name': country_name,
        'pop': country_pop,
        'change': pop_change
    }
    nations_pop_data.append(country)


def print_menu():
    print("===========Please select and option below=======")
    print("[1] Find the country with the largest population")
    print("[2] Find the country with the smallest population")
    print("[3] Add a new country")
    print("[4] Quit the program")
    print("=================================================")


main()
