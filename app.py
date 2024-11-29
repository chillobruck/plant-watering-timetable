from tools import Commands
file = Commands(url=r"C:/Users/user/Desktop/tools/plant_watering/v2/files/data.txt")
file.read_file()


# main functional
while True:
    user_input = input('What do you want to do?'
                       ' S - watch file data. a - add new plant. d - delete plant. c - Change setting.')

    match user_input.lower():
        case 's':
            file.print_file()

        case 'a':
            name = input('What is the name of plant?')
            days_without_watering = input("How many days plant won't be watered?"
                                          " E.g. if you enter '7', then you will get notification you in 6 days")

            file.add_element(name, days_without_watering)

        case 'd':
            name = input('What is the name of plant?')
            file.delete_element(name)

        case 'c':
            name = input('What is the name of plant?')
            new_setting = input('What is new setting')
            inp = input('which setting are you going to change?'
                        ' N-name, D-days without watering, L-last watering').lower()

            if inp == 'n':
                file.change_setting(name, 'name', new_setting)
            elif inp == 'd':
                file.change_setting(name, 'days_without_watering', new_setting)
            elif inp == 'l':
                file.change_setting(name, 'last_watering', new_setting)
            else:
                print('unknown setting')
        case _:
            print('unknown command')
    file.save_file()
