import pyinputplus as pyip
print("\nExample 1")
result = pyip.inputInt("Enter the number of shopping bags you will need for your items:", min=0)
print("\nYou will use",result, "store bags.")

print("\nExample 2")
result = pyip.inputMenu( ["red", "blue", "green"], lettered=False, numbered=True)
print("\nYou have chosen a", result, "marker")

result = pyip.inputEmail("Enter your email address:")

print("\nThe email you entered:", result)