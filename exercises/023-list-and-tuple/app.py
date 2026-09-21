# Your code here
def list_and_tuple(*arg):
    args=[]
    for i in arg:
        args.append(str(i))
    return (list(args), tuple(args))

print(list_and_tuple(34,67,55,33,12,98))