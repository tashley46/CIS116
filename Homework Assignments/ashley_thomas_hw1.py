
# File Name: Tommy_Ashley_hw1
# Author: Tommy Ashley
# Section: 8
# Description: The seed planting density calculator asks for a user to input
#              to input the user's field's length, width, spacing being crop
#              rows, spacing between seeds, cost of a seed, crop type, speed
#              of their tractor, and amount of plantings per year.
#
#              Using the information, the calculator outputs the amount of rows
#              needed, seeds per row, total seeds, total seed cost for one
#              planting, total seed cost for a year of planting, and average
#              monthly cost


#----------------------------------------------------------------------------------------------
#                                       PART: ONE
#----------------------------------------------------------------------------------------------

print("Welcome to the Seed Planting Density Calculator! \n")

#User values for various measurements in specified units
#-------------------------------------------------------------------------------------
field_len = float(input("Enter field length (yards): "))
field_wid = float(input("Enter field width (meters): "))
row_space = float(input("Enter spacing between rows (inches): "))
seed_space = float(input("Enter spacing between seeds (centimeters): "))
seed_cost = float(input("Enter cost per seed: "))
crop_type = input("What crop is being planted: ")
tractor_speed = float(input("Enter how fast the tractor can plant seeds (mph): "))
#-------------------------------------------------------------------------------------

#Calculate the amounts rows, seeds per row, and total seeds while converting units into feet
#-------------------------------------------------------------------------------------
rows = (field_wid * 3.28084) / (row_space / 12)
seed_per_row = (field_len * 3) / (seed_space * 0.0328084) 
total_seeds = rows * seed_per_row
#-------------------------------------------------------------------------------------

#print calculated values using fprint and rounds to the nearest whole number
#-------------------------------------------------------------------------------------
print(f"Rows in field: {rows:.0f} \n")
print(f"Seeds per row: {seed_per_row:.0f} \n")
print(f"Total seeds needed: {total_seeds:.0f} \n")
#-------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
#                                       PART: TWO
#----------------------------------------------------------------------------------------------


#User inputs amount of plantings per year
#-------------------------------------------------------------------------------------
plantings_per_year = int(input("Enter plantings per year: "))
#-------------------------------------------------------------------------------------

#Calculate the cost of one planting, the yearly cost, and average monthly cost
#-------------------------------------------------------------------------------------
cost_one_planting = total_seeds * seed_cost
cost_yearly = cost_one_planting * plantings_per_year
avg_cost_monthly = cost_yearly / 12
#-------------------------------------------------------------------------------------

#Print calculated values using fprint and rounding to the 2nd decimal place
#-------------------------------------------------------------------------------------
print(f"Total seed cost (one planting): ${cost_one_planting:.2f} \n")
print(f"Total seed cost per year: ${cost_yearly:.2f} \n")
print(f"Average cost per month: ${avg_cost_monthly:.2f} \n")
#-------------------------------------------------------------------------------------