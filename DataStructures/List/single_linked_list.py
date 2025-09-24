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
    if pos < 0 or pos >= my_list["size"]:
        return None

    node = my_list["first"]
    for _ in range(pos):
        node = node["next"]

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


def selection_sort(lst, cmp_function):
    n = size(lst)
    i = 0
    while i < n - 1:
        min_index = i
        elem_min = get_element(lst, i)

        j = i + 1
        while j < n:
            elem_j = get_element(lst, j)
            if elem_j is not None and elem_min is not None:
                if cmp_function(elem_j, elem_min):
                    elem_min = elem_j
                    min_index = j
            j += 1

        exchange(lst, i, min_index)
        i += 1



def insertion_sort(lst, cmp_function):
    n = size(lst)
    i = 1
    while i < n:
        key = get_element(lst, i)
        j = i - 1
        stop = False  

        while j >= 0 and not stop:
            elem_j = get_element(lst, j)
            if elem_j is not None and cmp_function(key, elem_j):
                exchange(lst, j, j + 1)
                j -= 1
            else:
                stop = True
        i += 1



def shell_sort(lst, cmp_function):
    n = size(lst)
    gap = n // 2

    while gap > 0:
        i = gap
        while i < n:
            temp = get_element(lst, i)
            j = i
            stop = False

            while j >= gap and not stop:
                elem_j_gap = get_element(lst, j - gap)
                if elem_j_gap is not None and cmp_function(temp, elem_j_gap):
                    exchange(lst, j, j - gap)
                    j -= gap
                else:
                    stop = True
            i += 1
        gap //= 2

# --- Merge Sort ---
def merge_sort(lst, cmp_function):
    n = size(lst)
    if n > 1:
        mid = n // 2
        left = sub_list(lst, 0, mid)
        right = sub_list(lst, mid, n - mid)

        merge_sort(left, cmp_function)
        merge_sort(right, cmp_function)

        i = j = k = 0
        while i < size(left) and j < size(right):
            elem_left = get_element(left, i)
            elem_right = get_element(right, j)

            if elem_left is not None and elem_right is not None:
                if cmp_function(elem_left, elem_right):
                    change_info(lst, k, elem_left)
                    i += 1
                else:
                    change_info(lst, k, elem_right)
                    j += 1
            k += 1

        while i < size(left):
            elem_left = get_element(left, i)
            if elem_left is not None:
                change_info(lst, k, elem_left)
            i += 1
            k += 1

        while j < size(right):
            elem_right = get_element(right, j)
            if elem_right is not None:
                change_info(lst, k, elem_right)
            j += 1
            k += 1


def quick_sort(lst, cmp_function):
    def partition(low, high):
        pivot = get_element(lst, high)
        i = low - 1
        j = low
        while j < high:
            elem_j = get_element(lst, j)
            if elem_j is not None and pivot is not None:
                if cmp_function(elem_j, pivot) or elem_j == pivot:
                    i += 1
                    exchange(lst, i, j)
            j += 1
        exchange(lst, i + 1, high)
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    n = size(lst)
    quick_sort_recursive(0, n - 1)
    
def default_sort_criteria(e1, e2):
    return e1 < e2