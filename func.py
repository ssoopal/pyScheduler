day = {
        "MONDAY" : 2,
        "TUESDAY" : 3,
        "WEDNESDAY" : 4,
        "THURSDAY" : 5,
        "FRIDAY" : 6,
        "SATURDAY" : 7,
        "SUNDAY" : 8,
    }
def display_sheet(sheet):
    user = ""
    while user != "E":
        option_select = day[input("Enter day: ").upper()]
        for row in range(1, sheet.max_row):
            cell = sheet.cell(row + 1, 1)
            cell2 = sheet.cell(row + 1, option_select)
            print(f"{cell.value} || {cell2.value}")
        user = "E"
def edit_sheet(sheet):
    user = -1
    while user != "E":
        user = input("Type a day or type E to exit. ").upper()
        if user == "MONDAY":
            y = 2
            option_select = ""
            while option_select != "EXIT":
                for row in range(1, sheet.max_row):
                    cell = sheet.cell(row + 1, 1)
                    cell2 = sheet.cell(row + 1, y)
                    print(f"{cell.value} || {cell2.value}")
                option_select = input("Enter a time you would like to select or exit: ").upper()
                if option_select.isdigit():
                    option_select = int(option_select)
                    cell = sheet.cell(option_select + 2, 1)
                    cell2 = sheet.cell(option_select + 2, 2)
                    option_select = input(f"Current Activity for {cell.value} is {cell2.value}\nWould you like to change? "
                                        f"(Y/N) ").upper()
                    if option_select == "Y":
                        cell2.value = input("Enter new activity: ")
                elif option_select == "EXIT":
                    break

        if user == "TUESDAY":
            y = 3
            option_select = ""
            while option_select != "EXIT":
                for row in range(1, sheet.max_row):
                    cell = sheet.cell(row + 1, 1)
                    cell2 = sheet.cell(row + 1, y)
                    print(f"{cell.value} || {cell2.value}")
                option_select = input("Enter a time you would like to select or exit: ").upper()
                if option_select.isdigit():
                    option_select = int(option_select)
                    cell = sheet.cell(option_select + 2, 1)
                    cell2 = sheet.cell(option_select + 2, y)
                    option_select = input(
                        f"Current Activity for {cell.value} is {cell2.value}\nWould you like to change? "
                        f"(Y/N) ").upper()
                    if option_select == "Y":
                        cell2.value = input("Enter new activity: ")
                elif option_select == "EXIT":
                    break

        if user == "WEDNESDAY":
            y = 4
            option_select = ""
            while option_select != "EXIT":
                for row in range(1, sheet.max_row):
                    cell = sheet.cell(row + 1, 1)
                    cell2 = sheet.cell(row + 1, y)
                    print(f"{cell.value} || {cell2.value}")
                option_select = input("Enter a time you would like to select or exit: ").upper()
                if option_select.isdigit():
                    option_select = int(option_select)
                    cell = sheet.cell(option_select + 2, 1)
                    cell2 = sheet.cell(option_select + 2, y)
                    option_select = input(
                        f"Current Activity for {cell.value} is {cell2.value}\nWould you like to change? "
                        f"(Y/N) ").upper()
                    if option_select == "Y":
                        cell2.value = input("Enter new activity: ")
                elif option_select == "EXIT":
                    break

        if user == "THURSDAY":
            y = 5
            option_select = ""
            while option_select != "EXIT":
                for row in range(1, sheet.max_row):
                    cell = sheet.cell(row + 1, 1)
                    cell2 = sheet.cell(row + 1, y)
                    print(f"{cell.value} || {cell2.value}")
                option_select = input("Enter a time you would like to select or exit: ").upper()
                if option_select.isdigit():
                    option_select = int(option_select)
                    cell = sheet.cell(option_select + 2, 1)
                    cell2 = sheet.cell(option_select + 2, y)
                    option_select = input(
                        f"Current Activity for {cell.value} is {cell2.value}\nWould you like to change? "
                        f"(Y/N) ").upper()
                    if option_select == "Y":
                        cell2.value = input("Enter new activity: ")
                elif option_select == "EXIT":
                    break

        if user == "FRIDAY":
            y = 6
            option_select = ""
            while option_select != "EXIT":
                for row in range(1, sheet.max_row):
                    cell = sheet.cell(row + 1, 1)
                    cell2 = sheet.cell(row + 1, y)
                    print(f"{cell.value} || {cell2.value}")
                option_select = input("Enter a time you would like to select or exit: ").upper()
                if option_select.isdigit():
                    option_select = int(option_select)
                    cell = sheet.cell(option_select + 2, 1)
                    cell2 = sheet.cell(option_select + 2, y)
                    option_select = input(
                        f"Current Activity for {cell.value} is {cell2.value}\nWould you like to change? "
                        f"(Y/N) ").upper()
                    if option_select == "Y":
                        cell2.value = input("Enter new activity: ")
                elif option_select == "EXIT":
                    break

        if user == "SATURDAY":
            y = 7
            option_select = ""
            while option_select != "EXIT":
                for row in range(1, sheet.max_row):
                    cell = sheet.cell(row + 1, 1)
                    cell2 = sheet.cell(row + 1, y)
                    print(f"{cell.value} || {cell2.value}")
                option_select = input("Enter a time you would like to select or exit: ").upper()
                if option_select.isdigit():
                    option_select = int(option_select)
                    cell = sheet.cell(option_select + 2, 1)
                    cell2 = sheet.cell(option_select + 2, y)
                    option_select = input(
                        f"Current Activity for {cell.value} is {cell2.value}\nWould you like to change? "
                        f"(Y/N) ").upper()
                    if option_select == "Y":
                        cell2.value = input("Enter new activity: ")
                elif option_select == "EXIT":
                    break

        if user == "SUNDAY":
            y = 8
            option_select = ""
            while option_select != "EXIT":
                for row in range(1, sheet.max_row):
                    cell = sheet.cell(row + 1, 1)
                    cell2 = sheet.cell(row + 1, y)
                    print(f"{cell.value} || {cell2.value}")
                option_select = input("Enter a time you would like to select or exit: ").upper()
                if option_select.isdigit():
                    option_select = int(option_select)
                    cell = sheet.cell(option_select + 2, 1)
                    cell2 = sheet.cell(option_select + 2, y)
                    option_select = input(
                        f"Current Activity for {cell.value} is {cell2.value}\nWould you like to change? "
                        f"(Y/N) ").upper()
                    if option_select == "Y":
                        cell2.value = input("Enter new activity: ")
                elif option_select == "EXIT":
                    break

def copy_sheet(sheet):
    user = ""
    while user != "E":
        option_select1 = input("Select which day you would like to copy to another: ").upper()
        option_select2 = input("Enter which day you would like to be rewritten: ").upper()
        for row in range(1, sheet.max_row):
            cell1 = sheet.cell(row + 1, day[option_select1])
            cell2 = sheet.cell(row + 1, day[option_select2])
            cell2.value = cell1.value

        print(option_select2)

        for row in range(1, sheet.max_row):
            cell = sheet.cell(row + 1, 1)
            cell2 = sheet.cell(row + 1, day[option_select2])
            print(f"{cell.value} || {cell2.value}")

        user = "E"
