def new_list():
    new_list = {"elements": [], "size": 0}
    return new_list


def get_element(my_list, index):
    return my_list["elements"][index]

def size(my_list):
    return my_list["size"]

def is_empty(my_list):
    return my_list["size"] == 0


def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["elements"][0]

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["elements"][my_list["size"] - 1]

def add_first(my_list, elem):
    my_list["elements"] = [elem] + my_list["elements"]
    my_list["size"] = my_list["size"] + 1
    return my_list

def add_last(my_list, elem):
    my_list["elements"] = my_list["elements"] + [elem]
    my_list["size"] = my_list["size"] + 1
    return my_list

def remove_first(my_list):
  
    if my_list["size"] == 0:
        return None
    removed = my_list["elements"][0]
    my_list["elements"] = my_list["elements"][1:]
    my_list["size"] = my_list["size"] - 1
    return removed

def remove_last(my_list):
 
    if my_list["size"] == 0:
        return None
    removed = my_list["elements"][my_list["size"] - 1]
    my_list["elements"] = my_list["elements"][: my_list["size"] - 1]
    my_list["size"] = my_list["size"] - 1
    return removed

def insert_element(my_list, pos, elem):

    if pos < 1 or pos > my_list["size"] + 1:
        return my_list
    left = my_list["elements"][: pos - 1]
    right = my_list["elements"][pos - 1 :]
    my_list["elements"] = left + [elem] + right
    my_list["size"] = my_list["size"] + 1
    return my_list

def delete_element(my_list, pos):
    if pos < 1 or pos > my_list["size"]:
        return my_list
    left = my_list["elements"][: pos - 1]
    right = my_list["elements"][pos:]
    my_list["elements"] = left + right
    my_list["size"] = my_list["size"] - 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 1 or pos > my_list["size"]:
        return my_list
    my_list["elements"][pos - 1] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if (pos1 < 1 or pos1 > my_list["size"] or
        pos2 < 1 or pos2 > my_list["size"] or
        pos1 == pos2):
        return my_list
    i = pos1 - 1
    j = pos2 - 1
    temp = my_list["elements"][i]
    my_list["elements"][i] = my_list["elements"][j]
    my_list["elements"][j] = temp
    return my_list

def sub_list(my_list, pos, num_elements):
    result = new_list()
    if num_elements <= 0 or pos < 1 or pos > my_list["size"]:
        return result
    end = pos - 1 + num_elements
    if end > my_list["size"]:
        end = my_list["size"]
    i = pos - 1
    while i < end:
        add_last(result, my_list["elements"][i])
        i = i + 1
    return result
    


def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) -- 0:
                keyexist - True
                break
        if keyexist:
            return keypos
    return -1