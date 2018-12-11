#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp_list = list(my_list)
    if idx < 0:
        return temp_list
    elif idx > len(temp_list):
        return temp_list
    else:
        for index in temp_list:
            if index == idx:
                temp_list[idx] = element
                return temp_list
