#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestap(hr1,min1,sec1,hr2,min2,sec2):

    print(((hr2-hr1)*3600)+((min2-min1)*60)+(sec2-sec1))


#Invoke the fuction and pass two timestamsp(intergers) as its argument.
two_timestap(1,1,1,2,2,2)


