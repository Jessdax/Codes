main_roads = ["Roxas Avenue", "Arnaldo Boulevard", "Fuentes Drive"]
speed_limit = (80, 50, 60) 
license_plate = {}
license1 = list(license_plate)
total_fines = {}

user = int(input("How Many Vehicle Reports to Process(1-5): "))
for i in range(user):
    road_name = input("Road Name: ")
    license = {input("License Plate: ")}
    speed = int(input("Speed(km/h): "))

    license1.append(license)
    if road_name in main_roads:
        if road_name == "Roxas Avenue":
            print("Roxas Avenue's Speed Limit: ", speed_limit[0])
        elif road_name == "Arnaldo Boulevard":
            print("Arnaldo Boulevard's Speed Limit: ", speed_limit[1])
        elif road_name == "Fuentes Drive":
            print("Fuentes Drive's Speed Limit: ", speed_limit[2])
    else:
        main_roads.append(road_name)
        print(main_roads)
        speed_list = list(speed_limit)
        speed_list.append(70)
        speed_limit = tuple(speed_list)
        print(speed_limit)

    if speed > speed_limit[0] + 10:
        print("Fine: $",(speed - speed_limit[0]) + 5 )
