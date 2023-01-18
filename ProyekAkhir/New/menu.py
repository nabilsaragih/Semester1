from prettytable import PrettyTable
import necessaryFunction as nf

def main_menu():
    nf.clear()
    myTable = PrettyTable(["Welcome to WAGE"])
    myTable.add_row(["[1] Login"])
    myTable.add_row(["[2] Register"])
    myTable.add_row(["[3] About"])
    myTable.add_row(["[4] Exit"])
    myTable.align["Welcome to WAGE"] = "l"
    print(myTable)

def admin_menu():
    nf.clear()
    adminTable = PrettyTable(["Welcome to WAGE Admin Menu"])
    adminTable.add_row(["[1] Add new stock"])
    adminTable.add_row(["[2] View stock"])
    adminTable.add_row(["[3] Change stock"])
    adminTable.add_row(["[4] Delete stock"])
    adminTable.add_row(["[5] Logout"])
    adminTable.align["Welcome to WAGE Admin Menu"] = "l"
    print(adminTable)

def user_menu():
    nf.clear()
    userTable = PrettyTable(["Welcome to WAGE User Menu"])
    userTable.add_row(["[1] View available stock"])
    userTable.add_row(["[2] Search for stock"])
    userTable.add_row(["[3] Logout"])
    userTable.align["Welcome to WAGE User Menu"] = "l"
    print(userTable)