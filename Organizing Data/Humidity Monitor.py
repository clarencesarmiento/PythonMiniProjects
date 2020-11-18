# Adding the newest data
# Let's use a list to manage soil humidity data received from a greenhouse monitor.
# We'll use the list to track at over five days.
# Every day at noon, we'll add the newest humidity value to the beginning of the list,
# and remove the oldest value.
# Start by coding an empty humidity_level list, to hold the humidity values over five days.
# Complete the list containing the values for the previous five days
# by coding a comma and the last value, 87.
humidity_level = [87, 83, 89, 88, 87]
# To add the newest humidity value at the beginning of the list,
# start by coding humidity_level and .insert().
# To insert the newest value at the beginning of the list, code 0 for the index, a comma, and then 90.
humidity_level.insert(0, 90)
# Next, display the updated list to check out the new value at the beginning.
print(humidity_level)
# Since we only want to keep five values in our list, use an instruction to remove the last value.
humidity_level.pop()
# Finally, display the final version of the list storing the humidity values over five days.
print(humidity_level)
# Great job using insert() and pop() to keep the humidity values list up to date.
# Run the code to give it another look.
