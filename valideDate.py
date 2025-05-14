from leapYear import isLeapYear

def validateDate(day, month, year):
    if( month in [4,6,9,11] and day > 30):
        return False
    elif( isLeapYear(year) == True and month == 2 and 30 > day):
        return True
    elif( month in [2] and day > 28):
        return False
    elif( year < 0):
        return False
    elif (day < 1) or (day > 31):
        return False
    elif(month < 1) or (month > 12):
        return False
    return True


def main():
    day   = int(input("Gib ein Tag ein: "))
    month = int(input("Gib ein Monat ein: "))
    year  = int(input("Gib ein Jahr ein: "))
    print(validateDate(day, month, year))

if __name__ == "__main__":
    main()


