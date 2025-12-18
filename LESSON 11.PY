print("we;come tp the tip calculator")

total_bill = float(input("what was the total bill?"))
tip_given = float(input("how much tip would you like to give?"))
bill_split =int(input("how many people to split the bill?"))

tip_as_percent = tip_given /100
total_tip_amount = total_bill * tip_as_percent
total_bill_amount = total_bill + total_tip_amount
people = total_bill_amount / bill_split


print(f" Each person should pay {people}")