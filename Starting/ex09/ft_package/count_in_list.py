def count_in_list(dt_list, string):
    i = 0

    for word in dt_list:
        if word == string:
            i += 1
    return i
