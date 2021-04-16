speed_driver = int(input("Enter Driver Here"))
speed = int(input("Enter Allowed Speed"))
points = (speed_driver - speed)/5

if speed_driver <= 60:
    print("OK")
else:
    if points >= 12:
        print("demerits " + str(points))

if points > 12:
    print("Go To Jail")








