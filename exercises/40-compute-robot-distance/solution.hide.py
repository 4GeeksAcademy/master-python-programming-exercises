import math
def compute_robot_distance(props):
    pos = [0,0]
    new_prop = props.split(" ")
    for x in range(len(new_prop)):
        if new_prop[x].upper() == 'UP':
            pos[0]+=int(new_prop[x+1])
        elif new_prop[x].upper() == 'DOWN':
            pos[0]-=int(new_prop[x+1])
        elif new_prop[x].upper() == 'LEFT':
            pos[1]-=int(new_prop[x+1])
        elif new_prop[x].upper() == 'RIGHT':
            pos[1]+=int(new_prop[x+1])
        else:
            None
    return (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
   