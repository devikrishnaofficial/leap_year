def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not a leap year")
        else:
            print("Leap Year")
    else:
        print("Not a leap year")

user_year = int(input("Enter a year: "))

is_leap_year(user_year)


