try:
    number = int(input("Enter a number:"))
    result = 10 / number
    print("The result is ", result)
except ValueError:
    print("you must enter a valid integer")
except ZeroDivisionError:
    print("you cannot divide by zero.")
    
   
years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1920, 1996]
years.reverse()
print(years)
assert years[0] <= years[-1], "first element greater than last element"
