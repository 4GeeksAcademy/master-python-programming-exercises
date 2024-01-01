from operator import itemgetter

# Your code here
def sort_tuples_ascending(data):
    tuples_list = [tuple(entry.split(',')) for entry in data]

    sorted_tuples = sorted(tuples_list, key=itemgetter(0, 1, 2))

    return sorted_tuples

example_input = [
    'Tom,19,80',
    'John,20,90',
    'Jony,17,91',
    'Jony,17,93',
    'Jason,21,85'
]

result = sort_tuples_ascending(example_input)
print(result)
