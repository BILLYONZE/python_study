# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70,
#  it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
#  If the driver gets more than 12 points, the function should print: “License suspended”.
def car_speed(speed):
    if speed < 70:
        res ="Ok"
    else:
        res ="You are exceeding the speed Limit"
        tim = round((speed - 70) / 5)
        if tim > 12:
            res ="License Suspended"
        else:
            res =f"You have {tim} Demerit Points"
    return res
speed = input("Vehicles Speed: ")
speed = int(speed)
sp = car_speed(speed)
print(sp)

