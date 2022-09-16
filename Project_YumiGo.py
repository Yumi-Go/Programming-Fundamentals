# Name: Yumi Go
# Blackwater Annual Concert

MIN_PER_HR = 60

while True:
    while True:
        count = 0
        count_musician = 0
        count_singer = 0
        count_dancer = 0
        total_list = ""
        total_time = 0
        longest_time = 0
        longest_name = ""
        longest_surname = ""
        menu = int(input("Blackwater Annual Music Concert\n"
                         "-------------------------------\n"
                         "\t1. Adding Performers\n"
                         "\t2. Generate Concert Details\n"
                         "\t3. Quit\n"
                         "==> "))
        print()
        if menu == 1:
            add_number = int(input("(1) Adding Performers\n"
                                   "---------------------\n"
                                   "How many performers are you adding: "))
            while count < add_number:
                performers = open("performers.txt", 'a')
                count = count + 1
                print(f"\nBooking {count}/{add_number}: ")
                add_name = str(input("Enter your name: "))
                add_surname = str(input("Enter your surname: "))
                while True:
                    add_type = int(input("Type of Performance"
                                         "\n\t1. Musical"
                                         "\n\t2. Singer"
                                         "\n\t3. Dance"
                                         "\n==> "))
                    performance_type = ""
                    if add_type == 1:
                        performance_type = "Musician"
                        count_musician = count_musician + 1
                        break
                    elif add_type == 2:
                        performance_type = "Singer"
                        count_singer = count_singer + 1
                        break
                    elif add_type == 3:
                        performance_type = "Dancer"
                        count_dancer = count_dancer + 1
                        break
                    else:
                        print('Enter the correct number of Performance Type.')
                add_time = int(input("Time slot required(mins): "))
                add_list = f"{add_name} {add_surname} {performance_type} {add_time} minutes"
                print()
                print(add_list, file=performers)
                if add_time >= longest_time:
                    longest_time = add_time
                    longest_name = add_name
                    longest_surname = add_surname
                    longest_type = performance_type
                total_time = total_time + add_time
                total_list = total_list + f"{count}. " + add_list + '\n'
                performers.close()
            total_time_hr = total_time // MIN_PER_HR
            total_time_min = total_time % MIN_PER_HR
            summary_notes = f"Summary Notes:\n" \
                            f"-------------\n"\
                            f"{count_musician} Musician(s)\n"\
                            f"{count_singer} Singer(s)\n"\
                            f"{count_dancer} Dancer(s)\n"\
                            f"Total time required: {total_time_hr} hour(s), {total_time_min} min(s)"\
                            f"\nThe longest act added is {longest_name}({longest_surname}) {longest_time} minutes.\n"
            print("The following information has been added.")
            print(total_list)
            print(summary_notes)
        elif menu == 2:
            with open("performers.txt", 'r') as performers_read:
                line_count = 1
                for line in performers_read:
                    data = line.split(" ")
                    name = data[0]
                    surname = data[1]
                    surname_more_15 = surname + "*"
                    performance = "(" + data[2] + ")"
                    performance_duration = int(data[3])
                    if performance_duration > 15:
                        more_15 = f"{line_count}: {name} {surname_more_15:<10} {performance:<10} " \
                                  f"{performance_duration:>5} minutes"
                        print(more_15)
                    elif performance_duration <= 15:
                        less_15 = f"{line_count}: {name} {surname:<10} {performance:<10} " \
                                  f"{performance_duration:>5} minutes"
                        print(less_15)
                    line_count = line_count + 1
                print()
        elif menu == 3:
            break
        else:
            print("Invalid Value. Enter the correct number.")
    break
