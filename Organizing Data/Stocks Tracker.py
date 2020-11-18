# Chapter 1: Updating the newest value
# Let's use a list to keep track of a company's stock values.
# We'll store the latest, highest, and lowest stock values in a list and then,
# update it when new values are recorded.
# Start by creating an empty list called apple_stocks, to store the stock values.
# Inside the list, code the newest stock value 298.18,
# then the highest value 304.18, and finally the lowest, 289.23.
apple_stocks = [298.18, 304.18, 289.23]
# There's a new stock value available, so we'll update the stock in the first position.
# Start by accessing apple_stocks[] at index 0.
# Next, code = followed by the newest value, 310, to update the list.
apple_stocks[0] = 310
# To display the update to the latest value, start with the string "latest value:".
print('Latest value:')
# Next, code a display statement, and inside it, access the first value in the apple_stocks list.
print(apple_stocks[0])
# Chapter 2: Updating the highest value
# The newest stock value, 310, is greater than the list's previous highest stock value,
# 304.18, so we'll update it.
# To update the highest stock value, start by accessing the second element of the list.
# The newest value is the highest value, so update the value at index 1 to 310.
apple_stocks[1] = 310
# Like before, start tracking the list updates by displaying "highest value:".
print('Highest value:')
# To display the updated highest value, access apple_stocks[] at index 1.
print(apple_stocks[1])
# To display the lowest value, start with "lowest value:" and on the second line, display the last list element.
print('Lowest value:')
print(apple_stocks[2])
# Great job using indices to manage and update a list of stock values.
