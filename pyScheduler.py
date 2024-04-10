import openpyxl as xl
import func
wb = xl.load_workbook(input("Name of file without extension: ") + ".xlsx")
sheet = wb["Sheet1"]
user = -1

while user != 0:
    user = int(input("What would you like to do today?\n1. Display Schedule\n2. Edit Schedule\n3. Copy Schedule\n0. Exit\n"))
    if user == 1:
        func.display_sheet(sheet)

    elif user == 2:
        func.edit_sheet(sheet)

    elif user == 3:
        func.copy_sheet(sheet)


wb.save("college.xlsx")
print("Saved!")