def computed_value(param):
    n1 = int( "%s" % param )
    n2 = int( "%s%s" % (param,param) )
    n3 = int( "%s%s%s" % (param,param,param) )
    n4 = int( "%s%s%s%s" % (param,param,param,param) )
    return (n1+n2+n3+n4)