def new_list():
    new_list = {"first": None, "last": None, "size": 0}
    return new_list


def size(my_list):
    return my_list["size"]

def add_first(my_list, elem):
    node = {"info": elem, "next": my_list["first"]}
    my_list["first"] = node
    if my_list["size"] == 0:
        my_list["last"] = node
    my_list["size"] = my_list["size"] + 1
    return my_list

def add_last(my_list, elem):
    node = {"info": elem, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
    my_list["size"] = my_list["size"] + 1
    return my_list

def remove_first(my_list):
   
    if my_list["size"] == 0:
        return None
    removed = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] = my_list["size"] - 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return removed

def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    if my_list["size"] == 1:
        removed = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = my_list["size"] - 1
        return removed
    prev = my_list["first"]
    while prev["next"] is not None and prev["next"] is not my_list["last"]:
        prev = prev["next"]
    removed = my_list["last"]["info"]
    prev["next"] = None
    my_list["last"] = prev
    my_list["size"] = my_list["size"] - 1
    return removed

def insert_element(my_list, pos, elem):
    if pos <= 1:
        return add_first(my_list, elem)
    elif pos > my_list["size"]:
        return add_last(my_list, elem)
    prev = my_list["first"]
    i = 1
    while i < pos - 1 and prev is not None:
        prev = prev["next"]
        i = i + 1
    if prev is None:
        return my_list
    node = {"info": elem, "next": prev["next"]}
    prev["next"] = node
    my_list["size"] = my_list["size"] + 1
    return my_list

def delete_element(my_list, pos):
    if my_list["size"] == 0:
        return my_list
    if pos <= 1:
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
        else:
            my_list["first"] = my_list["first"]["next"]
        my_list["size"] = my_list["size"] - 1
        return my_list
    if pos > my_list["size"]:
        return my_list
    prev = my_list["first"]
    i = 1
    while i < pos - 1 and prev is not None:
        prev = prev["next"]
        i = i + 1
    if prev is None or prev["next"] is None:
        return my_list
    to_del = prev["next"]
    prev["next"] = to_del["next"]
    if to_del is my_list["last"]:
        my_list["last"] = prev
    my_list["size"] = my_list["size"] - 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 1 or pos > my_list["size"]:
        return my_list
    cur = my_list["first"]
    i = 1
    while i < pos and cur is not None:
        cur = cur["next"]
        i = i + 1
    if cur is not None:
        cur["info"] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if (pos1 < 1 or pos1 > my_list["size"] or
        pos2 < 1 or pos2 > my_list["size"] or
        pos1 == pos2):
        return my_list
    
    a = my_list["first"]
    i = 1
    while i < pos1:
        a = a["next"]
        i = i + 1
    b = my_list["first"]
    i = 1
    while i < pos2:
        b = b["next"]
        i = i + 1
    
    tmp = a["info"]
    a["info"] = b["info"]
    b["info"] = tmp
    return my_list

def sub_list(my_list, pos, num_elements):
    result = new_list()
    if num_elements <= 0 or pos < 1 or pos > my_list["size"]:
        return result
    cur = my_list["first"]
    i = 1
    while i < pos and cur is not None:
        cur = cur["next"]
        i = i + 1
    count = 0
    while cur is not None and count < num_elements:
        add_last(result, cur["info"])
        cur = cur["next"]
        count = count + 1
    return result

def is_empty(my_list):
    list = my_list["size"] == 0
    return list 

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["first"]["info"]


def last_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["last"]["info"]