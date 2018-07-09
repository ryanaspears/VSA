# Name:
# Date:7/9/18

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here
"""
grade = raw_input("What grade are you in? ")
name = raw_input("What is your name? ")
years = 12 - int(grade)
grad = str(years)
name = name[0].upper() + name[1:].lower()
print name + ", you are " + grad + " year(s) from graduation."
current_day = 9
current_month = 7
month = raw_input("What is your birth month? (Numerical) ")
month = int(month)
if month >= current_month:
    month = month - current_month
elif month <= current_month:
    month = 12 - (month - current_month)
day = raw_input("What day were you born on? (Also numerical) ")
day = int(day)
if day >= current_day:
    day = day - current_day
elif day <= current_day:
    day = 30 - current_day - day
month = str(month)
day = str(day)
print "Your birthday is in " + month + " months and " + day + " days."
"""
age = raw_input("How old are you?")
age = int(age)
if 13 <= age > 17:
    print"You can watch G, PG, and PG-13 movies."
elif 8 <= age < 13:
    print"You can watch G and PG movies."
elif age < 8:
    print"You can only watch G movies."
elif age >= 17:
    print"You can watch G, PG, PG-13, and R movies."
