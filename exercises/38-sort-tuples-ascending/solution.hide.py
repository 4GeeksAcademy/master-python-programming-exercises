from operator import itemgetter, attrgetter
def sort_tuples_ascending(tuples):
    l = []
    l.append(tuple(tuples.split(",")))
    return (sorted(l, key=itemgetter(0,1,2)))
