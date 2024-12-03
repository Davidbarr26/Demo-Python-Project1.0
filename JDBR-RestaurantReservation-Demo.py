"""
Project: PythonProject
program: Restaurant Reservation Demo Project
Purpose: To create a list Simulating a Restaurant available tables
Revision History:
    Created on November 11th 2024. By Juan (David) Barrios Rozo
    edited on November 13th 2024. By Juan (David) Barrios Rozo
    edited on November 15th, 2024 by Juan (David) Barrios Rozo
    edited on November 16th, 2024 by Juan (David) Barrios Rozo
    edited on November 17th, 2024 by Juan (David) Barrios Rozo
"""

"""Introduction to the program"""
# Welcome message for the User
user_name = str(input("Welcome, please enter your name: "))
welcome_message = f"\nWelcome {user_name} to Demo Restaurant"
print(welcome_message)

reservation = "\nTo make a reservation, please follow the menu below\n"
print(reservation)
print("\u00A9 Juan (David) Barrios Rozo")
print("--------------------------------------------------------------")
"""Content of the program"""
# This function will display the tables and also will show which tables are available
seating_table = [["" for _ in range(5)] for _ in range(4)]


def Display_Seating_Table():
    print("\nSeating Table:")
    for row_num, row in enumerate(seating_table):
        print(f"Row {row_num + 1}: " + " | ".join([table if table else "Available" for table in row]))
        print("--------------------------------------------------------------")
# This function allows the user to add a new reservation
def Add_New_Reservation():
    Display_Seating_Table()
    #print("--------------------------------------------------------------")
    try:
        row = int(input("Please enter the row number (e.g. 1 - 4): ")) - 1
        seat = int(input("Please enter the seat number (e.g. 1 - 5): ")) - 1

        if seating_table[row][seat] == "":
            client_name = input("Please enter the name under whom the reservation will be made: ")
            seating_table[row][seat] = client_name
            print(f"Table {row + 1}-{seat + 1} is reserved for {client_name}")
        else:
            print("This table is already reserved. Please choose another table.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid row and seat numbers.")
    Display_Seating_Table()

# This function allows the user to edit/change an existing reservation
def Edit_Existing_Reservation():
    Display_Seating_Table()
    print("--------------------------------------------------------------")
    try:
        row = int(input("Please enter the row number (e.g. 1 - 4): ")) - 1
        seat = int(input("Please enter the seat number (e.g. 1 - 5): ")) - 1

        if seating_table[row][seat] != "":
            print(f"Existing reservation: {seating_table[row][seat]}")
            confirm_edit = input("Would you like to edit the existing reservation? (yes/no): ").strip().lower()
            if confirm_edit == "yes":
                new_client_name = input("Please enter the name for the new reservation: ")
                seating_table[row][seat] = new_client_name
                print(f"The reservation was successfully updated to {new_client_name}")
            else:
                print("No changes were made to the existing reservation.")
        else:
            print("No reservation found at the selected table.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid row and seat numbers.")
    Display_Seating_Table()

# This function allows the user to cancel an existing reservation
def Cancel_Reservation():
    Display_Seating_Table()
    print("--------------------------------------------------------------")
    try:
        row = int(input("Please enter the row number (e.g. 1 - 4): ")) - 1
        seat = int(input("Please enter the seat number (e.g. 1 - 5): ")) - 1

        if seating_table[row][seat] != "":
            print(f"Existing reservation: {seating_table[row][seat]}")
            confirm_cancel = input("Would you like to cancel the reservation? (yes/no): ").strip().lower()
            if confirm_cancel == "yes":
                seating_table[row][seat] = ""
                print("The cancellation of your reservation was executed successfully.")
            else:
                print("The cancellation of your reservation was not processed successfully.")
        else:
            print("No reservation found at the selected table.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid row and seat numbers.")
    Display_Seating_Table()

# This function will allow the user to choose between the options available to reserve/cancel/edit or display the table
def Main_Menu():
    while True:
        print("\nMain Menu")
        print("1. Add New Reservation")
        print("2. Edit Existing Reservation")
        print("3. Cancel Reservation")
        print("4. Display Seating Chart")
        print("5. Exit")

        try:
            option = int(input("Please select an option (e.g. 1-5): "))
            if option == 1:
                Add_New_Reservation()
            elif option == 2:
                Edit_Existing_Reservation()
            elif option == 3:
                Cancel_Reservation()
            elif option == 4:
                Display_Seating_Table()
            elif option == 5:
                print("You are now exiting the program. Please tell us how was your experience at Demo Restaurant")
                break
            else:
                print("Sorry, you enter an invalid option. Please enter a valid option")
        except ValueError:
            print("Sorry, you enter an invalid option. Please enter a valid option")

Main_Menu()
