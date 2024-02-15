# Your code here
def compute_robot_distance(movements):
    x, y = 0, 0

    for move in movements:
        direction, steps = move.split()
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    distance = (x**2 + y**2)**0.5
    rounded_distance = round(distance)

    return rounded_distance

print(compute_robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]))
