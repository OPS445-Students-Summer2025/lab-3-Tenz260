#!/usr/bin/env python3
# Author name: Tenzin wangyel
# Author ID: 134207232

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item: last item + 1
    last_item = ordered_list[-1]
    ordered_list.append(last_item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Remove all items that are in items_to_remove list
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
