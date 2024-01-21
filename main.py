import sys

from_idx = sys.argv[1]
to_idx = sys.argv[2]

file = open("database.txt")
# "w" write / creating a new file / overwriting , "r" read , "f" file , "a" append / save
# an example how to do it
# # file = open("test.txt")
# # .strip() means that you remove white spaces. Makes it clearer.
# # clean.row.startswith(date_to_look_for) means if it starts with a date then it will make it clearer.
# # To make it better instead of data = file.readline() and for row in data you can type for row in f: means read file


def database():
    while True:
        action = input("1. balance\2. inventory \n3. history \n0. End\n\nAction")
        if action == "0":
            print("Exiting the program...")
            break
        elif action == "1":
            print("balance: ")
            with open("database.txt") as f:
                for row in file:
                    print(row)
        elif action == "2":
            with open("database.txt", "a") as f:
                product_name = input("Enter the products name: ")
                if product_name in library:
                    library = product_name[product_name]["product_name"]
                    print(f"{product_name} is at the warehouse")
                    f.write(f"{product_name}")
                else:
                    print(f"{product_name} | not found in the library")
        elif action == "3":
            print("Get history from 2 indices")
            with open("database.txt") as f:
                rows = f.readlines()
            for row in rows:
                if row.strip().startswith(product_name):
                    print(row)
                print()
        else:
            print(f"The command: {action} are not supported by the system. Try again with another command.")
