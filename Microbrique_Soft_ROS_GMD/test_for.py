from robot_control_class import RobotControl

rc = RobotControl()


a=rc.get_laser_full()
print(a)

maxim = 0

for value in a  :
    if value > maxim:
        maxim=value
    print ("The higher value in the list is: ", maxim)
