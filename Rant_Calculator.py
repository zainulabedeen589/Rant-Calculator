## Inputs we need fron the user
# Total rent
# Total food ordered for snacking
# Electricity unit spand
# Charge per unit
# Person living in room/flat

## Output
# Total amount you've to pay is

rent = int(input("Enter your hostal/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the number of persons living in room/flat = "))

total_bil = electricity_spend * charge_per_unit
output = (food + rent + total_bil) / person
print("Each person will pay = ", output)
