import calendar

# ask of month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month (in numbers 01-12): "))

# display the calendar
print(calendar.month(yy, mm))

