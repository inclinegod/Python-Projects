weight = 0
drone_weight = 0
## define vars


#selection from user
ground = int(input("input type of shipping.\n 1 for ground\n 2 for drone."))
if ground == 2:
  drone = 1
  ground = 0
elif ground == 1:
  ground = 1
else:
    ground = int(input("input type of shipping. \n 1 for ground  \n 2 for drone.    "))


#ground shipping calculation
if ground == 1:
  weight = int(input("input weight of parcel : "))
  if weight == 0:
    print("no weight inputted ")
  elif weight <= 2:
    ground_cost = weight * 1.50 + 20
  elif weight >= 2 and weight <= 6:
    ground_cost = weight * 3.00 + 20
  elif weight >= 6 and weight <= 10:
    ground_cost = weight * 4.00 + 20
  elif weight > 10:
      ground_cost = weight * 4.75 + 20
  if weight != 0:
    print("\n To ship that parcel via ground shipping, it will cost : $ ",ground_cost)
    ground_premium = 125
    print("\n ground shipping premium costs : $",ground_premium )
else:
  if drone == 1:  #drone shipping calculation
    drone_weight = int(input("input drone weight "))
    if drone_weight == 0:
      print("\nno weight inputted ")
    elif drone_weight <= 2:
      drone_cost = drone_weight * 4.50
    elif drone_weight >= 2 and drone_weight <= 6:
      drone_cost = drone_weight * 9.00
    elif drone_weight >= 6 and drone_weight <= 10:
      drone_cost = drone_weight * 12.00
    elif drone_weight >=10:
      drone_cost = drone_weight * 14.25
    else:
        drone_weight = int(input("input drone weight "))

#prints final statement
if drone_weight != 0:
  print("\n To ship that parcel via drone shipping, it will cost : $ ",drone_cost)
