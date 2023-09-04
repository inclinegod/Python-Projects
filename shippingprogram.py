

weight = 0
ground_cost = 0
drone_weight = 0
drone_cost = 0



#ground shipping

if weight == 0:
  print("no weight inputted")
elif weight <= 2:
  ground_cost = weight * 1.50 + 20
elif weight >= 2 and weight <= 6:
  ground_cost = weight * 3.00 + 20
elif weight >= 6 and weight <= 10:
  ground_cost = weight * 4.00 + 20
else:
  if weight > 10:
    ground_cost = weight * 4.75 + 20

if weight != 0:
  print("\n To ship that parcel via ground shipping, it will cost : $",ground_cost)

  ground_premium = 125
  print("\n ground shipping premium costs : $",ground_premium )

  ##drone shipping

  if drone_weight == 0:
    print("\nno weight inputted")
    drone_cost = 0
elif drone_weight <= 2:
  drone_cost = drone_weight * 4.50
elif drone_weight >= 2 and drone_weight <= 6:
  drone_cost = drone_weight * 9.00
elif drone_weight >= 6 and drone_weight <= 10:
  drone_cost = drone_weight * 12.00
else:
  if drone_weight >= 10:
    drone_cost = drone_weight * 14.25

if drone_weight != 0:
  print("\n To ship that parcel via drone shipping, it will cost : $",drone_cost)


