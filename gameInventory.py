# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

from collections import OrderedDict
import csv


# Takes a list and returns the length of its longest element
def getcharlength(listofelements):
        longestlength = 0
        for element in listofelements:
            if len(str((element))) > longestlength:
                longestlength = len(str(element))
        return longestlength


# Displays inventory in all its glory
def display_inventory(inventory):
    print("Inventory:")
    for i in inventory.keys():
        print(str(inventory[i])+" "+str(i))
    print("Total number of items: "+str(sum(inventory.values())))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if str(i) not in inventory.keys():
            inventory[i] = 0
        inventory[i] += 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    parameter_list = [0, "count,asc", "count,desc"]
    # sorting dictionary elements in ascending order
    sortvalues = OrderedDict(sorted(inventory.items(), key=lambda t: t[1]))
    # sorting dictionary elements in descending order
    reversevalues = OrderedDict(sorted(inventory.items(), key=lambda t: t[1], reverse=True))
    c_length = getcharlength(inventory.keys())  # Needed for dynamic column length
    print("Inventory")
    print("{:>15}{:>{width}}".format("count", "item name", width=c_length+5))
    print("=" * (c_length+20))
    if order == "count,desc":
        for k, v in reversevalues.items():
                print("{:>15}{:>{width}}".format(str(v), str(k), width=c_length+5))
        if order == "count,asc":
            for k, v in sortvalues.items():
                print("{:>15}{:>{width}}".format(str(v), str(k), width=c_length+5))
        elif order == 0:
            for k, v in inventory.items():
                print("{:>15}{:>{width}}".format(str(v), str(k), width=c_length+5))
    print("=" * (c_length+20))
    print("Total number of items: "+str(sum(inventory.values())))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:  # Handles multiple rows for great justice
            inventory = add_to_inventory(inventory, row)
        return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv", multirows=False):
    exporting = inventory
    if multirows is True:  # Multirows exports separate dictionary keys to separate rows
        with open(filename, "w") as f:
            w = csv.writer(f, delimiter=",")
            for k, v in exporting.items():
                w.writerow([k]*v)
    else:
        with open(filename, "w") as f:
            w = csv.writer(f, inventory.keys(), delimiter=",")
            items = []
            for k in inventory.keys():
                count = inventory[k]
                for i in range(0, count):
                    items.append(k)
            w.writerow(items)
