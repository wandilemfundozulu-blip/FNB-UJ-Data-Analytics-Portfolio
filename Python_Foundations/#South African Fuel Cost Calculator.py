#South African Fuel Cost Calculator

#Ask the user the distance to travel
kilometres = float(input("Enter the current kilometres price per litre(R): "))

#Ask the user for the petrol per litre
petrol_price = float(input("Enter the current petrol price per litre: "))


#Calculate the litres needed
litres_needed = kilometres /10

#Calculate the total fuel cost
Total_cost = litres_needed*petrol_price

#Round off the total cost to 2 decimal places
Total_cost = round(Total_cost, 2)

#Display the results
print('\n==== FUEL COST ESTIMATE ====')
print(f"Distance to travel : {kilometres} km")
print(f'Petrol price       : R{petrol_price:.2f}per litre')
print(f"Fuel required      :{litres_needed:.2f}litres")
print(f"Estimated cost     :R{Total_cost:.2f}")
print("=====================================================")
