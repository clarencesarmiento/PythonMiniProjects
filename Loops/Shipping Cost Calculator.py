# Chapter 1: Shipping Destination
# Let's use our knowledge of if, elif, and else statements to code a shipping cost calculator.
# We'll save the destination type and total purchase cost in variables,
# then we'll update the shipping cost based on the destination.
# To keep track of the destination type, set the variable international_shipping to True.
international_shipping = True
# For the purchase cost, create the variable total and set it to 150.
# Then, create the variable shipping_cost and set it to 0.
total = 150
shipping_cost = 0
# To adapt the cost to the destination type, code an if statement that uses international_shipping as the condition.
if international_shipping:
    # If the shipping is international, use self-assignment to increase shipping_cost by 15.
    shipping_cost += 15
    # To inform the user about the extra cost, display International base cost applied inside the if block.
    print('International base cost applied')

# Chapter 2: Extra Costs
# Next, we'll update the shipping cost based on the total purchase.
# The higher the total, the cheaper the shipping will be.
# Start with an if statement that checks if total is less than or equal to 50.
if total <= 50:
    # If the purchase total is at most 50$, use self-assignment to increase shipping_cost by 20.
    shipping_cost += 20
# Next, code an elif statement for cases where the total is less than or equal to 100.
elif total <= 100:
    # If the purchase total is over 50, but at most 100, use self-assignment to increase shipping_cost by 15.
    shipping_cost += 15
# Finally, code an else: statement to cover the cases where the total is over 100$.
else:
    # If the total purchase is over 100, use self-assignment to increase shipping_cost by 5.
    shipping_cost += 5
# Display the shipping cost with an f-string that contains Shipping cost:, and the shipping_cost variable.
print(f'Shipping cost: {shipping_cost}')
