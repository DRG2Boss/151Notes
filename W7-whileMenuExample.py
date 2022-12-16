
file = open("W7-nationsPop.txt", 'r')
file_lines = file.readlines()
country_data = []
for line in file_lines:
    split_line_list = line.split(',')
    country = {
        "name":split_line_list[0],
        "pop":int(split_line_list[1]),while True:
    print("===========Please select and option below=======")
    print("[1] Find the country with the largest population")
    print("[2] Find the country with the smallest population")
    print("[3] Add a new country")
    print("[4] Quit the program")
    print("=================================================")
    answer = input("Enter choice 1-4:")
    if answer == '1':
        largest_so_far = country_data[0]
        for country_dict in country_data:
            if country_dict["pop"] > largest_so_far['pop']:
                largest_so_far = country_dict
        print(f"The largest country is {largest_so_far['name']} with pop {largest_so_far['pop']}")
    elif answer == '2':
        smallest_so_far = country_data[0]
        for country_dict in country_data:
            if country_dict['pop'] < smallest_so_far['pop']:
                smallest_so_far = country_dict
        print(f"The smallest country is {smallest_so_far['name']}")
    elif answer == '3':
        country_name = input("Please enter new country name")
        country_pop = int(input(f"please enter population for {country_name}:"))
        pop_change = float(input(f"Please enter the population change 2021-2022"))
        country = {
            'name':country_name,
            'pop' : country_pop,
            'change': pop_change
        }
        country_data.append(country)
    elif answer == '4':
        exit(0)
    else:
        print("invalid entry, please enter 1-4")
        "change":float(split_line_list[2]),
    }
    country_data.insert(0, country)


