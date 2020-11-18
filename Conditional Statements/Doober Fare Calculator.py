# Chapter 1: Calculate the ride price
# We'll use our knowledge of if, elif and else conditionals
# to calculate a ride share fare depending on the chosen ride type.
# We'll create the variables ride_type and credits, calculate ride_price
# based on ride_type, then subtract credits for the final_price.
# Store the user's ride choice in the variable ride_type, set to "Black".
ride_type = 'Black'
# Credits are money for in-app purchases. Create a credits variable set to 4.
credit = 4
# Before we start calculating, create the variables ride_price
# and final_price and set them to 0. We'll update them later.
ride_price = 0
final_price = 0
# Next, code an if statement that checks if the user chose the first type of ride, "DooberX".
if ride_type == 'DooberX':
    # When the user chooses "DooberX", update the ride_price to 20.45 dollars.
    ride_price = 20.45
# For the next option, continue with an elif statement that uses == to check if ride_type is equal to "Black".
elif ride_type == 'Black':
    # If the user chose "Black", update ride_price to 37.9.
    ride_price = 37.9
# Finally, code an else: statement to cover any other type of ride.
else:
    # If ride_type is neither DooberX, nor Black, we'll update the ride_price to the standard 18.7.
    ride_price = 18.7

# Chapter 2: Use in-app credits
# Now that we've calculated the price depending on the ride type,
# display "Ride price":, and on the next line, ride_price.
print('Ride price: ')
print(ride_price)
# Next, let's adjust the fare price depending on credits.
# Code an if statement that uses > to check if credits is greater than 0.
if credit > 0:
    # If the user has any credits, we'll update final_price to ride_price minus credits.
    final_price = ride_price - credit
# Done! Now let's display the final price starting with "Final price:" and, on the next line, final_price.
print('Final price: ')
print(final_price)
# You did great!
# You've written a piece of code that uses conditionals to decide how much a Doober user pays for their ride.
