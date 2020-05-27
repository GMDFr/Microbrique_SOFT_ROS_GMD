from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(280)
print("laser1=", laser1)

laser2 = rc.get_laser(420)
print("laser2=", laser2)

laser3 = rc.get_laser(500)
print("laser3=", laser3)

#print ("The distance measured is: ", a)