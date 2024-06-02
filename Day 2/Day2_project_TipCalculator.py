#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to Deep's tip calculator")
total = float(input("Bill Total?"))
no_of_people = int(input("Number of people to split bill?"))
tip = float(input("Tip percentage?, 10,12, or 15?"))/100
total *= (1+tip) / no_of_people
# rounded_total = round(total,2) PRINTS 33.6 ratehr than 33.60
rounded_total = "{:.2f}".format(total)
print(f"Each person should pay: ${rounded_total}")

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇