from operator import itemgetter
import functools


def sort_list_with_tuple_rules(rules: tuple[str], color_lst: list[str]) -> list[str]:
    """ Sort color list acording rules by sorted method with itemgetter

    :param rules: Rules for items order in color list
    :param color_lst: List of color objects
    :return: Sorted color objects list

    """
    list_with_rules = [(item, rules.index(item),) for item in color_lst]
    # return [item[0] for item in sorted(list_with_rules, key=lambda i : i[1])]

    return [item[0] for item in sorted(list_with_rules, key=itemgetter(1))]


def sort_list_with_functools(rules, color_lst):
    """ Sort color list acording rules by sorted method with functools

    :param rules: Rules for items order in color list
    :param color_lst: List of color objects
    :return: Sorted color objects list

    """
    return sorted(color_lst, key=functools.cmp_to_key(lambda x,y: -1 if rules.index(x) < rules.index(y) else 1))


in_obj_list = ['С', 'С', 'З', 'С', 'К', 'З', 'З', 'З', 'К', 'К', 'С', 'З', 'С', 'С', 'К', 'З']
in_obj_rules = [ 'З', 'С', 'К']

print("Input: ")
print("    Rules: ", [ 'З', 'С', 'К'])
print("    Color list: ", in_obj_list)
print("-- Version 1 --")
print("Output: ", sort_list_with_tuple_rules(in_obj_rules, in_obj_list))
print("-- Version 2 --")
print("Output: ", sort_list_with_functools(in_obj_rules, in_obj_list))