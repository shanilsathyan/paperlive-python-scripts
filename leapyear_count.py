def is_leap_year(year):
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        return True
    else:
        return False

start_year = int(input("enter the starting year: "))
end_year = int(input("enter the ending year: "))

count = 0

for year in range(start_year, end_year+1):
    if is_leap_year(year):
        print(year, "is a leap year")
    else:
        print(year, "not a leap year")

print ("Number of leap years", start_year, "and", end_year, "are: ", count)