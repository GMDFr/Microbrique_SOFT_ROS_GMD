from robot_control_class import RobotControl

rc = RobotControl()

lists=rc.get_laser_full()

print("Position 0: ",lists[0])
print("Position 360: ",lists[360])
print("Position 719: ",lists[719])
