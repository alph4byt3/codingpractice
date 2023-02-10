# Shipping calculator

# Define variables
weight = 1
cost = 0
ground_flat_charge = 20
ground_premium_flat_charge = 125.00

# Ground shipping
if weight <= 2: # Price per pound - $1.50
  cost = ground_flat_charge + weight * 1.50
  print("Ground shipping cost")
  print("--------------------")
  print("Total - $" + str(cost))
elif (weight > 2) and (weight <=6): # Price per pound - $3.00
  cost = ground_flat_charge + weight * 3.00
  print("Ground shipping cost")
  print("--------------------")
  print("Total - $" + str(cost))
elif (weight > 6) and (weight <=10): # Price per pound - $4.00
  cost = ground_flat_charge + weight * 4.00
  print("Ground shipping cost")
  print("--------------------")
  print("Total - $" + str(cost))
elif weight > 10: # Price per pound - $4.75
  cost = ground_flat_charge + weight * 4.75
  print("Ground shipping cost")
  print("--------------------")
  print("Total - $" + str(cost))
else:
  print("No weight value detected")

# Ground premium shipping
print("")
print("Ground shipping premium cost")
print("----------------------------")
print("Total - $" + str(ground_premium_flat_charge))

# Drone shipping
if weight <= 2: # Price per pound - 4.50
  cost = weight * 4.50
  print("")
  print("Drone shipping cost")
  print("-------------------")
  print("Total - $" + str(cost))
elif (weight > 2) and (weight <=6): # Price per pound - $9.00
  cost = weight * 9.00
  print("")
  print("Drone shipping cost")
  print("-------------------")
  print("Total - $" + str(cost))
elif (weight > 6) and (weight <=10): # Price per pound - $12.00
  cost = weight * 12.00
  print("")
  print("Drone shipping cost")
  print("-------------------")
  print("Total - $" + str(cost))
elif weight > 10: # Price per pound - $14.25
  cost = weight * 14.25
  print("")
  print("Drone shipping cost")
  print("-------------------")
  print("Total - $" + str(cost))
else:
  print("No weight value detected")
