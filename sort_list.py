def sort_list(rules: tuple[str], color_lst: list[str]) -> list[str]:
    """ Sort color list acording rules without python standard libraries

    :param rules: Rules for items order in color list
    :param color_lst: List of color objects
    :return: Sorted color objects list

    """
    if type(rules) is not tuple:
        raise TypeError("Rules must be of type tuple")
    if type(color_lst) is not list:
        raise TypeError("Rules must be of type list")
    if rules == ():
        raise Exception("Rules must not be empty")
    if len(rules) != len(set(rules)):
        raise Exception("Rules must contain unique elements")

    for i in range(len(color_lst)):
        if color_lst[i] not in rules:
            raise KeyError(
                f"Symbol '{color_lst[i]}' is not in rules or it is written with a different keyboard layout. Register is important")
        j = i
        while j > 0 and rules.index(color_lst[j]) < rules.index(color_lst[j-1]):
            color_lst[j], color_lst[j-1] = color_lst[j-1], color_lst[j]
            j -= 1

    return color_lst


in_obj_list = ['С', 'С', 'З', 'С', 'К', 'З', 'З', 'З', 'К', 'К', 'С', 'З', 'С', 'С', 'К', 'З']
obj_rules = ('З', 'С', 'К')

print("Input: ")
print("    Rules: ", obj_rules)
print("    Color list: ", in_obj_list)
print("Output: ", sort_list(rules=obj_rules, color_lst=in_obj_list))

