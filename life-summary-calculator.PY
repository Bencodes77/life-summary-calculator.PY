# Ask for user's age& greet the user.
print("WELOME TO THE LIFE SUMMARY CALCULATOR")
print("===================================")
print("This calculator will show you how much time you have spent and how much time you have left based on a life expectancy of 90 years.")
print("===================================================================================================================================")
name = input("what  is your name? ")
print(f"hi {name}, let's get started!")
age = int(input("What is your age? "))

# Calculate time spent
years_spent = age
months_spent = years_spent * 12
weeks_spent = years_spent * 52
days_spent = years_spent * 365

# Calculate time left (assuming life expectancy = 90 years)
years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

# Display results in table format
print("\n========== LIFE SUMMARY ==========")
print(f"{'Category':<15}{'Time Spent':<20}{'Time Left'}")
print("-------------------------------------------")
print(f"{'Years':<15}{years_spent:<20}{years_left}")
print(f"{'Months':<15}{months_spent:<20}{months_left}")
print(f"{'Weeks':<15}{weeks_spent:<20}{weeks_left}")
print(f"{'Days':<15}{days_spent:<20}{days_left}")
print("===========================================")
print("Thank you for using the Life Summary Calculator. Live well!")
