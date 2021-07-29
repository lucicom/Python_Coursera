def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    result = []
    for l in list2:
        result.append(l)

    i = len(list1) - 1
    while i >= 0:
        result.append(list1[i])
        i = i - 1

    return result


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))