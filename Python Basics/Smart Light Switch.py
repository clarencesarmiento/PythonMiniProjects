# Let's create a smart light switch that switches the lights off if it's daytime and on if it's nighttime.
# Start by creating an is_day variable.
# Let's say it's daytime, so set is_day to True.
is_day = True
# To keep the lights off during the day, create a lights_on variable that stores False.
lights_on = False
# Now use print() to display Daytime? in the console.
print('Is it Daytime?')
# Display the value of the is_day variable in the console.
print(is_day)
# Time to check on the status of the light! Start by displaying Lights on?.
print('lights on?')
# Next, display the value of the lights_on variable.
print(lights_on)
# Let's play with our program.
# Now let's simulate what happens during the night. Temporarily set is_day to False.
is_day = False
# When it's not daytime, the lights should be on, so use not to update lights_on to the opposite of is_day.
lights_on = not is_day
# There we go!
# We've written some code that checks if it's daytime or nighttime and switches the lights on and off accordingly.
