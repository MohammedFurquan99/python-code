def is_leap(year):
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    


#print(is_leap(2008))
year = int(input("Enter the year:"))
print(is_leap(year))
    