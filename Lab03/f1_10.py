def unique_elements(list):
    unique_list = []

    for el in list:
        if el not in list:
            unique_list.append(el)

    return unique_list