print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
tip_percent = float(input("What percentage tip would you like to give? "))
total_people = float(input("How many people are splitting the bill? "))

total_ind = round((total + (total * (tip_percent / 100))) / total_people, 2)

print(f"Each person should pay ${total_ind}.")
