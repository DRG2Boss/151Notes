
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

def main():
    main_country_data = load_data()
    while True:
        print_menu()
        #finish next week

def print_menu():
    print("===========Please select and option below=======")
    print("[1] Find the country with the largest population")
    print("[2] Find the country with the smallest population")
    print("[3] Add a new country")
    print("[4] Quit the program")
    print("=================================================")
main()
