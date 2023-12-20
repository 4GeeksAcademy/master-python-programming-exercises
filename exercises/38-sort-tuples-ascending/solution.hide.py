from operator import itemgetter

# Your code here
def sort_tuples_ascending(tuples):
    tuple_list = [tuple(item.split(',')) for item in tuples.split()]

    sorted_list = sorted(tuple_list, key=itemgetter(0, 1, 2))

    return sorted_list

print(sort_tuples_ascending("Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Jason,21,85"))
