list = [17, 38, 10, 25, 72]

def sort_list(list):
    try:
        list = sorted(list)
        print(list)
    except TypeError:
        print(TypeError, f"Only list is allowed here !")
    return

def add_list(list, element):
    try:
        list.append(element)
        print(list)
    except TypeError:
        print(TypeError, f"Only list is allowed here !")
    return

def reverse_list(list):
    try:
        list.sort(reverse=True)
        print(list)
    except TypeError:
        print(TypeError, f"Only list is allowed here !")
    return

def show_index_list(list, element):
    try:
        index = list.index(element)
        print(index)
    except ValueError:
        print(ValueError, f"{element} isn't in the list")
    return

def remove_index_list(list, element):
    try:
        list.remove(element)
        print(list)
    except ValueError:
        print(ValueError, f"{element} isn't in the list")
    return

def slice_list(list, start_index, end_index):
    try:
        if end_index == -1:
            new_list = list[start_index:]
            print(new_list)
            return
        
        new_list = list[start_index:end_index+1]

        if new_list == []:
            raise ValueError
        
        print(new_list)
    except ValueError:
        print(ValueError, f"Out of range")
    return


sort_list(list)
add_list(list, 12)
reverse_list(list)
show_index_list(list, 17)
remove_index_list(list, 38)
slice_list(list, 2, 3)
slice_list(list, 0, 2)
slice_list(list, 3, -1)
slice_list(list, 0, -1)